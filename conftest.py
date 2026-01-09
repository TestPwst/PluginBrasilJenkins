import pytest
import os
import shutil
from datetime import datetime

try:
    import pytest_html
except ImportError:
    pytest_html = None

_logo_filename = "Logotest.png"
_logo_relative_path = None  # Se definirá dinámicamente


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and pytest_html:
        if hasattr(item, 'user_properties'):
            for prop_name, prop_value in item.user_properties:
                if prop_name == "screenshot":
                    extra = getattr(report, 'extra', [])
                    extra.append(pytest_html.extras.html(prop_value))
                    report.extra = extra


def pytest_configure(config):
    global _logo_relative_path

    ruta_html = getattr(config.option, "htmlpath", None)
    if ruta_html:
        carpeta_html = os.path.dirname(os.path.abspath(ruta_html))

        # Copiar el logo junto al HTML
        origen_logo = os.path.join("resources", _logo_filename)
        destino_logo = os.path.join(carpeta_html, _logo_filename)

        if os.path.exists(origen_logo):
            shutil.copy(origen_logo, destino_logo)
            # Solo guardamos el nombre del archivo para que sea relativo al HTML
            _logo_relative_path = _logo_filename


def pytest_html_report_title(report):
    nombre_automatizacion = os.getenv("NOMBRE_TEST", "Automatizaciones testing")
    report.title = f"Reporte de Pruebas - PowerStreet EAL Brasil - {nombre_automatizacion}"


def pytest_html_results_table_header(cells):
    cells.insert(2, '<th class="sortable" col="time">Tiempo</th>')
    cells.insert(3, '<th class="sortable" col="screenshot">Captura</th>')


def pytest_html_results_table_row(report, cells):
    cells.insert(2, f'<td>{getattr(report, "duration", 0):.2f}s</td>')

    screenshot_cell = '<td>—</td>'
    if hasattr(report, 'extra') and report.extra:
        for extra in report.extra:
            if hasattr(extra, 'html') and 'img src' in str(extra.html):
                screenshot_cell = '<td>IMG</td>'
                break
    cells.insert(3, screenshot_cell)


def pytest_html_results_summary(prefix, summary, postfix):
    global _logo_relative_path
    if _logo_relative_path:
        logo_html = f'<div style="margin-bottom:10px;"><img src="{_logo_relative_path}" alt="Logo" height="90"/></div>'
    else:
        logo_html = '<div style="margin-bottom:10px;"><strong>[Logo no disponible]</strong></div>'

    autor_html = '<p><strong>Autor:</strong> TESTING </p>'
    fecha_html = f'<p><strong>Fecha de ejecución:</strong> {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>'

    prefix.extend([logo_html, autor_html, fecha_html])

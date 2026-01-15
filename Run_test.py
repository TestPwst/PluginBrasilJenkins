import os
import time
import subprocess
import datetime
import logging

MODO_DEBUG = False


def configurar_logger(log_file_path):
    """Configura el logger principal para la ejecución de pruebas"""
    log_level = logging.DEBUG if MODO_DEBUG else logging.INFO
    log_silenciado = logging.DEBUG if MODO_DEBUG else logging.WARNING

    logging.basicConfig(
        level=log_level,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file_path, mode='w', encoding='utf-8'),
            logging.StreamHandler()
        ]
    )

    # Silenciar módulos
    for modulo in ['selenium', 'urllib3', 'asyncio']:
        logging.getLogger(modulo).setLevel(log_silenciado)


def ejecutar_tests():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Carpeta raíz de resultados
    carpeta_resultado = os.path.join("results", timestamp)
    os.makedirs(carpeta_resultado, exist_ok=True)

    # Carpeta de logs
    carpeta_logs = os.path.join(carpeta_resultado, "logs")
    os.makedirs(carpeta_logs, exist_ok=True)
    log_file_path = os.path.join(carpeta_logs, "execution.log")
    configurar_logger(log_file_path)

    rutas_base = ["BRASIL/Prioridad_ALTA"]
    nombres_excluidos = ("FuncionesGral.py", "VariablesGral.py", "base_test.py", "__init__.py")
    extensiones_validas = (".py",)

    for base in rutas_base:
        for carpeta, _, archivos in os.walk(base):
            for archivo in archivos:
                if archivo.endswith(extensiones_validas) and archivo not in nombres_excluidos:
                    ruta_test = os.path.join(carpeta, archivo)
                    modulo = base.split(os.sep)[0]  # Enterprise o EAL
                    nombre_base = os.path.splitext(archivo)[0]

                    # Subcarpeta relativa como TEST
                    subfolder_relativa = os.path.relpath(carpeta, base)
                    ruta_reporte_modulo = os.path.join(carpeta_resultado, modulo, subfolder_relativa)
                    os.makedirs(ruta_reporte_modulo, exist_ok=True)

                    # Assets para capturas
                    carpeta_assets = os.path.join(ruta_reporte_modulo, "assets")
                    os.makedirs(carpeta_assets, exist_ok=True)

                    # Guardar capturas en carpeta del test
                    os.environ["ASSETS_DIR"] = carpeta_assets

                    # Define el nombre de la prueba
                    os.environ["NOMBRE_TEST"] = nombre_base

                    nombre_reporte = f"{nombre_base}.html"
                    ruta_reporte = os.path.join(ruta_reporte_modulo, nombre_reporte)

                    comando = [
                        "pytest",
                        ruta_test,
                        "--html=" + ruta_reporte,
                        "--self-contained-html",
                        "--css=resources/custom.css",  # nuevo
                        "-v"
                    ]

                    logging.info(f"Ejecutando prueba: {ruta_test}")
                    resultado = subprocess.run(comando, capture_output=True, text=True)

                    logging.info(f"Reporte generado en: {ruta_reporte}")
                    if resultado.returncode != 0:
                        logging.error(f"Errores encontrados:\n{resultado.stderr}")
                    else:
                        logging.info("Prueba completada sin errores.")

                    logging.info("Esperando la siguiente ejecución...")
                    time.sleep(300)


if __name__ == "__main__":
    ejecutar_tests()

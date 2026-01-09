from FuncionesGralBrasil import *
from Configuracion import *


# Configuración general de la plantilla

def ingreso_app(self):
    try:
        FuncionesBrasil.ingreso_app(self)
    except Exception as e:  # pragma: no cover
        Log().error(f"No se logró ingresar a la aplicación, validar el error: {e}")
        raise


def configuracion_inicial(self):
    try:
        FuncionesBrasil.cargar(self)
    except Exception as e:  # pragma: no cover
        Log().error(f"No se logró ingresar a la aplicación, validar el error: {e}")
        raise

    try:
        FuncionesBrasil.registro_punto(self)
    except Exception as e:  # pragma: no cover
        Log().error(f"No se logró ingresar a la aplicación, validar el error: {e}")
        raise


def pegar_funcion():
    try:
        # ==================================================
        #      PEGAR CÓDIGO DE APPIUM RECORDER ABAJO
        # ==================================================
        pegar_funcion()
    # ==================================================
    #                 FIN DEL PEGADO
    # ==================================================
    except Exception as e:  # pragma: no cover
        Log().error(f"No se logró dar click al botón instalar, validar el error: {e}")
        raise


class Test:
    def test_001(self):
        ingreso_app(self)

    def test_002(self):
        configuracion_inicial(self)

    def test_003(self):
        pegar_funcion()

import time

from FuncionesGralBrasil import *
from Configuracion import *

# Variables Globales
salvar = "new UiSelector().text(\"Salvar\")"
aceitar = "new UiSelector().text(\"Aceitar\")"
bar_cliente = "new UiSelector().text(\"BAR E MERCEARIA PARA PEDRO LTDA\")"


def ingreso_app(self, request):
    try:
        Log().info("Iniciando ingreso a la aplicación")
        FuncionesBrasil.ingreso_app(self)
        FuncionesBrasil.captura_pantalla(driver, "FLJ04-Ingreso App", request)
    except Exception as e:  # pragma: no cover
        Log().error(f"No se logró ingresar a la aplicación, validar el error: {e}")
        raise


def configuracion_inicial(self, request):
    try:
        Log().info("Iniciando carga de usuario")
        FuncionesBrasil.cargar(self)
        FuncionesBrasil.captura_pantalla(driver, "FLJ04-Carga Usuario", request)
    except Exception as e:  # pragma: no cover
        Log().error(f"No se logró cargar usuario, validar el error: {e}")
        raise

    try:
        Log().info("Iniciando registro de punto")
        FuncionesBrasil.registro_punto(self)
        FuncionesBrasil.captura_pantalla(driver, "FLJ04-Registro Punto", request)
    except Exception as e:  # pragma: no cover
        Log().error(f"No se logró registrar punto, validar el error: {e}")
        raise


# FLUJO 4 : SIN VENTA


def pegar_funcion(request):
    try:
        # ==================================================
        #      PEGAR CÓDIGO DE APPIUM RECORDER ABAJO
        # ==================================================
        # Seleccionar cliente BAR E MERCEARIA PARA PEDRO LTDA
        cliente = (AppiumBy.ANDROID_UIAUTOMATOR, bar_cliente)

        Log().info("Buscando cliente BAR E MERCEARIA PARA PEDRO LTDA")
        selector = driver.find_elements(*cliente)

        if selector:
            Log().info("Cliente BAR E MERCEARIA PARA PEDRO LTDA encontrado")
            cliente_encontrado = wait.until(EC.element_to_be_clickable(cliente))
            cliente_encontrado.click()
            cliente_encontrado.click()
            Log().info("Cliente encontrado y seleccionado directamente")
            FuncionesBrasil.captura_pantalla(driver, "FLJ04-Cliente Seleccionado", request)
        else:
            Log().info("Cliente no visible, realizando scroll")
            scroll_script = (
                'new UiScrollable(new UiSelector().scrollable(true))'
                '.scrollIntoView(new UiSelector().text("BAR E MERCEARIA PARA PEDRO LTDA")).instance(0)')

            # Ejecutar scroll
            driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, scroll_script)

            # Esperar a que sea clickable después del scroll
            cliente_encontrar = wait.until(EC.element_to_be_clickable(cliente))
            time.sleep(2)
            cliente_encontrar.click()
            cliente_encontrar.click()
            Log().info("Cliente encontrado después de scroll y seleccionado")
            FuncionesBrasil.captura_pantalla(driver, "FLJ04-Cliente Scroll", request)

        Log().info("Accediendo a datos del cliente")
        el2 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                     "new UiSelector().text(\"Dados do cliente\")")))
        el2.click()
        
        Log().info("Iniciando visita")
        el3 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                     "new UiSelector().text(\"Iniciar visita\")")))
        el3.click()
        el4 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, aceitar)))
        el4.click()
        
        Log().info("Finalizando sin venta")
        el5 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                     "new UiSelector().text(\"Finalizar sem venda\")")))
        el5.click()
        FuncionesBrasil.captura_pantalla(driver, "FLJ04-Finalizar Sin Venta", request)

        Log().info("Seleccionando motivo de no venta")
        el6 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                     "new UiSelector().text(\"Falta de tempo\")")))
        el6.click()
        el7 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        el7.click()
        el8 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, aceitar)))
        el8.click()
        
        Log().info("Verificando registro sin venta")
        el9 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                     "new UiSelector().text(\"Sem venda\n1\")")))
        el9.click()
        FuncionesBrasil.captura_pantalla(driver, "FLJ04-Sin Venta Registrada", request)

        Log().info("Completando flujo")
        el10 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, bar_cliente)))
        el10.click()

        # ==================================================
        #                 FIN DEL PEGADO
        # ==================================================
    except Exception as e:  # pragma: no cover
        Log().error(f"Error en la función principal, validar el error: {e}")
        raise


class Test:
    def test_001(self, request):
        ingreso_app(self, request)

    def test_002(self, request):
        configuracion_inicial(self, request)

    def test_003(self, request):
        pegar_funcion(request)
from FuncionesGralBrasil import *
from Configuracion import *

# Variables Globales
salvar = "new UiSelector().text(\"Salvar\")"
boton = "android:id/button2"
imagen = "android.widget.ImageView"
lucio_cliente = "new UiSelector().text(\"LUCIO LUIZ NUNES DE OLIVEIRA\")"
finalizar = "new UiSelector().text(\"Finalizar\")"
image_view_0 = "new UiSelector().className(\"android.widget.ImageView\").instance(0)"


def ingreso_app(self, request):
    try:
        Log().info("Iniciando ingreso a la aplicación")
        FuncionesBrasil.ingreso_app(self)
        FuncionesBrasil.captura_pantalla(driver, "FLJ02-Ingreso App", request)
    except Exception as e:  # pragma: no cover
        Log().error(f"No se logró ingresar a la aplicación, validar el error: {e}")
        raise


def configuracion_inicial(self, request):
    try:
        Log().info("Iniciando carga de usuario")
        FuncionesBrasil.cargar(self)
        FuncionesBrasil.captura_pantalla(driver, "FLJ02-Carga Usuario", request)
    except Exception as e:  # pragma: no cover
        Log().error(f"No se logró cargar usuario, validar el error: {e}")
        raise

    try:
        Log().info("Iniciando registro de punto")
        FuncionesBrasil.registro_punto(self)
        FuncionesBrasil.captura_pantalla(driver, "FLJ02-Registro Punto", request)
    except Exception as e:  # pragma: no cover
        Log().error(f"No se logró registrar punto, validar el error: {e}")
        raise


# Visitas fuera de Ruta


def pegar_funcion(request):
    try:
        # ==================================================
        #      PEGAR CÓDIGO DE APPIUM RECORDER ABAJO
        # ==================================================
        Log().info("Accediendo al menú principal")
        el101 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, image_view_0)))
        el101.click()
        
        Log().info("Seleccionando visitas fuera de ruta")
        el102 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                       "new UiSelector().text(\"Visitas fora de rota\")")))
        el102.click()
        FuncionesBrasil.captura_pantalla(driver, "FLJ02-Visitas Fuera Ruta", request)

        Log().info("Buscando cliente")
        el103 = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, "Pesquisar")))
        el103.click()
        el103.send_keys("111")
        driver.execute_script('mobile:pressKey', {"keycode": 4})
        el104 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, lucio_cliente)))
        el104.click()
        el104.click()
        FuncionesBrasil.captura_pantalla(driver, "FLJ02-Cliente Seleccionado", request)

        Log().info("Accediendo a datos del cliente")
        el105 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                       "new UiSelector().text(\"Dados do cliente\")")))
        el105.click()
        
        Log().info("Iniciando visita")
        el106 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                       "new UiSelector().text(\"Iniciar visita\")")))
        el106.click()

        el1 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                     "new UiSelector().text(\"Aceitar\")")))
        el1.click()
        
        Log().info("Realizando venta")
        el2 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                     "new UiSelector().text(\"Realizar venda\")")))
        el2.click()
        FuncionesBrasil.captura_pantalla(driver, "FLJ02-Realizar Venda", request)

        Log().info("Seleccionando productos")
        el109 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                       "new UiSelector().className("
                                                       "\"android.widget.ImageView\").instance(4)")))
        el109.click()
        el109.click()
        el109.click()
        el109.click()
        el110 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                       "new UiSelector().className("
                                                       "\"android.widget.ImageView\").instance(26)")))
        el110.click()
        el110.click()
        el110.click()
        
        Log().info("Accediendo a Sinergia")
        el111 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                       "new UiSelector().text(\"Sinergia\")")))
        el111.click()
        el112 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                       "new UiSelector().className("
                                                       "\"android.widget.ImageView\").instance(19)")))
        el112.click()
        el112.click()
        el112.click()
        FuncionesBrasil.captura_pantalla(driver, "FLJ02-Productos Sinergia", request)

        Log().info("Finalizando selección de productos")
        el6 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, finalizar)))
        el6.click()
        
        Log().info("Configurando método de pago")
        el7 = wait.until(EC.element_to_be_clickable((AppiumBy.CLASS_NAME, imagen)))
        el7.click()
        el8 = wait.until(EC.element_to_be_clickable((AppiumBy.ID, boton)))
        el8.click()
        el9 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                     "new UiSelector().text(\"Cartão de crédito\")")))
        el9.click()
        el10 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        el10.click()
        
        Log().info("Ingresando datos de tarjeta")
        el11 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                      "new UiSelector().className("
                                                      "\"android.widget.TextView\").instance(20)")))
        el11.click()
        el12 = wait.until(EC.element_to_be_clickable((AppiumBy.ID, "uy.com.assist.eaf:id/contextmenu_item_text")))
        el12.click()
        el13 = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID,
                                                      "Adesivo no comprovante (escrito SN)")))
        el13.click()
        el13.send_keys("1234")
        driver.execute_script('mobile: pressKey', {"keycode": 4})
        el14 = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID,
                                                      "Últimos 6 dígitos do STONE ID")))
        el14.click()
        el14.send_keys("1234567")
        driver.execute_script('mobile: pressKey', {"keycode": 4})
        FuncionesBrasil.captura_pantalla(driver, "FLJ02-Datos Tarjeta", request)

        Log().info("Guardando y finalizando pedido")
        el15 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        el15.click()
        el16 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                      "new UiSelector().text(\"Finalizar pedido\")")))
        el16.click()
        el17 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        el17.click()

        Log().info("Verificando pedidos finalizados")
        el129 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, image_view_0)))
        el129.click()
        el130 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                       "new UiSelector().text(\"Finalizadas\n1\")")))
        el130.click()
        FuncionesBrasil.captura_pantalla(driver, "FLJ02-Pedidos Finalizados", request)

        Log().info("Accediendo a cliente finalizado")
        el131 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, lucio_cliente)))
        el131.click()
        el132 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                       "new UiSelector().text(\"Fora de rota\n1\")")))
        el132.click()
        FuncionesBrasil.captura_pantalla(driver, "FLJ02-Cliente Fuera Ruta", request)

        Log().info("Completando flujo")
        el133 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, lucio_cliente)))
        el133.click()
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
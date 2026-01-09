from FuncionesGralBrasil import *
from Configuracion import *

# Variables Globales
cliente = "new UiSelector().text(\"CAFE E BAR SAO CRISTOVAO LTDA\")"
salvar = "new UiSelector().text(\"Salvar\")"
boton = "android:id/button2"
imagen = "android.widget.ImageView"
# Variables repetidas identificadas
sim = "new UiSelector().text(\"Sim\")"
finalizar = "new UiSelector().text(\"Finalizar\")"
image_view_15 = "new UiSelector().className(\"android.widget.ImageView\").instance(15)"
text_view_24 = "new UiSelector().className(\"android.widget.TextView\").instance(24)"
numero_2 = "new UiSelector().text(\"2\")"


def ingreso_app(self, request):
    try:
        Log().info("Iniciando ingreso a la aplicación")
        FuncionesBrasil.ingreso_app(self)
        FuncionesBrasil.captura_pantalla(driver, "FLJ01-Ingreso App", request)
    except Exception as e:  # pragma: no cover
        Log().error(f"No se logró ingresar a la aplicación, validar el error: {e}")
        raise


def configuracion_inicial(self, request):
    try:
        Log().info("Iniciando carga de usuario")
        FuncionesBrasil.cargar(self)
        FuncionesBrasil.captura_pantalla(driver, "FLJ01-Carga Usuario", request)
    except Exception as e:  # pragma: no cover
        Log().error(f"No se logró cargar usuario, validar el error: {e}")
        raise

    try:
        Log().info("Iniciando registro de punto")
        FuncionesBrasil.registro_punto(self)
        FuncionesBrasil.captura_pantalla(driver, "FLJ01-Registro Punto", request)
    except Exception as e:  # pragma: no cover
        Log().error(f"No se logró registrar punto, validar el error: {e}")
        raise


def pegar_funcion(request):
    try:
        # ==================================================
        #      PEGAR CÓDIGO DE APPIUM RECORDER ABAJO
        # ==================================================
        Log().info("Seleccionando cliente")
        el135 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, cliente)))
        el135.click()
        el136 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, cliente)))
        el136.click()
        FuncionesBrasil.captura_pantalla(driver, "FLJ01-Ingreso Cliente", request)

        Log().info("Accediendo a datos del cliente")
        el137 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                       "new UiSelector().text(\"Dados do cliente\")")))
        el137.click()
        FuncionesBrasil.captura_pantalla(driver, "FLJ01-Datos Cliente", request)

        Log().info("Iniciando visita")
        el138 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                       "new UiSelector().text(\"Iniciar visita\")")))
        el138.click()
        el139 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                       "new UiSelector().text(\"Aceitar\")")))
        el139.click()
        
        Log().info("Realizando venta")
        el140 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                       "new UiSelector().text(\"Realizar venda\")")))
        el140.click()
        FuncionesBrasil.captura_pantalla(driver, "FLJ01-Realizar Venda", request)

        Log().info("Seleccionando productos")
        el141 = wait.until(EC.element_to_be_clickable((AppiumBy.ID, boton)))
        el141.click()
        el142 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, image_view_15)))
        el142.click()
        el142.click()
        el142.click()
        el142.click()
        time.sleep(2)
        
        Log().info("Finalizando selección de productos")
        el143 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, finalizar)))
        el143.click()
        FuncionesBrasil.captura_pantalla(driver, "FLJ01-Finalizar Venta", request)

        time.sleep(2)
        Log().info("Configurando método de pago")
        el144 = wait.until(EC.element_to_be_clickable((AppiumBy.CLASS_NAME, imagen)))
        el144.click()
        el145 = wait.until(EC.element_to_be_clickable((AppiumBy.ID, boton)))
        el145.click()
        el146 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                       "new UiSelector().text(\"Boleto\")")))
        el146.click()
        
        Log().info("Guardando configuración de pago")
        el147 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        el147.click()
        el148 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, sim)))
        el148.click()
        
        Log().info("Configurando fechas de pago")
        el149 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, text_view_24)))
        el149.click()
        el150 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, sim)))
        el150.click()
        el151 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, text_view_24)))
        el151.click()
        el152 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        el152.click()
        
        Log().info("Configurando días de parcelado")
        el153 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                       "new UiSelector().className("
                                                       "\"android.widget.TextView\").instance(21)")))
        el153.click()
        el154 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, numero_2)))
        el154.click()
        el155 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                       "new UiSelector().className("
                                                       "\"android.widget.TextView\").instance(22)")))
        el155.click()
        el156 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, numero_2)))
        el156.click()
        el157 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                       "new UiSelector().className("
                                                       "\"android.widget.TextView\").instance(35)")))
        el157.click()
        el158 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                       "new UiSelector().text(\"B470 - 2/2 dias, parcelado\")")))
        el158.click()
        FuncionesBrasil.captura_pantalla(driver, "FLJ01-Dias Parcelado", request)

        Log().info("Accediendo a ítems del pedido")
        el159 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                       "new UiSelector().text(\"Itens do pedido\")")))
        el159.click()
        el160 = wait.until(EC.element_to_be_clickable((AppiumBy.CLASS_NAME, imagen)))
        el160.click()
        
        Log().info("Guardando sin finalizar")
        el161 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        el161.click()
        el162 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                       "new UiSelector().text(\"Salvar sem finalizar\")")))
        el162.click()
        FuncionesBrasil.captura_pantalla(driver, "FLJ01-Salvar Sin Finalizar", request)

        Log().info("Accediendo a pendientes")
        el163 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        el163.click()
        el164 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                       "new UiSelector().text(\"Pendentes\n1\")")))
        el164.click()
        FuncionesBrasil.captura_pantalla(driver, "FLJ01-Ingreso Pendientes", request)

        el165 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, cliente)))
        el165.click()

        # Editar Venta Pendiente
        Log().info("Editando venta pendiente")
        el30 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                      "new UiSelector().text(\"Editar\")")))
        el30.click()
        FuncionesBrasil.captura_pantalla(driver, "FLJ01-Editar Pendiente", request)
        el31 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, image_view_15)))
        el31.click()
        el31.click()
        
        Log().info("Accediendo a Sinergia")
        el32 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                      "new UiSelector().text(\"Sinergia\")")))
        el32.click()
        FuncionesBrasil.captura_pantalla(driver, "FLJ01-Ingreso Sinergia", request)
        
        Log().info("Continuando con el flujo completo")
        el33 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                      "new UiSelector().className("
                                                      "\"android.widget.ImageView\").instance(19)")))
        el33.click()
        el33.click()
        el33.click()
        el33.click()
        el34 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, finalizar)))
        el34.click()
        FuncionesBrasil.captura_pantalla(driver, "FLJ01-Finalizar Venta Editada", request)
        
        Log().info("Configurando pago con tarjeta")
        el35 = wait.until(EC.element_to_be_clickable((AppiumBy.CLASS_NAME, imagen)))
        el35.click()
        el36 = wait.until(EC.element_to_be_clickable((AppiumBy.ID, boton)))
        el36.click()
        el37 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                      "new UiSelector().text(\"Cartão de crédito\")")))
        el37.click()
        el38 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        el38.click()
        
        Log().info("Ingresando datos de tarjeta")
        el39 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                      "new UiSelector().className("
                                                      "\"android.widget.TextView\").instance(20)")))
        el39.click()
        el40 = wait.until(EC.element_to_be_clickable((AppiumBy.ID, "uy.com.assist.eaf:id/contextmenu_item_text")))
        el40.click()
        el41 = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID,
                                                      "Adesivo no comprovante (escrito SN)")))
        el41.click()
        el41.send_keys("321")
        driver.execute_script('mobile:pressKey', {"keycode": 4})
        el42 = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID,
                                                      "Últimos 6 dígitos do STONE ID")))
        el42.click()
        el42.send_keys("7654")
        driver.execute_script('mobile:pressKey', {"keycode": 4})
        
        Log().info("Finalizando pedido")
        el43 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                      "new UiSelector().text(\"Itens do pedido\")")))
        el43.click()
        el44 = wait.until(EC.element_to_be_clickable((AppiumBy.CLASS_NAME, "android.widget.ImageView")))
        el44.click()
        el45 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        el45.click()
        el46 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                      "new UiSelector().text(\"Finalizar pedido\")")))
        el46.click()
        FuncionesBrasil.captura_pantalla(driver, "FLJ01-Finalizar Pedido", request)

        Log().info("Guardando pedido finalizado")
        el48 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        el48.click()

        Log().info("Verificando pedidos finalizados")
        el50 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                      "new UiSelector().text(\"Finalizadas\n1\")")))
        el50.click()
        el51 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, cliente)))
        el51.click()
        FuncionesBrasil.captura_pantalla(driver, "FLJ01-Finalizados", request)

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
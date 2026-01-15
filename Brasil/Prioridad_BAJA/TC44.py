# *****************************************
# TC44 - Pagos de Deuda
# *****************************************


from FuncionesGralBrasil import *
from Configuracion import *

# Variables Globales
salvar = "new UiSelector().text(\"Salvar\")"
aceitar = "new UiSelector().text(\"Aceitar\")"
info_financiera = "new UiSelector().text(\"Informação financeira\")"
image_view_0 = "new UiSelector().className(\"android.widget.ImageView\").instance(0)"
image_view_1 = "new UiSelector().className(\"android.widget.ImageView\").instance(1)"
boton = "android:id/button2"
niteroi_cliente = "new UiSelector().text(\"NITEROI ROD LANCHES LTDA ME\")"
press_back_key = {"keycode": 4}


def press_back():
    driver.execute_script('mobile:pressKey', press_back_key)


def ingreso_app(self, request):
    try:
        Log().info("Iniciando ingreso a la aplicación")
        FuncionesBrasil.ingreso_app(self)
        FuncionesBrasil.captura_pantalla(driver, "TC44-Ingreso App", request)
    except Exception as e:  # pragma: no cover
        Log().error(f"No se logró ingresar a la aplicación, validar el error: {e}")
        raise


def configuracion_inicial(self, request):
    try:
        Log().info("Iniciando carga de usuario")
        FuncionesBrasil.cargar(self)
        FuncionesBrasil.captura_pantalla(driver, "TC44-Carga Usuario", request)
    except Exception as e:  # pragma: no cover
        Log().error(f"No se logró cargar usuario, validar el error: {e}")
        raise

    try:
        Log().info("Iniciando registro de punto")
        FuncionesBrasil.registro_punto(self)
        FuncionesBrasil.captura_pantalla(driver, "TC44-Registro Punto", request)
    except Exception as e:  # pragma: no cover
        Log().error(f"No se logró registrar punto, validar el error: {e}")
        raise


def pegar_funcion(request):
    try:
        # ==================================================
        #      PEGAR CÓDIGO DE APPIUM RECORDER ABAJO
        # ==================================================

        # Seleccionar cliente NITEROI ROD LANCHES LTDA ME
        Log().info("Seleccionando cliente NITEROI ROD LANCHES")
        cliente_niteroi = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, niteroi_cliente)))
        cliente_niteroi.click()
        cliente_niteroi.click()
        FuncionesBrasil.captura_pantalla(driver, "TC44-Cliente Seleccionado", request)

        # Acceder a dados do cliente
        Log().info("Accediendo a dados do cliente")
        btn_dados = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                           "new UiSelector().text(\"Dados do cliente\")")))
        btn_dados.click()

        # Navegar a información financiera
        Log().info("Navegando a información financiera")
        btn_nav = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, image_view_1)))
        btn_nav.click()

        # Acceder a información financiera
        Log().info("Accediendo a información financiera")
        btn_info_financiera = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, info_financiera)))
        btn_info_financiera.click()
        FuncionesBrasil.captura_pantalla(driver, "TC44-Info Financiera", request)

        # Seleccionar cuenta específica
        Log().info("Seleccionando cuenta específica")
        cuenta_especifica = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                   "new UiSelector().text(\"003423622-2 - 14\")")))
        cuenta_especifica.click()

        # Revisar montos de deuda
        Log().info("Revisando montos de deuda")
        montos_deuda = ["225,40", "182,85", "190,90"]
        for monto in montos_deuda:
            monto_item = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                f"new UiSelector().text(\"{monto}\")")))
            monto_item.click()
        FuncionesBrasil.captura_pantalla(driver, "TC44-Montos Revisados", request)

        # Regresar al menú principal
        Log().info("Regresando al menú principal")
        btn_back = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, image_view_0)))
        btn_back.click()

        # Iniciar visita
        Log().info("Iniciando visita")
        btn_iniciar = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                             "new UiSelector().text(\"Iniciar visita\")")))
        btn_iniciar.click()

        # Confirmar inicio de visita
        Log().info("Confirmando inicio de visita")
        confirmacion = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                              "new UiSelector().text(\"Tem certeza de que deseja "
                                                              "iniciar a visita ao cliente?\")")))
        confirmacion.click()

        btn_aceitar = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, aceitar)))
        btn_aceitar.click()
        FuncionesBrasil.captura_pantalla(driver, "TC44-Visita Iniciada", request)

        # Navegar nuevamente a información financiera
        Log().info("Segunda navegación a información financiera")
        btn_nav2 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, image_view_1)))
        btn_nav2.click()

        btn_info_financiera2 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, info_financiera)))
        btn_info_financiera2.click()

        # Seleccionar monto para pago
        Log().info("Seleccionando monto para pago")
        monto_pago = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                            "new UiSelector().text(\"225,40\")")))
        monto_pago.click()

        # Navegar por opciones de pago
        Log().info("Navegando por opciones de pago")
        btn_nav_pago = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                              "new UiSelector().className("
                                                              "\"android.widget.ImageView\").instance(3)")))
        btn_nav_pago.click()

        # Verificar monto total
        monto_total = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                             "new UiSelector().text(\"R$ 225,40\")")))
        monto_total.click()
        FuncionesBrasil.captura_pantalla(driver, "TC44-Monto Seleccionado", request)

        # Navegar por más opciones
        Log().info("Navegando por opciones adicionales")
        btn_nav_opciones = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                  "new UiSelector().className("
                                                                  "\"android.widget.ImageView\").instance(4)")))
        btn_nav_opciones.click()

        btn_nav_opciones2 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                   "new UiSelector().className("
                                                                   "\"android.widget.ImageView\").instance(5)")))
        btn_nav_opciones2.click()

        # Continuar con pagamento
        Log().info("Continuando con pagamento")
        btn_continuar = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                               "new UiSelector().text(\"Continuar com pagamento\")")))
        btn_continuar.click()

        # Verificar monto total final
        Log().info("Verificando monto total final")
        monto_total_final = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                   "new UiSelector().text(\"R$ 599,15\")")))
        monto_total_final.click()
        FuncionesBrasil.captura_pantalla(driver, "TC44-Monto Total", request)

        # Seleccionar metodo de pago
        Log().info("Seleccionando método de pago")
        campo_metodo = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                              "new UiSelector().className("
                                                              "\"android.widget.TextView\").instance(25)")))
        campo_metodo.click()

        credito_3 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                           "new UiSelector().text(\"CREDITO - 3\")")))
        credito_3.click()

        # Llenar campos de comprovante
        Log().info("Llenando campos de comprovante")
        campo_adesivo = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID,
                                                               "Adesivo no comprovante (escrito SN)")))
        campo_adesivo.click()
        campo_adesivo.send_keys("test")
        press_back()

        campo_stone = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID,
                                                             "Últimos 6 dígitos do STONE ID")))
        campo_stone.click()
        campo_stone.send_keys("1234")
        press_back()
        FuncionesBrasil.captura_pantalla(driver, "TC44-Datos Comprovante", request)

        # Acceder a pagamento de dívida
        Log().info("Accediendo a pagamento de dívida")
        pagamento_divida = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                  "new UiSelector().text(\"Pagamento de dívida\")")))
        pagamento_divida.click()

        # Guardar pago
        Log().info("Guardando pago")
        btn_salvar = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        btn_salvar.click()

        # Manejar mensaje de confirmación
        Log().info("Manejando mensaje de confirmación")
        mensaje_confirmacion = wait.until(EC.element_to_be_clickable((AppiumBy.ID, "android:id/message")))
        mensaje_confirmacion.click()

        btn_ok = wait.until(EC.element_to_be_clickable((AppiumBy.ID, boton)))
        btn_ok.click()
        FuncionesBrasil.captura_pantalla(driver, "TC44-Pago Confirmado", request)

        # Verificar información financiera actualizada
        Log().info("Verificando información financiera actualizada")
        btn_nav_verificacion = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, image_view_1)))
        btn_nav_verificacion.click()

        btn_info_verificacion = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, info_financiera)))
        btn_info_verificacion.click()

        # Verificar información financiera nuevamente
        btn_info_verificacion2 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, info_financiera)))
        btn_info_verificacion2.click()
        FuncionesBrasil.captura_pantalla(driver, "TC44-Info Verificada", request)

        # Regresar final
        Log().info("Completando TC44 Pagos de Deudas")
        btn_back_final = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, image_view_0)))
        btn_back_final.click()
        FuncionesBrasil.captura_pantalla(driver, "TC44-Completado", request)

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
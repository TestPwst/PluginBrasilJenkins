# ********************************
# TC47 - RPA - Información Financiera
# ********************************

from FuncionesGralBrasil import *
from Configuracion import *

# Variables Globales
salvar = "new UiSelector().text(\"Salvar\")"
boton = "android:id/button2"
aceitar = "new UiSelector().text(\"Aceitar\")"
antonio_cliente = "new UiSelector().text(\"ANTONIO JOSE GOMES MARINHO\")"
info_financiera = "new UiSelector().text(\"Informação financeira\")"
continuar_pagamento = "new UiSelector().text(\"Continuar com pagamento\")"
image_view_0 = "new UiSelector().className(\"android.widget.ImageView\").instance(0)"
image_view_1 = "new UiSelector().className(\"android.widget.ImageView\").instance(1)"


def ingreso_app(self, request):
    try:
        Log().info("Iniciando ingreso a la aplicación")
        FuncionesBrasil.ingreso_app(self)
        FuncionesBrasil.captura_pantalla(driver, "TC47-Ingreso App", request)
    except Exception as e:  # pragma: no cover
        Log().error(f"No se logró ingresar a la aplicación, validar el error: {e}")
        raise


def configuracion_inicial(self, request):
    try:
        Log().info("Iniciando carga de usuario")
        FuncionesBrasil.cargar(self)
        FuncionesBrasil.captura_pantalla(driver, "TC47-Carga Usuario", request)
    except Exception as e:  # pragma: no cover
        Log().error(f"No se logró cargar usuario, validar el error: {e}")
        raise

    try:
        Log().info("Iniciando registro de punto")
        FuncionesBrasil.registro_punto(self)
        FuncionesBrasil.captura_pantalla(driver, "TC47-Registro Punto", request)
    except Exception as e:  # pragma: no cover
        Log().error(f"No se logró registrar punto, validar el error: {e}")
        raise


def pegar_funcion(request):
    try:
        # ==================================================
        #      PEGAR CÓDIGO DE APPIUM RECORDER ABAJO
        # ==================================================

        # Seleccionar cliente ANTONIO JOSE GOMES MARINHO
        Log().info("Seleccionando cliente ANTONIO JOSE GOMES MARINHO")
        cliente_antonio = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, antonio_cliente)))
        cliente_antonio.click()
        cliente_antonio.click()
        FuncionesBrasil.captura_pantalla(driver, "TC47-Cliente Seleccionado", request)

        # Acceder a datos del cliente
        Log().info("Accediendo a datos del cliente")
        btn_dados_cliente = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                   "new UiSelector().text(\"Dados do cliente\")")))
        btn_dados_cliente.click()

        # Navegar a información financiera
        Log().info("Navegando a información financiera")
        btn_nav_info = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, image_view_1)))
        btn_nav_info.click()

        # Acceder a información financiera
        Log().info("Accediendo a información financiera")
        btn_info_financiera = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, info_financiera)))
        btn_info_financiera.click()
        FuncionesBrasil.captura_pantalla(driver, "TC47-Info Financiera", request)

        # Seleccionar cuenta específica
        Log().info("Seleccionando cuenta específica")
        cuenta_especifica = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                   "new UiSelector().text(\"4061583628 - 3\")")))
        cuenta_especifica.click()

        # Regresar
        Log().info("Regresando al menú anterior")
        btn_regresar = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, image_view_0)))
        btn_regresar.click()

        # Iniciar visita
        Log().info("Iniciando visita")
        btn_iniciar_visita = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                    "new UiSelector().text(\"Iniciar visita\")")))
        btn_iniciar_visita.click()

        # Aceptar confirmación
        Log().info("Aceptando confirmación")
        btn_aceitar = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, aceitar)))
        btn_aceitar.click()
        FuncionesBrasil.captura_pantalla(driver, "TC47-Visita Iniciada", request)

        # Navegar a información financiera nuevamente
        Log().info("Segunda navegación a información financiera")
        btn_nav_info2 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, image_view_1)))
        btn_nav_info2.click()

        # Acceder a información financiera
        Log().info("Segunda información financiera accedida")
        btn_info_financiera2 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, info_financiera)))
        btn_info_financiera2.click()

        # Navegar hacia atrás
        Log().info("Navegando hacia atrás")
        btn_back = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                          "new UiSelector().className("
                                                          "\"android.widget.ImageView\").instance(3)")))
        btn_back.click()

        # Continuar con pagamento
        Log().info("Continuando con pagamento")
        btn_continuar_pago = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, continuar_pagamento)))
        btn_continuar_pago.click()
        FuncionesBrasil.captura_pantalla(driver, "TC46-Continuar Pagamento", request)

        # Seleccionar metodo de pago
        Log().info("Seleccionando método de pago")
        campo_metodo = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                              "new UiSelector().className("
                                                              "\"android.widget.TextView\").instance(25)")))
        campo_metodo.click()

        # Seleccionar CREDITO - 3
        Log().info("Seleccionando CREDITO - 3")
        credito_3 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                           "new UiSelector().text(\"CREDITO - 3\")")))
        credito_3.click()

        # Acceder a número de maquininha
        Log().info("Accediendo a número de maquininha")
        numero_maquininha = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                   "new UiSelector().text(\"Número da Maquininha\")")))
        numero_maquininha.click()

        # Llenar campo adesivo
        Log().info("Llenando campo adesivo")
        campo_adesivo = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID,
                                                               "Adesivo no comprovante (escrito SN)")))
        campo_adesivo.click()
        campo_adesivo.send_keys("TEST RPA")
        driver.execute_script('mobile:pressKey', {"keycode": 4})

        # Acceder a autenticación
        Log().info("Accediendo a autenticación")
        autenticacion = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                               "new UiSelector().text(\"Autenticação\")")))
        autenticacion.click()

        # Llenar campo Stone ID
        Log().info("Llenando campo Stone ID")
        campo_stone = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID,
                                                             "Últimos 6 dígitos do STONE ID")))
        campo_stone.click()
        campo_stone.send_keys("7777777")
        driver.execute_script('mobile:pressKey', {"keycode": 4})
        FuncionesBrasil.captura_pantalla(driver, "TC47-Datos Maquininha", request)

        # Guardar información
        Log().info("Guardando información")
        btn_salvar = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        btn_salvar.click()

        # Manejar mensaje de confirmación
        Log().info("Manejando mensaje de confirmación")
        mensaje_confirmacion = wait.until(EC.element_to_be_clickable((AppiumBy.ID, "android:id/message")))
        mensaje_confirmacion.click()
        btn_aceptar_dialogo = wait.until(EC.element_to_be_clickable((AppiumBy.ID, boton)))
        btn_aceptar_dialogo.click()

        # Navegar hacia atrás
        Log().info("Segunda navegación hacia atrás")
        btn_back2 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, image_view_1)))
        btn_back2.click()

        # Acceder nuevamente a información financiera
        Log().info("Tercera información financiera accedida")
        btn_info_financiera3 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, info_financiera)))
        btn_info_financiera3.click()

        # Continuar con pagamento
        Log().info("Segunda continuación con pagamento")
        btn_continuar_pago2 = wait.until(EC.element_to_be_clickable((
            AppiumBy.ANDROID_UIAUTOMATOR, continuar_pagamento)))
        btn_continuar_pago2.click()

        # Aceptar segundo diálogo
        Log().info("Aceptando segundo diálogo")
        btn_aceptar_dialogo2 = wait.until(EC.element_to_be_clickable((AppiumBy.ID, boton)))
        btn_aceptar_dialogo2.click()
        FuncionesBrasil.captura_pantalla(driver, "TC47-Pagamento Procesado", request)

        # Regresar al menú principal
        Log().info("Regresando al menú principal")
        btn_regresar_menu = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, image_view_0)))
        btn_regresar_menu.click()

        # Finalizar sin venta
        Log().info("Finalizando sin venta")
        btn_finalizar_sin_venta = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                         "new UiSelector().text(\"Finalizar sem "
                                                                         "venda\")")))
        btn_finalizar_sin_venta.click()

        # Seleccionar motivo: Falta de tiempo
        Log().info("Seleccionando motivo 'Falta de tempo'")
        motivo_falta_tiempo = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                     "new UiSelector().text(\"Falta de tempo\")")))
        motivo_falta_tiempo.click()

        # Guardar motivo
        Log().info("Guardando motivo")
        btn_salvar_motivo = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        btn_salvar_motivo.click()
        FuncionesBrasil.captura_pantalla(driver, "TC47-Motivo Sin Venta", request)

        # Confirmar finalización
        Log().info("Confirmando finalización")
        confirmacion_final = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                    "new UiSelector().text(\"Tem certeza que deseja "
                                                                    "finalizar a visita sem venda?\")")))
        confirmacion_final.click()

        # Aceptar finalización
        Log().info("Aceptando finalización")
        btn_aceitar_final = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, aceitar)))
        btn_aceitar_final.click()

        # Verificar contador sin venta
        Log().info("Verificando contador sin venta")
        contador_sin_venta = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                    "new UiSelector().text(\"Sem venda\n1\")")))
        contador_sin_venta.click()
        FuncionesBrasil.captura_pantalla(driver, "TC47-Sin Venta Verificada", request)

        # Verificar cliente en lista
        Log().info("Verificando cliente en lista")
        cliente_verificacion = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, antonio_cliente)))
        cliente_verificacion.click()

        # Verificar contador de visitas
        Log().info("Verificando contador de visitas - TC046 completado exitosamente")
        contador_visitas = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                  "new UiSelector().text(\"Visitas\n1/8\")")))
        contador_visitas.click()
        FuncionesBrasil.captura_pantalla(driver, "TC47-Completado", request)

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
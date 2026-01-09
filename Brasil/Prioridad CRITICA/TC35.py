# ********************************
# TC35 - Venta con Límite de Crédito - Proceso Completo de Venda
# ********************************

from FuncionesGralBrasil import *
from Configuracion import *

# Variables Globales
salvar = "new UiSelector().text(\"Salvar\")"
aceitar = "new UiSelector().text(\"Aceitar\")"
sim = "new UiSelector().text(\"Sim\")"
finalizar = "new UiSelector().text(\"Finalizar\")"
antonio_cliente = "new UiSelector().text(\"ANTONIO JOSE GOMES MARINHO\")"
dados_cliente = "new UiSelector().text(\"Dados do cliente\")"
iniciar_visita = "new UiSelector().text(\"Iniciar visita\")"
realizar_venda = "new UiSelector().text(\"Realizar venda\")"
chesterfield_blue = "new UiSelector().text(\"CHESTERFIELD BLUE BOX\")"
chesterfield_original = "new UiSelector().text(\"CHESTERFIELD ORIGINAL BOX\")"
chf_terras_blue = "new UiSelector().text(\"CHF Terras Blue\")"
sinergia = "new UiSelector().text(\"Sinergia\")"
cricket_isqueiro = "new UiSelector().text(\"CRICKET ISQUEIRO MINI BANDEJA\")"
boleto = "new UiSelector().text(\"Boleto\")"
itens_pedido = "new UiSelector().text(\"Itens do pedido\")"
info_financeira = "new UiSelector().text(\"Informação financeira\")"
finalizar_pedido = "new UiSelector().text(\"Finalizar pedido\")"
finalizadas = "new UiSelector().text(\"Finalizadas\n1\")"
visitas = "new UiSelector().text(\"Visitas\n1/8\")"
numero_3 = "new UiSelector().text(\"3\")"
android_button2 = "android:id/button2"
android_message = "android:id/message"
contextmenu_item = "uy.com.assist.eaf:id/contextmenu_item_text"
press_back_key = {'keycode': 4}


def press_back():
    """Función auxiliar para presionar tecla atrás"""
    driver.execute_script('mobile:pressKey', press_back_key)


def ingreso_app(self, request):
    try:
        Log().info("Iniciando ingreso a la aplicación")
        FuncionesBrasil.ingreso_app(self)
        FuncionesBrasil.captura_pantalla(driver, "TC35-Ingreso App", request)
    except Exception as e:  # pragma: no cover
        Log().error(f"No se logró ingresar a la aplicación, validar el error: {e}")
        raise


def configuracion_inicial(self, request):
    try:
        Log().info("Iniciando carga de usuario")
        FuncionesBrasil.cargar(self)
        FuncionesBrasil.captura_pantalla(driver, "TC35-Carga Usuario", request)
    except Exception as e:  # pragma: no cover
        Log().error(f"No se logró cargar usuario, validar el error: {e}")
        raise

    try:
        Log().info("Iniciando registro de punto")
        FuncionesBrasil.registro_punto(self)
        FuncionesBrasil.captura_pantalla(driver, "TC35-Registro Punto", request)
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
        Log().info("Cliente ANTONIO JOSE GOMES MARINHO seleccionado")
        FuncionesBrasil.captura_pantalla(driver, "TC35-Cliente Seleccionado", request)

        # Acceder a dados do cliente
        Log().info("Accediendo a dados do cliente")
        btn_dados_cliente = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, dados_cliente)))
        btn_dados_cliente.click()

        # Iniciar visita
        Log().info("Iniciando visita")
        btn_iniciar_visita = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, iniciar_visita)))
        btn_iniciar_visita.click()

        # Aceitar inicio de visita
        Log().info("Confirmando inicio de visita")
        btn_aceitar = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, aceitar)))
        btn_aceitar.click()
        FuncionesBrasil.captura_pantalla(driver, "TC35-Visita Iniciada", request)

        # Realizar venda
        Log().info("Iniciando proceso de venda")
        btn_realizar_venda = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, realizar_venda)))
        btn_realizar_venda.click()

        # Confirmar diálogo de venda
        btn_dialogo_venda = wait.until(EC.element_to_be_clickable((AppiumBy.ID, android_button2)))
        btn_dialogo_venda.click()
        Log().info("Diálogo de venda confirmado")

        # Seleccionar productos y agregar cantidades
        Log().info("Seleccionando productos y agregando cantidades")
        
        # CHESTERFIELD BLUE BOX - 10 unidades
        producto_blue = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, chesterfield_blue)))
        producto_blue.click()
        
        btn_agregar_blue = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                  "new UiSelector().className("
                                                                  "\"android.widget.ImageView\").instance(4)")))
        for i in range(10):
            btn_agregar_blue.click()
        Log().info("10 unidades de CHESTERFIELD BLUE BOX agregadas")

        # CHESTERFIELD ORIGINAL BOX - 10 unidades
        producto_original = wait.until(EC.element_to_be_clickable((
            AppiumBy.ANDROID_UIAUTOMATOR, chesterfield_original)))
        producto_original.click()
        
        btn_agregar_original = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                      "new UiSelector().className("
                                                                      "\"android.widget.ImageView\").instance(15)")))
        for i in range(10):
            btn_agregar_original.click()
        Log().info("10 unidades de CHESTERFIELD ORIGINAL BOX agregadas")

        # CHF Terras Blue - 10 unidades
        producto_terras = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, chf_terras_blue)))
        producto_terras.click()
        
        btn_agregar_terras = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                    "new UiSelector().className("
                                                                    "\"android.widget.ImageView\").instance(26)")))
        for i in range(10):
            btn_agregar_terras.click()
        Log().info("10 unidades de CHF Terras Blue agregadas")

        # Sinergia
        producto_sinergia = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, sinergia)))
        producto_sinergia.click()
        Log().info("Artículo Sinergia seleccionado")

        # CRICKET ISQUEIRO MINI BANDEJA - 3 unidades
        producto_cricket = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, cricket_isqueiro)))
        producto_cricket.click()
        
        btn_agregar_cricket = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                     "new UiSelector().className("
                                                                     "\"android.widget.ImageView\").instance(4)")))
        for i in range(3):
            btn_agregar_cricket.click()
        Log().info("3 unidades de CRICKET ISQUEIRO MINI BANDEJA agregadas")
        FuncionesBrasil.captura_pantalla(driver, "TC35-Productos Seleccionados", request)

        # Finalizar selección de artículos
        Log().info("Finalizando selección de artículos")
        btn_finalizar = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, finalizar)))
        btn_finalizar.click()

        # Continuar con el proceso
        btn_continuar = wait.until(EC.element_to_be_clickable((AppiumBy.CLASS_NAME, "android.widget.ImageView")))
        btn_continuar.click()
        Log().info("Continuando con el proceso de venda")

        # Manejar mensaje de límite de crédito
        Log().info("Manejando mensaje de límite de crédito")
        mensaje_limite = wait.until(EC.element_to_be_clickable((AppiumBy.ID, android_message)))
        mensaje_limite.click()
        
        btn_confirmar_limite = wait.until(EC.element_to_be_clickable((AppiumBy.ID, android_button2)))
        btn_confirmar_limite.click()
        Log().info("Mensaje de límite de crédito procesado")

        # Configurar metodo de pago
        Log().info("Configurando método de pago")
        metodo_boleto = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, boleto)))
        metodo_boleto.click()

        btn_salvar_pago = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        btn_salvar_pago.click()
        Log().info("Método de pago Boleto configurado")

        # Confirmar condiciones
        Log().info("Confirmando condiciones de venta")
        btn_sim1 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, sim)))
        btn_sim1.click()

        btn_sim2 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, sim)))
        btn_sim2.click()

        btn_salvar_condiciones = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        btn_salvar_condiciones.click()
        Log().info("Condiciones de venta confirmadas")
        FuncionesBrasil.captura_pantalla(driver, "TC35-Condiciones Configuradas", request)

        # Configurar parcelas
        Log().info("Configurando parcelas de pago")
        campo_parcela1 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                "new UiSelector().className("
                                                                "\"android.widget.TextView\").instance(21)")))
        campo_parcela1.click()

        valor_3_1 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, numero_3)))
        valor_3_1.click()

        campo_parcela2 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                "new UiSelector().className("
                                                                "\"android.widget.TextView\").instance(22)")))
        campo_parcela2.click()

        valor_3_2 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, numero_3)))
        valor_3_2.click()

        # Configurar tipo de parcelado
        campo_tipo_parcelado = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                      "new UiSelector().className("
                                                                      "\"android.widget.TextView\").instance(35)")))
        campo_tipo_parcelado.click()

        opcion_contextual = wait.until(EC.element_to_be_clickable((AppiumBy.ID, contextmenu_item)))
        opcion_contextual.click()
        Log().info("Parcelas configuradas exitosamente")

        # Ingresar observación sobre límite de crédito
        Log().info("Ingresando observación sobre límite de crédito")
        campo_observacion = wait.until(EC.element_to_be_clickable((AppiumBy.CLASS_NAME, "android.widget.EditText")))
        campo_observacion.click()
        campo_observacion.send_keys("Limite de credito")
        press_back()
        FuncionesBrasil.captura_pantalla(driver, "TC35-Observacion Ingresada", request)

        # Revisar itens do pedido
        Log().info("Revisando ítems del pedido")
        btn_itens_pedido = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, itens_pedido)))
        btn_itens_pedido.click()

        btn_continuar_itens = wait.until(EC.element_to_be_clickable((AppiumBy.CLASS_NAME, "android.widget.ImageView")))
        btn_continuar_itens.click()
        Log().info("Ítems del pedido revisados")

        # Acceder a informação financeira
        Log().info("Configurando información financiera")
        btn_info_financeira = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, info_financeira)))
        btn_info_financeira.click()

        btn_config_financeira = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                       "new UiSelector().className("
                                                                       "\"android.widget.ImageView\").instance(0)")))
        btn_config_financeira.click()

        btn_salvar_financeira = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        btn_salvar_financeira.click()
        Log().info("Información financiera configurada")
        FuncionesBrasil.captura_pantalla(driver, "TC35-Info Financiera", request)

        # Finalizar pedido
        Log().info("Finalizando pedido")
        btn_finalizar_pedido = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, finalizar_pedido)))
        btn_finalizar_pedido.click()

        btn_confirmar_finalizacion = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        btn_confirmar_finalizacion.click()
        Log().info("Pedido finalizado exitosamente")

        # Verificar en finalizadas
        Log().info("Verificando pedido en finalizadas")
        contador_finalizadas = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, finalizadas)))
        contador_finalizadas.click()

        cliente_finalizadas = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, antonio_cliente)))
        cliente_finalizadas.click()
        Log().info("Cliente confirmado en finalizadas")

        # Verificar estado de visitas
        estado_visitas = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, visitas)))
        estado_visitas.click()
        Log().info("TC35 - Venta con Límite de Crédito completado exitosamente")
        FuncionesBrasil.captura_pantalla(driver, "TC35-Completado", request)

        # ==================================================
        #                 FIN DEL PEGADO
        # ==================================================
    except Exception as e:  # pragma: no cover
        Log().error(f"No se logró completar la automatización TC35, validar el error: {e}")
        raise


class Test:
    def test_001(self, request):
        ingreso_app(self, request)

    def test_002(self, request):
        configuracion_inicial(self, request)

    def test_003(self, request):
        pegar_funcion(request)
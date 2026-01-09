# ****************************************************************
# TC52 - Stock - Ventas pendientes - Pendientes
# ****************************************************************

from FuncionesGralBrasil import *
from Configuracion import *

# Variables Globales
salvar = "new UiSelector().text(\"Salvar\")"
imagen = "android.widget.ImageView"
finalizar = "new UiSelector().text(\"Finalizar\")"
itens_pedido = "new UiSelector().text(\"Itens do pedido\")"
salvar_sem_finalizar = "new UiSelector().text(\"Salvar sem finalizar\")"
numero_3 = "new UiSelector().text(\"3\")"
aurenio_cliente = "new UiSelector().text(\"AURENIO DE CARVALHO ANDRADE\")"
text_view_35 = "new UiSelector().className(\"android.widget.TextView\").instance(35)"
contextmenu_item = "uy.com.assist.eaf:id/contextmenu_item_text"
press_back_key = {'keycode': 4}
test_stock_text = "Test Stock PENDIENTE"


def press_back():
    driver.execute_script('mobile:pressKey', press_back_key)


def ingreso_app(self, request):
    try:
        Log().info("Iniciando ingreso a la aplicación")
        FuncionesBrasil.ingreso_app(self)
        FuncionesBrasil.captura_pantalla(driver, "TC52-Ingreso App", request)
    except Exception as e:  # pragma: no cover
        Log().error(f"No se logró ingresar a la aplicación, validar el error: {e}")
        raise


def configuracion_inicial(self, request):
    try:
        Log().info("Iniciando carga de usuario")
        FuncionesBrasil.cargar(self)
        FuncionesBrasil.captura_pantalla(driver, "TC52-Carga Usuario", request)
    except Exception as e:  # pragma: no cover
        Log().error(f"No se logró cargar usuario, validar el error: {e}")
        raise

    try:
        Log().info("Iniciando registro de punto")
        FuncionesBrasil.registro_punto(self)
        FuncionesBrasil.captura_pantalla(driver, "TC52-Registro Punto", request)
    except Exception as e:  # pragma: no cover
        Log().error(f"No se logró registrar punto, validar el error: {e}")
        raise


def pegar_funcion(request):
    try:
        # ==================================================
        #      PEGAR CÓDIGO DE APPIUM RECORDER ABAJO
        # ==================================================
        # Seleccionar cliente AURENIO DE CARVALHO ANDRADE
        cliente = (AppiumBy.ANDROID_UIAUTOMATOR, aurenio_cliente)

        Log().info("Buscando cliente AURENIO DE CARVALHO ANDRADE")
        selector = driver.find_elements(*cliente)

        if selector:
            Log().info("Cliente AURENIO DE CARVALHO ANDRADE encontrado")
            cliente_encontrado = wait.until(EC.element_to_be_clickable(cliente))
            cliente_encontrado.click()
            cliente_encontrado.click()
            Log().info("Cliente encontrado y seleccionado directamente")
            FuncionesBrasil.captura_pantalla(driver, "TC52-Cliente Seleccionado", request)
        else:
            Log().info("Cliente no visible, realizando scroll")
            scroll_script = (
                'new UiScrollable(new UiSelector().scrollable(true))'
                '.scrollIntoView(new UiSelector().text("AURENIO DE CARVALHO ANDRADE"))')

            # Ejecutar scroll
            driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, scroll_script)

            # Esperar a que sea clickable después del scroll
            cliente_encontrar = wait.until(EC.element_to_be_clickable(cliente))
            cliente_encontrar.click()
            cliente_encontrar.click()
            Log().info("Cliente encontrado después de scroll y seleccionado")
            FuncionesBrasil.captura_pantalla(driver, "TC52-Cliente Scroll", request)

        # Acceder a datos del cliente
        Log().info("Accediendo a datos del cliente")
        btn_dados_cliente = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                   "new UiSelector().text(\"Dados do cliente\")")))
        btn_dados_cliente.click()

        # Iniciar visita
        Log().info("Iniciando visita")
        btn_iniciar_visita = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                    "new UiSelector().text(\"Iniciar visita\")")))
        btn_iniciar_visita.click()

        # Aceptar confirmación
        Log().info("Aceptando confirmación")
        btn_aceitar = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                             "new UiSelector().text(\"Aceitar\")")))
        btn_aceitar.click()
        FuncionesBrasil.captura_pantalla(driver, "TC52-Visita Iniciada", request)

        # Realizar venta
        Log().info("Iniciando proceso de venta")
        btn_realizar_venda = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                    "new UiSelector().text(\"Realizar venda\")")))
        btn_realizar_venda.click()

        # Seleccionar producto CHESTERFIELD BLUE BOX
        Log().info("Seleccionando producto CHESTERFIELD BLUE BOX")
        producto_blue = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                               "new UiSelector().text(\"CHESTERFIELD BLUE BOX\")")))
        producto_blue.click()
        FuncionesBrasil.captura_pantalla(driver, "TC52-Producto Seleccionado", request)

        # Agregar cantidades múltiples
        Log().info("Agregando cantidades múltiples")
        for i, instance in enumerate([4, 10, 15, 21, 26, 32], 1):
            btn_agregar = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                 f"new UiSelector().className("
                                                                 f"\"android.widget.ImageView\").instance("
                                                                 f"{instance})")))
            btn_agregar.click()

        # Finalizar pedido
        Log().info("Finalizando pedido")
        btn_finalizar = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, finalizar)))
        btn_finalizar.click()

        # Seleccionar imagen para metodo de pago
        Log().info("Seleccionando método de pago")
        imagen_pago = wait.until(EC.element_to_be_clickable((AppiumBy.CLASS_NAME, imagen)))
        imagen_pago.click()

        # Seleccionar metodo boleto
        metodo_boleto = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                               "new UiSelector().text(\"Boleto\")")))
        metodo_boleto.click()

        # Guardar metodo de pago
        btn_salvar_pago = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        btn_salvar_pago.click()

        # Guardar configuración
        Log().info("Guardando configuración")
        btn_salvar_config = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        btn_salvar_config.click()
        FuncionesBrasil.captura_pantalla(driver, "TC52-Metodo Pago", request)

        # Configurar parcelas - primera opción
        Log().info("Configurando parcelas")
        campo_parcela1 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                "new UiSelector().className("
                                                                "\"android.widget.TextView\").instance(21)")))
        campo_parcela1.click()

        # Seleccionar valor 3
        valor_3 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, numero_3)))
        valor_3.click()

        # Configurar parcelas - segunda opción
        campo_parcela2 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                "new UiSelector().className("
                                                                "\"android.widget.TextView\").instance(22)")))
        campo_parcela2.click()

        # Seleccionar valor 4
        valor_4 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                         "new UiSelector().text(\"4\")")))
        valor_4.click()

        # Configurar tipo de parcelado - múltiples clics
        Log().info("Configurando tipo de parcelado")
        for i in range(3):
            campo_tipo_parcelado = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                          text_view_35)))
            campo_tipo_parcelado.click()

        # Seleccionar valores específicos
        valor_4_instance = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                  "new UiSelector().text(\"4\").instance(0)")))
        valor_4_instance.click()

        valor_3_final = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, numero_3)))
        valor_3_final.click()

        # Configurar tipo de parcelado final
        campo_tipo_final = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                  text_view_35)))
        campo_tipo_final.click()

        # Seleccionar opción del menú contextual
        Log().info("Configurando opciones adicionales")
        opcion_menu = wait.until(EC.element_to_be_clickable((AppiumBy.ID, contextmenu_item)))
        opcion_menu.click()

        # Llenar campo de texto
        campo_texto = wait.until(EC.element_to_be_clickable((AppiumBy.CLASS_NAME, "android.widget.EditText")))
        campo_texto.click()
        campo_texto.send_keys(test_stock_text)
        press_back()
        FuncionesBrasil.captura_pantalla(driver, "TC52-Configuracion Parcelas", request)

        # Acceder a itens do pedido
        Log().info("Accediendo a ítems del pedido")
        itens_pedido_btn = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, itens_pedido)))
        itens_pedido_btn.click()

        # Seleccionar imagen
        imagen_item = wait.until(EC.element_to_be_clickable((AppiumBy.CLASS_NAME, imagen)))
        imagen_item.click()

        # Guardar cambios
        btn_salvar_cambios = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        btn_salvar_cambios.click()

        # Salvar sem finalizar
        Log().info("Guardando sin finalizar")
        btn_salvar_sem_finalizar = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                          salvar_sem_finalizar)))
        btn_salvar_sem_finalizar.click()

        # Guardar acción
        btn_salvar_acao = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        btn_salvar_acao.click()
        FuncionesBrasil.captura_pantalla(driver, "TC52-Pedido Pendiente", request)

        # Verificar contador pendiente
        Log().info("Verificando contador pendientes")
        contador_pendientes = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                     "new UiSelector().text(\"Pendentes\n1\")")))
        contador_pendientes.click()

        # Editar pedido pendiente
        Log().info("Editando pedido pendiente")
        btn_editar = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                            "new UiSelector().text(\"Editar\")")))
        btn_editar.click()

        # Agregar cantidad adicional
        btn_agregar_adicional = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                       "new UiSelector().className("
                                                                       "\"android.widget.ImageView\").instance(15)")))
        btn_agregar_adicional.click()

        # Finalizar pedido editado
        Log().info("Finalizando pedido editado")
        btn_finalizar_editado = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, finalizar)))
        btn_finalizar_editado.click()
        FuncionesBrasil.captura_pantalla(driver, "TC52-Pedido Editado", request)

        # Seleccionar imagen para metodo de pago final
        Log().info("Configurando método de pago final")
        imagen_pago_final = wait.until(EC.element_to_be_clickable((AppiumBy.CLASS_NAME, imagen)))
        imagen_pago_final.click()

        # Seleccionar Cartão de crédito
        metodo_cartao = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                               "new UiSelector().text(\"Cartão de crédito\")")))
        metodo_cartao.click()

        # Guardar metodo final
        btn_salvar_final = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        btn_salvar_final.click()

        # Acceder a comprovante de pagamento
        Log().info("Configurando comprovante de pagamento")
        comprovante_pago = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                  "new UiSelector().text("
                                                                  "\"Comprovante de pagamento\")")))
        comprovante_pago.click()

        # Seleccionar campo específico
        campo_especifico = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                  "new UiSelector().className("
                                                                  "\"android.widget.TextView\").instance(20)")))
        campo_especifico.click()

        # Seleccionar opción del menú contextual final
        opcion_menu_final = wait.until(EC.element_to_be_clickable((AppiumBy.ID, contextmenu_item)))
        opcion_menu_final.click()

        # Llenar campo adesivo
        Log().info("Llenando campos de comprovante")
        campo_adesivo = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID,
                                                               "Adesivo no comprovante (escrito SN)")))
        campo_adesivo.click()
        campo_adesivo.send_keys(test_stock_text)
        press_back()

        # Llenar campo Stone ID
        campo_stone = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID,
                                                             "Últimos 6 dígitos do STONE ID")))
        campo_stone.click()
        campo_stone.send_keys("PENDIENTE editado")
        press_back()
        FuncionesBrasil.captura_pantalla(driver, "TC52-Comprovante Pagamento", request)

        # Acceder a itens do pedido final
        Log().info("Finalizando configuración")
        itens_pedido_final = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                    itens_pedido)))
        itens_pedido_final.click()

        # Seleccionar imagen final
        imagen_final = wait.until(EC.element_to_be_clickable((AppiumBy.CLASS_NAME, imagen)))
        imagen_final.click()

        # Guardar cambios finales
        btn_salvar_final_cambios = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                          salvar)))
        btn_salvar_final_cambios.click()

        # Salvar sem finalizar final
        btn_salvar_sem_finalizar_final = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                                salvar_sem_finalizar)))
        btn_salvar_sem_finalizar_final.click()

        # Guardar acción final
        Log().info("Guardando configuración final")
        btn_salvar_acao_final = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                       salvar)))
        btn_salvar_acao_final.click()
        FuncionesBrasil.captura_pantalla(driver, "TC52-Completado", request)

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
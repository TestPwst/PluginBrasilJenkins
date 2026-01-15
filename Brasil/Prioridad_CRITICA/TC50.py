# ****************************************************************
# TC50 - Stock - Ventas Pendientes - Finalizado
# ****************************************************************


from FuncionesGralBrasil import *
from Configuracion import *

# Variables Globales
salvar = "new UiSelector().text(\"Salvar\")"
aceitar = "new UiSelector().text(\"Aceitar\")"
finalizar = "new UiSelector().text(\"Finalizar\")"
imagen = "android.widget.ImageView"
itens_pedido = "new UiSelector().text(\"Itens do pedido\")"
cartao_credito = "new UiSelector().text(\"Cartão de crédito\")"
text_view_20 = "new UiSelector().className(\"android.widget.TextView\").instance(20)"
contextmenu_item = "uy.com.assist.eaf:id/contextmenu_item_text"
numero_3 = "new UiSelector().text(\"3\")"
text_view_35 = "new UiSelector().className(\"android.widget.TextView\").instance(35)"
aurenio_cliente = "new UiSelector().text(\"AURENIO DE CARVALHO ANDRADE\").instance(0)"
press_back_key = {"keycode": 4}
test_stock_text = "Test Stock PENDIENTE"


def press_back():
    driver.execute_script('mobile:pressKey', press_back_key)


def ingreso_app(self, request):
    try:
        Log().info("Iniciando ingreso a la aplicación")
        FuncionesBrasil.ingreso_app(self)
        FuncionesBrasil.captura_pantalla(driver, "TC50-Ingreso App", request)
    except Exception as e:  # pragma: no cover
        Log().error(f"No se logró ingresar a la aplicación, validar el error: {e}")
        raise


def configuracion_inicial(self, request):
    try:
        Log().info("Iniciando carga de usuario")
        FuncionesBrasil.cargar(self)
        FuncionesBrasil.captura_pantalla(driver, "TC50-Carga Usuario", request)
    except Exception as e:  # pragma: no cover
        Log().error(f"No se logró cargar usuario, validar el error: {e}")
        raise

    try:
        Log().info("Iniciando registro de punto")
        FuncionesBrasil.registro_punto(self)
        FuncionesBrasil.captura_pantalla(driver, "TC50-Registro Punto", request)
    except Exception as e:  # pragma: no cover
        Log().error(f"No se logró registrar punto, validar el error: {e}")
        raise


def pegar_funcion(request):
    try:
        # ==================================================
        #      PEGAR CÓDIGO DE APPIUM RECORDER ABAJO
        # ==================================================
        Log().info("Realizando scroll para encontrar cliente")
        el17 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                   value='new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new '
                                         'UiSelector().text("AURENIO DE CARVALHO ANDRADE"))')
        el17.click()
        
        # Seleccionar cliente AURENIO DE CARVALHO ANDRADE
        Log().info("Seleccionando cliente AURENIO DE CARVALHO ANDRADE")
        cliente_aurenio = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, aurenio_cliente)))
        cliente_aurenio.click()
        cliente_aurenio.click()
        FuncionesBrasil.captura_pantalla(driver, "TC50-Cliente Seleccionado", request)

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
        btn_aceitar = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, aceitar)))
        btn_aceitar.click()
        FuncionesBrasil.captura_pantalla(driver, "TC50-Visita Iniciada", request)

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
        FuncionesBrasil.captura_pantalla(driver, "TC50-Producto Seleccionado", request)

        # Agregar cantidades múltiples
        Log().info("Agregando cantidades múltiples")
        for i, instance in enumerate([4, 10, 15, 21, 26, 32], 1):
            btn_agregar = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                 f"new UiSelector().className("
                                                                 f"\"android.widget.ImageView\").instance("
                                                                 f"{instance})")))
            btn_agregar.click()

        # Finalizar pedido inicial
        Log().info("Finalizando pedido inicial")
        btn_finalizar = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, finalizar)))
        btn_finalizar.click()

        # Configurar metodo de pago inicial
        Log().info("Configurando método de pago inicial")
        imagen_pago = wait.until(EC.element_to_be_clickable((AppiumBy.CLASS_NAME, imagen)))
        imagen_pago.click()

        metodo_boleto = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                               "new UiSelector().text(\"Boleto\")")))
        metodo_boleto.click()

        btn_salvar_pago = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        btn_salvar_pago.click()

        btn_salvar_config = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        btn_salvar_config.click()
        FuncionesBrasil.captura_pantalla(driver, "TC50-Metodo Pago", request)

        # Configurar parcelas
        Log().info("Configurando parcelas")
        campo_parcela1 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                "new UiSelector().className("
                                                                "\"android.widget.TextView\").instance(21)")))
        campo_parcela1.click()

        valor_3 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, numero_3)))
        valor_3.click()

        campo_parcela2 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                "new UiSelector().className("
                                                                "\"android.widget.TextView\").instance(22)")))
        campo_parcela2.click()

        valor_4 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                         "new UiSelector().text(\"4\")")))
        valor_4.click()

        # Configurar tipo de parcelado
        Log().info("Configurando tipo de parcelado")
        for i in range(3):
            campo_tipo = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, text_view_35)))
            campo_tipo.click()

        valor_4_instance = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                  "new UiSelector().text(\"4\").instance(0)")))
        valor_4_instance.click()

        valor_3_final = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, numero_3)))
        valor_3_final.click()

        campo_tipo_final = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, text_view_35)))
        campo_tipo_final.click()

        opcion_menu = wait.until(EC.element_to_be_clickable((AppiumBy.ID, contextmenu_item)))
        opcion_menu.click()
        FuncionesBrasil.captura_pantalla(driver, "TC50-Configuracion Parcelas", request)

        # Llenar campo de texto inicial
        Log().info("Llenando campo de texto inicial")
        campo_texto = wait.until(EC.element_to_be_clickable((AppiumBy.CLASS_NAME, "android.widget.EditText")))
        campo_texto.click()
        campo_texto.send_keys(test_stock_text)
        press_back()

        # Guardar como pendiente
        Log().info("Guardando como pendiente")
        itens_pedido_btn = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, itens_pedido)))
        itens_pedido_btn.click()

        imagen_item = wait.until(EC.element_to_be_clickable((AppiumBy.CLASS_NAME, imagen)))
        imagen_item.click()

        btn_salvar_item = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        btn_salvar_item.click()

        btn_salvar_sem_finalizar = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                          "new UiSelector().text(\"Salvar sem "
                                                                          "finalizar\")")))
        btn_salvar_sem_finalizar.click()

        btn_salvar_acao = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        btn_salvar_acao.click()
        FuncionesBrasil.captura_pantalla(driver, "TC50-Pedido Pendiente", request)

        # Verificar contador pendiente
        Log().info("Verificando contador pendientes")
        contador_pendientes = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                     "new UiSelector().text(\"Pendentes\n1\")")))
        contador_pendientes.click()

        btn_editar = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                            "new UiSelector().text(\"Editar\")")))
        btn_editar.click()

        btn_agregar_adicional = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                       "new UiSelector().className("
                                                                       "\"android.widget.ImageView\").instance(15)")))
        btn_agregar_adicional.click()

        btn_finalizar_editado = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, finalizar)))
        btn_finalizar_editado.click()
        FuncionesBrasil.captura_pantalla(driver, "TC50-Pedido Editado", request)

        # Configurar metodo de pago editado
        Log().info("Configurando método de pago editado")
        imagen_pago_editado = wait.until(EC.element_to_be_clickable((AppiumBy.CLASS_NAME, imagen)))
        imagen_pago_editado.click()

        metodo_cartao = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, cartao_credito)))
        metodo_cartao.click()

        btn_salvar_cartao = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        btn_salvar_cartao.click()

        # Configurar comprovante de pagamento
        Log().info("Configurando comprovante de pagamento")
        comprovante_pago = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                  "new UiSelector().text("
                                                                  "\"Comprovante de pagamento\")")))
        comprovante_pago.click()

        campo_especifico = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, text_view_20)))
        campo_especifico.click()

        opcion_menu2 = wait.until(EC.element_to_be_clickable((AppiumBy.ID, contextmenu_item)))
        opcion_menu2.click()

        Log().info("Llenando campos de comprovante")
        campo_adesivo = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID,
                                                               "Adesivo no comprovante (escrito SN)")))
        campo_adesivo.click()
        campo_adesivo.send_keys(test_stock_text)
        press_back()

        campo_stone = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID,
                                                             "Últimos 6 dígitos do STONE ID")))
        campo_stone.click()
        campo_stone.send_keys("PENDIENTE editado")
        press_back()
        FuncionesBrasil.captura_pantalla(driver, "TC50-Comprovante Configurado", request)

        # Guardar sin finalizar nuevamente
        Log().info("Guardando sin finalizar nuevamente")
        itens_pedido2 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, itens_pedido)))
        itens_pedido2.click()

        imagen_item2 = wait.until(EC.element_to_be_clickable((AppiumBy.CLASS_NAME, imagen)))
        imagen_item2.click()

        btn_salvar_item2 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        btn_salvar_item2.click()

        btn_salvar_sem_finalizar2 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                           "new UiSelector().text(\"Salvar sem "
                                                                           "finalizar\")")))
        btn_salvar_sem_finalizar2.click()

        btn_salvar_acao2 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        btn_salvar_acao2.click()

        btn_editar2 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                             "new UiSelector().text(\"Editar\")")))
        btn_editar2.click()
        FuncionesBrasil.captura_pantalla(driver, "TC50-Segunda Edicion", request)

        # Agregar más productos
        Log().info("Agregando más productos")
        btn_agregar_mas = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                 "new UiSelector().className("
                                                                 "\"android.widget.ImageView\").instance(26)")))
        btn_agregar_mas.click()
        btn_agregar_mas.click()

        btn_sinergia = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                              "new UiSelector().text(\"Sinergia\")")))
        btn_sinergia.click()

        producto_cricket = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                  "new UiSelector().text(\"CRICKET ISQUEIRO MINI "
                                                                  "BANDEJA\")")))
        producto_cricket.click()

        btn_agregar_cricket = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                     "new UiSelector().className("
                                                                     "\"android.widget.ImageView\").instance(4)")))
        btn_agregar_cricket.click()
        FuncionesBrasil.captura_pantalla(driver, "TC50-Productos Agregados", request)

        # Finalizar definitivamente
        Log().info("Finalizando definitivamente")
        btn_finalizar_definitivo = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, finalizar)))
        btn_finalizar_definitivo.click()

        imagen_pago_final = wait.until(EC.element_to_be_clickable((AppiumBy.CLASS_NAME, imagen)))
        imagen_pago_final.click()

        metodo_cartao_final = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, cartao_credito)))
        metodo_cartao_final.click()

        btn_salvar_final = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        btn_salvar_final.click()

        # Configurar comprovante final
        Log().info("Configurando comprovante final")
        campo_especifico_final = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, text_view_20)))
        campo_especifico_final.click()

        opcion_menu_final = wait.until(EC.element_to_be_clickable((AppiumBy.ID, contextmenu_item)))
        opcion_menu_final.click()

        campo_adesivo_final = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID,
                                                                     "Adesivo no comprovante (escrito SN)")))
        campo_adesivo_final.click()
        campo_adesivo_final.send_keys("Test Pendiente a Finalizado")
        press_back()

        campo_stone_final = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID,
                                                                   "Últimos 6 dígitos do STONE ID")))
        campo_stone_final.click()
        campo_stone_final.send_keys("1234567")
        press_back()
        FuncionesBrasil.captura_pantalla(driver, "TC50-Comprovante Final", request)

        # Finalizar pedido completamente
        Log().info("Finalizando pedido completamente")
        itens_pedido_final = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, itens_pedido)))
        itens_pedido_final.click()

        imagen_final = wait.until(EC.element_to_be_clickable((AppiumBy.CLASS_NAME, imagen)))
        imagen_final.click()

        btn_salvar_final_item = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        btn_salvar_final_item.click()

        btn_finalizar_pedido = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                      "new UiSelector().text(\"Finalizar pedido\")")))
        btn_finalizar_pedido.click()

        btn_salvar_pedido_final = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        btn_salvar_pedido_final.click()
        FuncionesBrasil.captura_pantalla(driver, "TC50-Pedido Finalizado", request)

        # Verificar contador finalizadas
        Log().info("Verificando contador finalizadas - TC050 completado exitosamente")
        contador_finalizadas = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                      "new UiSelector().text(\"Finalizadas\n1\")")))
        contador_finalizadas.click()
        FuncionesBrasil.captura_pantalla(driver, "TC50-Completado", request)

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
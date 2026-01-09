# *******************************
# TC49 - Stock - ventas emitidas
# *******************************


from FuncionesGralBrasil import *
from Configuracion import *

# Variables Globales
salvar = "new UiSelector().text(\"Salvar\")"
aceitar = "new UiSelector().text(\"Aceitar\")"
boton = "android:id/button2"
finalizar = "new UiSelector().text(\"Finalizar\")"
niteroi_cliente = "new UiSelector().text(\"NITEROI ROD LANCHES LTDA ME\")"
press_back_key = {"keycode": 4}


def press_back():
    driver.execute_script('mobile:pressKey', press_back_key)


def ingreso_app(self, request):
    try:
        Log().info("Iniciando ingreso a la aplicación")
        FuncionesBrasil.ingreso_app(self)
        FuncionesBrasil.captura_pantalla(driver, "TC49-Ingreso App", request)
    except Exception as e:  # pragma: no cover
        Log().error(f"No se logró ingresar a la aplicación, validar el error: {e}")
        raise


def configuracion_inicial(self, request):
    try:
        Log().info("Iniciando carga de usuario")
        FuncionesBrasil.cargar(self)
        FuncionesBrasil.captura_pantalla(driver, "TC49-Carga Usuario", request)
    except Exception as e:  # pragma: no cover
        Log().error(f"No se logró cargar usuario, validar el error: {e}")
        raise

    try:
        Log().info("Iniciando registro de punto")
        FuncionesBrasil.registro_punto(self)
        FuncionesBrasil.captura_pantalla(driver, "TC49-Registro Punto", request)
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
        FuncionesBrasil.captura_pantalla(driver, "TC49-Cliente Seleccionado", request)

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
        FuncionesBrasil.captura_pantalla(driver, "TC49-Visita Iniciada", request)

        # Realizar venta
        Log().info("Iniciando proceso de venta")
        btn_realizar_venda = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                    "new UiSelector().text(\"Realizar venda\")")))
        btn_realizar_venda.click()

        # Aceptar diálogo de venta
        Log().info("Aceptando diálogo de venta")
        btn_aceptar_venta = wait.until(EC.element_to_be_clickable((AppiumBy.ID, boton)))
        btn_aceptar_venta.click()

        # Seleccionar producto CHESTERFIELD BLUE BOX
        Log().info("Seleccionando producto CHESTERFIELD BLUE BOX")
        producto_blue = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                               "new UiSelector().text(\"CHESTERFIELD BLUE BOX\")")))
        producto_blue.click()
        FuncionesBrasil.captura_pantalla(driver, "TC49-Producto Seleccionado", request)

        # Agregar cantidades múltiples
        Log().info("Agregando cantidades múltiples")
        instances = [4, 10, 15, 17, 26, 32]
        for i, instance in enumerate(instances, 1):
            btn_agregar = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                 f"new UiSelector().className("
                                                                 f"\"android.widget.ImageView\")."
                                                                 f"instance({instance})")))
            btn_agregar.click()

        # Finalizar pedido
        Log().info("Finalizando pedido")
        btn_finalizar = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, finalizar)))
        btn_finalizar.click()
        FuncionesBrasil.captura_pantalla(driver, "TC49-Pedido Finalizado", request)

        # Seleccionar metodo de pago
        Log().info("Seleccionando método manual")
        btn_manual = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                            "new UiSelector().text(\"Manual\")")))
        btn_manual.click()

        # Seleccionar adicional
        btn_adicional = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                               "new UiSelector().text(\"Adicional\")")))
        btn_adicional.click()

        # Navegar hacia atrás
        Log().info("Navegando hacia atrás")
        btn_back = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                          "new UiSelector().className("
                                                          "\"android.widget.ImageView\").instance(0)")))
        btn_back.click()

        # Aceptar diálogo
        btn_aceptar_dialogo = wait.until(EC.element_to_be_clickable((AppiumBy.ID, boton)))
        btn_aceptar_dialogo.click()
        FuncionesBrasil.captura_pantalla(driver, "TC49-Metodo Manual", request)

        # Seleccionar metodo de pago CARTA DE CREDITO
        Log().info("Seleccionando método Cartão de crédito")
        metodo_cartao = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                               "new UiSelector().text(\"Cartão de crédito\")")))
        metodo_cartao.click()

        # Guardar metodo de pago
        btn_salvar_pago = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        btn_salvar_pago.click()

        # Acceder a comprovante de pagamento
        Log().info("Accediendo a comprovante de pagamento")
        comprovante_pago = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                  "new UiSelector().text("
                                                                  "\"Comprovante de pagamento\")")))
        comprovante_pago.click()

        # Seleccionar campo específico
        campo_especifico = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                  "new UiSelector().className("
                                                                  "\"android.widget.TextView\").instance(20)")))
        campo_especifico.click()

        # Seleccionar opción del menú contextual
        opcion_menu = wait.until(EC.element_to_be_clickable((AppiumBy.ID,
                                                             "uy.com.assist.eaf:id/contextmenu_item_text")))
        opcion_menu.click()
        FuncionesBrasil.captura_pantalla(driver, "TC49-Comprovante Pagamento", request)

        # Llenar campo adesivo
        Log().info("Llenando campos de comprovante")
        campo_adesivo = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID,
                                                               "Adesivo no comprovante (escrito SN)")))
        campo_adesivo.click()
        campo_adesivo.send_keys("Test 1 stock finalizado")
        press_back()

        # Llenar campo Stone ID
        campo_stone = wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID,
                                                             "Últimos 6 dígitos do STONE ID")))
        campo_stone.click()
        campo_stone.send_keys("1111111")
        press_back()
        FuncionesBrasil.captura_pantalla(driver, "TC49-Datos Comprovante", request)

        # Acceder a itens do pedido
        Log().info("Accediendo a ítems do pedido")
        itens_pedido = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                              "new UiSelector().text(\"Itens do pedido\")")))
        itens_pedido.click()

        # Seleccionar imagen
        imagen_item = wait.until(EC.element_to_be_clickable((AppiumBy.CLASS_NAME, "android.widget.ImageView")))
        imagen_item.click()

        # Guardar cambios
        btn_salvar_cambios = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        btn_salvar_cambios.click()

        # Finalizar pedido
        Log().info("Finalizando pedido completo")
        btn_finalizar_pedido = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                      "new UiSelector().text(\"Finalizar pedido\")")))
        btn_finalizar_pedido.click()

        # Guardar finalización
        btn_salvar_final = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        btn_salvar_final.click()
        FuncionesBrasil.captura_pantalla(driver, "TC49-Pedido Guardado", request)

        # Verificar contador finalizadas
        Log().info("Verificando contador finalizadas - TC049 completado exitosamente")
        contador_finalizadas = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                      "new UiSelector().text(\"Finalizadas\n1\")")))
        contador_finalizadas.click()
        FuncionesBrasil.captura_pantalla(driver, "TC49-Completado", request)

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
from FuncionesGralBrasil import *
from Configuracion import *

# Variables Globales
salvar = "new UiSelector().text(\"Salvar\")"
boton = "android:id/button2"
imagen = "android.widget.ImageView"
# Variables repetidas identificadas
sim = "new UiSelector().text(\"Sim\")"
finalizar = "new UiSelector().text(\"Finalizar\")"
image_view_4 = "new UiSelector().className(\"android.widget.ImageView\").instance(4)"
image_view_15 = "new UiSelector().className(\"android.widget.ImageView\").instance(15)"
image_view_26 = "new UiSelector().className(\"android.widget.ImageView\").instance(26)"
text_view_21 = "new UiSelector().className(\"android.widget.TextView\").instance(21)"
text_view_22 = "new UiSelector().className(\"android.widget.TextView\").instance(22)"
numero_2 = "new UiSelector().text(\"2\")"
numero_3 = "new UiSelector().text(\"3\")"
items_pedido = "new UiSelector().text(\"Itens do pedido\")"
salvar_sin_finalizar = "new UiSelector().text(\"Salvar sem finalizar\")"
press_back_key = {'keycode': 4}


def press_back():
    """Función auxiliar para presionar tecla atrás"""
    driver.execute_script('mobile:pressKey', press_back_key)


def ingreso_app(self, request):
    try:
        Log().info("Iniciando ingreso a la aplicación")
        FuncionesBrasil.ingreso_app(self)
        FuncionesBrasil.captura_pantalla(driver, "TC56-Ingreso App", request)
    except Exception as e:  # pragma: no cover
        Log().error(f"No se logró ingresar a la aplicación, validar el error: {e}")
        raise


def configuracion_inicial(self, request):
    try:
        Log().info("Iniciando carga de usuario")
        FuncionesBrasil.cargar(self)
        FuncionesBrasil.captura_pantalla(driver, "TC56-Carga Usuario", request)
    except Exception as e:  # pragma: no cover
        Log().error(f"No se logró cargar usuario, validar el error: {e}")
        raise

    try:
        Log().info("Iniciando registro de punto")
        FuncionesBrasil.registro_punto(self)
        FuncionesBrasil.captura_pantalla(driver, "TC56-Registro Punto", request)
    except Exception as e:  # pragma: no cover
        Log().error(f"No se logró registrar punto, validar el error: {e}")
        raise


def pegar_funcion(request):
    try:
        # ==================================================
        #      PEGAR CÓDIGO DE APPIUM RECORDER ABAJO
        # ==================================================

        # Seleccionar cliente MARIA LUCIA DA SILVA ANDRADE
        Log().info("Seleccionando primer cliente")
        el46 = wait.until(EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"MARIA LUCIA DA SILVA ANDRADE\")")))
        el46.click()
        el46.click()
        Log().info("Cliente MARIA LUCIA DA SILVA ANDRADE seleccionado")
        FuncionesBrasil.captura_pantalla(driver, "TC56-Cliente1 Seleccionado", request)

        # Iniciar visita
        Log().info("Iniciando visita")
        el47 = wait.until(EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Iniciar visita\")")))
        el47.click()

        # Aceptar inicio de visita
        el48 = wait.until(EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Aceitar\")")))
        el48.click()
        Log().info("Inicio de visita confirmado")

        # Acceder a datos del cliente
        Log().info("Accediendo a datos del cliente")
        el49 = wait.until(EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Dados do cliente\")")))
        el49.click()

        # Realizar venta
        Log().info("Realizando primera venta")
        el50 = wait.until(EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Realizar venda\")")))
        el50.click()
        FuncionesBrasil.captura_pantalla(driver, "TC56-Realizar Venda1", request)

        # Confirmar diálogo de venta
        Log().info("Seleccionando productos para primera venta")
        el51 = wait.until(EC.element_to_be_clickable((AppiumBy.ID, boton)))
        el51.click()

        # Seleccionar artículo CHESTERFIELD BLUE BOX
        el52 = wait.until(EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"CHESTERFIELD BLUE BOX\")")))
        el52.click()

        # Agregar cantidad del primer artículo
        el53 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, image_view_4)))
        el53.click()
        Log().info("Cantidad agregada para CHESTERFIELD BLUE BOX")

        # Seleccionar artículo CHESTERFIELD ORIGINAL BOX
        el54 = wait.until(EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"CHESTERFIELD ORIGINAL BOX\")")))
        el54.click()

        # Agregar cantidad del segundo artículo
        el55 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, image_view_15)))
        el55.click()
        Log().info("Cantidad agregada para CHESTERFIELD ORIGINAL BOX")

        # Seleccionar artículo CHF Terras Blue
        el56 = wait.until(EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"CHF Terras Blue\")")))
        el56.click()

        # Agregar cantidad del tercer artículo
        el57 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, image_view_26)))
        el57.click()
        Log().info("Cantidad agregada para CHF Terras Blue")
        time.sleep(2)

        # Finalizar selección de artículos
        Log().info("Finalizando selección de productos")
        el58 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, finalizar)))
        el58.click()
        FuncionesBrasil.captura_pantalla(driver, "TC56-Finalizar Venta1", request)

        # Continuar con el proceso
        time.sleep(2)
        Log().info("Configurando método de pago")
        el59 = wait.until(EC.element_to_be_clickable((AppiumBy.CLASS_NAME, imagen)))
        el59.click()
        el60 = wait.until(EC.element_to_be_clickable((AppiumBy.ID, boton)))
        el60.click()

        # Seleccionar forma de pago: Boleto
        el61 = wait.until(EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Boleto\")")))
        el61.click()

        # Guardar configuración de pago
        Log().info("Guardando configuración de pago")
        el62 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        el62.click()
        el63 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, sim)))
        el63.click()
        el64 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, sim)))
        el64.click()
        el65 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        el65.click()

        # Configurar parcelas
        Log().info("Configurando parcelas")
        el66 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, text_view_21)))
        el66.click()
        el67 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, numero_2)))
        el67.click()
        el68 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, text_view_22)))
        el68.click()
        el69 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, numero_2)))
        el69.click()
        el70 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                      "new UiSelector().className("
                                                      "\"android.widget.TextView\").instance(35)")))
        el70.click()
        el71 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                      "new UiSelector().text(\"B470 - 2/2 dias, parcelado\")")))
        el71.click()

        # Ingresar observación
        el72 = wait.until(EC.element_to_be_clickable((AppiumBy.CLASS_NAME, "android.widget.EditText")))
        el72.click()
        el72.send_keys("Prueba")

        press_back()
        Log().info("Observación 'Prueba' ingresada")
        FuncionesBrasil.captura_pantalla(driver, "TC56-Parcelas Configuradas", request)

        # Revisar ítems del pedido
        Log().info("Accediendo a ítems del pedido")
        el73 = wait.until(EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, items_pedido)))
        el73.click()
        el74 = wait.until(EC.element_to_be_clickable((AppiumBy.CLASS_NAME, imagen)))
        el74.click()

        # Guardar sin finalizar (crear venta pendiente)
        Log().info("Guardando sin finalizar")
        el75 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        el75.click()
        el76 = wait.until(EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, salvar_sin_finalizar)))
        el76.click()
        el77 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        el77.click()
        Log().info("Primera venta guardada como pendiente")
        FuncionesBrasil.captura_pantalla(driver, "TC56-Primera Venta Pendiente", request)

        # Seleccionar cliente NITEROI ROD LANCHES LTDA ME
        Log().info("Seleccionando segundo cliente")
        el78 = wait.until(EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"NITEROI ROD LANCHES LTDA ME\")")))
        el78.click()
        el78.click()
        Log().info("Cliente NITEROI ROD LANCHES LTDA ME seleccionado")
        FuncionesBrasil.captura_pantalla(driver, "TC56-Cliente2 Seleccionado", request)

        # Acceder a datos del segundo cliente
        Log().info("Accediendo a datos del segundo cliente")
        el79 = wait.until(EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Dados do cliente\")")))
        el79.click()

        # Iniciar segunda visita
        Log().info("Iniciando segunda visita")
        el80 = wait.until(EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Iniciar visita\")")))
        el80.click()
        el81 = wait.until(EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Aceitar\")")))
        el81.click()

        # Realizar segunda venta
        Log().info("Realizando segunda venta")
        el82 = wait.until(EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Realizar venda\")")))
        el82.click()
        FuncionesBrasil.captura_pantalla(driver, "TC56-Realizar Venda2", request)

        # Confirmar segundo diálogo de venta
        Log().info("Seleccionando productos para segunda venta")
        el83 = wait.until(EC.element_to_be_clickable((AppiumBy.ID, boton)))
        el83.click()

        # Agregar múltiples artículos
        el84 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, image_view_4)))
        el84.click()
        el85 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, image_view_15)))
        el85.click()
        el86 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, image_view_26)))
        el86.click()

        # Seleccionar artículo Sinergia
        Log().info("Accediendo a Sinergia")
        el87 = wait.until(EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Sinergia\")")))
        el87.click()
        FuncionesBrasil.captura_pantalla(driver, "TC56-Ingreso Sinergia", request)

        # Agregar múltiples cantidades de Sinergia
        el88 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, image_view_4)))
        el88.click()
        el89 = wait.until(EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.ImageView\").instance(9)")))
        el89.click()
        el90 = wait.until(EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.ImageView\").instance(14)")))
        el90.click()
        el91 = wait.until(EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.ImageView\").instance(19)")))
        el91.click()
        time.sleep(2)

        # Finalizar segunda selección de artículos
        Log().info("Finalizando segunda selección")
        el92 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, finalizar)))
        el92.click()
        FuncionesBrasil.captura_pantalla(driver, "TC56-Finalizar Venta2", request)

        # Continuar con segundo proceso
        time.sleep(2)
        Log().info("Configurando pago con tarjeta")
        el93 = wait.until(EC.element_to_be_clickable((AppiumBy.CLASS_NAME, imagen)))
        el93.click()
        el94 = wait.until(EC.element_to_be_clickable((AppiumBy.ID, boton)))
        el94.click()

        # Seleccionar forma de pago: Tarjeta de crédito
        el95 = wait.until(EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Cartão de crédito\")")))
        el95.click()
        el96 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        el96.click()

        # Configurar datos del comprobante
        Log().info("Ingresando datos de tarjeta")
        el97 = wait.until(EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().className(\"android.widget.TextView\").instance(20)")))
        el97.click()
        el98 = wait.until(EC.element_to_be_clickable(
            (AppiumBy.ID, "uy.com.assist.eaf:id/contextmenu_item_text")))
        el98.click()

        # Ingresar número de adhesivo
        el99 = wait.until(EC.element_to_be_clickable(
            (AppiumBy.ACCESSIBILITY_ID, "Adesivo no comprovante (escrito SN)")))
        el99.click()
        el99.send_keys("Pendiente 2")
        press_back()

        # Ingresar STONE ID
        el100 = wait.until(EC.element_to_be_clickable(
            (AppiumBy.ACCESSIBILITY_ID, "Últimos 6 dígitos do STONE ID")))
        el100.click()
        el100.send_keys("2222222")
        press_back()
        Log().info("STONE ID '2222222' ingresado")
        FuncionesBrasil.captura_pantalla(driver, "TC56-Datos Tarjeta", request)

        # Revisar ítems del segundo pedido
        Log().info("Guardando segunda venta como pendiente")
        el101 = wait.until(EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, items_pedido)))
        el101.click()
        el102 = wait.until(EC.element_to_be_clickable((AppiumBy.CLASS_NAME, imagen)))
        el102.click()
        el103 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        el103.click()
        el104 = wait.until(EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, salvar_sin_finalizar)))
        el104.click()
        el105 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        el105.click()
        Log().info("Segunda venta guardada como pendiente")
        FuncionesBrasil.captura_pantalla(driver, "TC56-Segunda Venta Pendiente", request)

        # Verificar ventas pendientes (2)
        Log().info("Accediendo a pendientes")
        el106 = wait.until(EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Pendentes\n2\")")))
        el106.click()
        FuncionesBrasil.captura_pantalla(driver, "TC56-Ingreso Pendientes", request)

        # Seleccionar primera venta pendiente para editar
        el107 = wait.until(EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"MARIA LUCIA DA SILVA ANDRADE\")")))
        el107.click()

        # Editar venta pendiente
        Log().info("Editando venta pendiente")
        el108 = wait.until(EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Editar\").instance(0)")))
        el108.click()
        FuncionesBrasil.captura_pantalla(driver, "TC56-Editar Pendiente", request)

        # Modificar artículos existentes
        Log().info("Modificando productos existentes")
        el109 = wait.until(EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"CHESTERFIELD BLUE BOX\")")))
        el109.click()
        el110 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, image_view_4)))
        el110.click()
        el111 = wait.until(EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"CHESTERFIELD ORIGINAL BOX\")")))
        el111.click()
        el112 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, image_view_15)))
        el112.click()
        el113 = wait.until(EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"CHF Terras Blue\")")))
        el113.click()
        el114 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, image_view_26)))
        el114.click()

        # Finalizar edición de artículos
        Log().info("Finalizando edición")
        el115 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, finalizar)))
        el115.click()
        FuncionesBrasil.captura_pantalla(driver, "TC56-Finalizar Venta Editada", request)

        # Continuar con finalización
        Log().info("Configurando pago con boleto")
        el116 = wait.until(EC.element_to_be_clickable((AppiumBy.CLASS_NAME, imagen)))
        el116.click()
        el117 = wait.until(EC.element_to_be_clickable((AppiumBy.ID, boton)))
        el117.click()

        # Cambiar forma de pago de tarjeta a boleto
        el118 = wait.until(EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Cartão de crédito\")")))
        el118.click()
        el119 = wait.until(EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Boleto\")")))
        el119.click()
        el120 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        el120.click()
        el121 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, sim)))
        el121.click()
        el122 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, sim)))
        el122.click()
        el123 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        el123.click()

        # Actualizar configuración de parcelas a 3
        Log().info("Actualizando parcelas a 3")
        el124 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, text_view_21)))
        el124.click()
        el125 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, numero_3)))
        el125.click()
        el126 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, text_view_22)))
        el126.click()
        el127 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, numero_3)))
        el127.click()
        el128 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                       "new UiSelector().className("
                                                       "\"android.widget.TextView\").instance(35)")))
        el128.click()
        el129 = wait.until(EC.element_to_be_clickable(
            (AppiumBy.ID, "uy.com.assist.eaf:id/contextmenu_item_text")))
        el129.click()

        # Actualizar observación
        el130 = wait.until(EC.element_to_be_clickable((AppiumBy.CLASS_NAME, "android.widget.EditText")))
        el130.click()
        el130.send_keys("Pendiente Editado")
        press_back()
        Log().info("Observación actualizada a 'Pendiente Editado'")
        FuncionesBrasil.captura_pantalla(driver, "TC56-Observacion Editada", request)

        # Revisar ítems del pedido editado
        Log().info("Guardando edición sin finalizar")
        el131 = wait.until(EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, items_pedido)))
        el131.click()
        el132 = wait.until(EC.element_to_be_clickable((AppiumBy.CLASS_NAME, imagen)))
        el132.click()
        el133 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        el133.click()
        el134 = wait.until(EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, salvar_sin_finalizar)))
        el134.click()
        el135 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        el135.click()
        Log().info("Edición guardada sin finalizar")
        FuncionesBrasil.captura_pantalla(driver, "TC56-Edicion Guardada", request)

        # Verificar estado final de visitas
        Log().info("Verificando estado final")
        el136 = wait.until(EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Visitas\n2/8\")")))
        el136.click()
        el137 = wait.until(EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Pendentes\n2\")")))
        el137.click()
        Log().info("Estado final de ventas pendientes verificado: 2")
        FuncionesBrasil.captura_pantalla(driver, "TC56-Estado Final", request)

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

from FuncionesGralBrasil import *
from Configuracion import *

# Variables Globales - Solo elementos que se repiten
cliente_maria = "new UiSelector().text(\"MARIA LUCIA DA SILVA ANDRADE\")"
finalizar = "new UiSelector().text(\"Finalizar\")"
salvar = "new UiSelector().text(\"Salvar\")"
sim = "new UiSelector().text(\"Sim\")"
boleto = "new UiSelector().text(\"Boleto\")"
boton_ok = "android:id/button2"
image_view = "android.widget.ImageView"
valor_2 = "new UiSelector().text(\"2\")"


def ingreso_app(self, request):
    try:
        Log().info("Iniciando ingreso a la aplicación")
        FuncionesBrasil.ingreso_app(self)
        FuncionesBrasil.captura_pantalla(driver, "TC16-Ingreso App", request)
    except Exception as e:  # pragma: no cover
        Log().error(f"No se logró ingresar a la aplicación, validar el error: {e}")
        raise


def configuracion_inicial(self, request):
    try:
        Log().info("Iniciando carga de usuario")
        FuncionesBrasil.cargar(self)
        FuncionesBrasil.captura_pantalla(driver, "TC16-Carga Usuario", request)
    except Exception as e:  # pragma: no cover
        Log().error(f"No se logró cargar usuario, validar el error: {e}")
        raise

    try:
        Log().info("Iniciando registro de punto")
        FuncionesBrasil.registro_punto(self)
        FuncionesBrasil.captura_pantalla(driver, "TC16-Registro Punto", request)
    except Exception as e:  # pragma: no cover
        Log().error(f"No se logró registrar punto, validar el error: {e}")
        raise


def pegar_funcion(request):
    try:
        # ==================================================
        #      PEGAR CÓDIGO DE APPIUM RECORDER ABAJO
        # ==================================================

        # Seleccionar cliente MARIA LUCIA DA SILVA ANDRADE
        Log().info("Seleccionando cliente MARIA LUCIA DA SILVA ANDRADE")
        el1 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, cliente_maria)))
        el1.click()
        el1.click()

        # Iniciar visita
        Log().info("Iniciando visita")
        el2 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                     "new UiSelector().text(\"Iniciar visita\")")))
        el2.click()

        # Aceptar confirmación
        Log().info("Aceptando confirmación")
        el3 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                     "new UiSelector().text(\"Aceitar\")")))
        el3.click()
        FuncionesBrasil.captura_pantalla(driver, "TC16-Visita Iniciada", request)

        # Acceder a dados do cliente
        Log().info("Accediendo a dados do cliente")
        el4 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                     "new UiSelector().text(\"Dados do cliente\")")))
        el4.click()
        FuncionesBrasil.captura_pantalla(driver, "TC16-Dados Cliente", request)

        # Navegar a información financiera
        Log().info("Navegando a información financiera")
        el5 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                     "new UiSelector().className("
                                                     "\"android.widget.ImageView\").instance(1)")))
        el5.click()

        # Acceder a información financiera
        Log().info("Accediendo a información financiera")
        el6 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                     "new UiSelector().text(\"Informação financeira\")")))
        el6.click()
        FuncionesBrasil.captura_pantalla(driver, "TC16-Info Financiera", request)

        # Regresar
        Log().info("Regresando")
        el7 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                     "new UiSelector().className("
                                                     "\"android.widget.ImageView\").instance(0)")))
        el7.click()

        # Realizar venta
        Log().info("Iniciando realizar venda")
        el8 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                     "new UiSelector().text(\"Realizar venda\")")))
        el8.click()
        FuncionesBrasil.captura_pantalla(driver, "TC16-Realizar Venda", request)

        # Manejar mensaje de advertencia
        Log().info("Manejando mensaje de advertencia")
        el9 = wait.until(EC.element_to_be_clickable((AppiumBy.ID, "android:id/message")))
        el9.click()
        el10 = wait.until(EC.element_to_be_clickable((AppiumBy.ID, boton_ok)))
        el10.click()
        FuncionesBrasil.captura_pantalla(driver, "TC16-Advertencia Aceptada", request)

        # Agregar productos - primer producto (7 clics)
        Log().info("Agregando primer producto (7 unidades)")
        el11 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                      "new UiSelector().className("
                                                      "\"android.widget.ImageView\").instance(4)")))
        for i in range(7):
            el11.click()

        # Agregar productos - segundo producto (4 clics)
        Log().info("Agregando segundo producto (4 unidades)")
        el12 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                      "new UiSelector().className("
                                                      "\"android.widget.ImageView\").instance(15)")))
        for i in range(4):
            el12.click()
        FuncionesBrasil.captura_pantalla(driver, "TC16-Productos Agregados", request)

        # Finalizar primer pedido
        Log().info("Finalizando primer pedido")
        el13 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, finalizar)))
        el13.click()
        FuncionesBrasil.captura_pantalla(driver, "TC16-Primer Pedido", request)

        # Manejar imagen de finalización
        Log().info("Manejando imagen de finalización 1")
        el14 = wait.until(EC.element_to_be_clickable((AppiumBy.CLASS_NAME, image_view)))
        el14.click()
        el15 = wait.until(EC.element_to_be_clickable((AppiumBy.ID, boton_ok)))
        el15.click()

        # Segunda imagen de finalización
        Log().info("Manejando imagen de finalización 2")
        el16 = wait.until(EC.element_to_be_clickable((AppiumBy.CLASS_NAME, image_view)))
        el16.click()

        # Agregar más productos (10 clics)
        Log().info("Agregando tercer producto (10 unidades)")
        el17 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                      "new UiSelector().className("
                                                      "\"android.widget.ImageView\").instance(26)")))
        for i in range(10):
            el17.click()

        # Finalizar segundo pedido
        Log().info("Finalizando segundo pedido")
        el18 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, finalizar)))
        el18.click()

        # Manejar imagen de finalización
        Log().info("Manejando imagen de finalización 3")
        el19 = wait.until(EC.element_to_be_clickable((AppiumBy.CLASS_NAME, image_view)))
        el19.click()
        el20 = wait.until(EC.element_to_be_clickable((AppiumBy.ID, boton_ok)))
        el20.click()

        # Seleccionar metodo de pago
        Log().info("Seleccionando método Boleto")
        el21 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, boleto)))
        el21.click()
        el22 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        el22.click()
        FuncionesBrasil.captura_pantalla(driver, "TC16-Metodo Boleto", request)

        # Configurar opciones Sim/Não
        Log().info("Configurando opciones Sim/Não")
        el23 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, sim)))
        el23.click()
        el24 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                      "new UiSelector().text(\"Não\")")))
        el24.click()

        # Agregar más productos (3 clics)
        Log().info("Agregando cuarto producto (3 unidades)")
        el25 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                      "new UiSelector().className("
                                                      "\"android.widget.ImageView\").instance(25)")))
        for i in range(3):
            el25.click()

        # Finalizar tercer pedido
        Log().info("Finalizando tercer pedido")
        el26 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, finalizar)))
        el26.click()

        # Manejar imagen de finalización
        Log().info("Manejando imagen de finalización 4")
        el27 = wait.until(EC.element_to_be_clickable((AppiumBy.CLASS_NAME, image_view)))
        el27.click()
        el28 = wait.until(EC.element_to_be_clickable((AppiumBy.ID, boton_ok)))
        el28.click()

        el29 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        el29.click()
        el30 = wait.until(EC.element_to_be_clickable((AppiumBy.ID, boton_ok)))
        el30.click()

        # Seleccionar metodo de boleto
        Log().info("Seleccionando método Boleto")
        el31 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, boleto)))
        el31.click()
        el32 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        el32.click()
        el33 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, sim)))
        el33.click()

        # Manejar mensaje de cliente inadimplente
        Log().info("Manejando mensaje de cliente inadimplente")
        el34 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                      "new UiSelector().text(\"Cliente inadimplente. "
                                                      "Alega pagamento ou intenção de pagar? Se sim, "
                                                      "o pedido será analisado. Caso contrário, "
                                                      "será cancelado. Deseja continuar?\")")))
        el34.click()
        FuncionesBrasil.captura_pantalla(driver, "TC16-Cliente Inadimplente", request)

        el35 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, sim)))
        el35.click()
        el36 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        el36.click()

        # Verificar cadastro
        Log().info("Verificando cadastro")
        el37 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                      "new UiSelector().text(\"Cadastro: 14\")")))
        el37.click()

        # Configurar parcelas - primera opción
        Log().info("Configurando parcelas")
        el38 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                      "new UiSelector().className("
                                                      "\"android.widget.TextView\").instance(21)")))
        el38.click()
        el39 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, valor_2)))
        el39.click()

        # Configurar parcelas - segunda opción
        el40 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                      "new UiSelector().className("
                                                      "\"android.widget.TextView\").instance(22)")))
        el40.click()
        el41 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, valor_2)))
        el41.click()

        # Configurar tipo de parcelado
        Log().info("Configurando tipo de parcelado")
        el42 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                      "new UiSelector().className("
                                                      "\"android.widget.TextView\").instance(35)")))
        el42.click()
        el43 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                      "new UiSelector().text(\"B470 - 2/2 dias, parcelado\")")))
        el43.click()
        FuncionesBrasil.captura_pantalla(driver, "TC16-Parcelas Configuradas", request)

        el44 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        el44.click()

        # Finalizar pedido
        Log().info("Finalizando pedido")
        el45 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                      "new UiSelector().text(\"Finalizar pedido\")")))
        el45.click()
        el46 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        el46.click()
        FuncionesBrasil.captura_pantalla(driver, "TC16-Pedido Finalizado", request)

        # Verificar finalizadas
        Log().info("Verificando pedidos finalizados")
        el47 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                      "new UiSelector().text(\"Finalizadas\n1\")")))
        el47.click()
        FuncionesBrasil.captura_pantalla(driver, "TC16-Completado", request)

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
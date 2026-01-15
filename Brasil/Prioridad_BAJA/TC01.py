# *****************************************
# TC01 - Ajuste en pantallas devoluciones - Articulos
# *****************************************


from FuncionesGralBrasil import *
from Configuracion import *

# Variables Globales
salvar = "new UiSelector().text(\"Salvar\")"
aceitar = "new UiSelector().text(\"Aceitar\")"
devolucoes = "new UiSelector().text(\"Devoluções\")"
criar_devolucao = "new UiSelector().text(\"Criar devolução\")"
image_view_1 = "new UiSelector().className(\"android.widget.ImageView\").instance(1)"
maria_cliente = "new UiSelector().text(\"MARIA LUCIA DA SILVA ANDRADE\")"
press_back_key = {"keycode": 4}


def press_back():
    driver.execute_script('mobile:pressKey', press_back_key)


def ingreso_app(self, request):
    try:
        Log().info("Iniciando ingreso a la aplicación")
        FuncionesBrasil.ingreso_app(self)
        FuncionesBrasil.captura_pantalla(driver, "TC01-Ingreso App", request)
    except Exception as e:  # pragma: no cover
        Log().error(f"No se logró ingresar a la aplicación, validar el error: {e}")
        raise


def configuracion_inicial(self, request):
    try:
        Log().info("Iniciando carga de usuario")
        FuncionesBrasil.cargar(self)
        FuncionesBrasil.captura_pantalla(driver, "TC01-Carga Usuario", request)
    except Exception as e:  # pragma: no cover
        Log().error(f"No se logró cargar usuario, validar el error: {e}")
        raise

    try:
        Log().info("Iniciando registro de punto")
        FuncionesBrasil.registro_punto(self)
        FuncionesBrasil.captura_pantalla(driver, "TC01-Registro Punto", request)
    except Exception as e:  # pragma: no cover
        Log().error(f"No se logró registrar punto, validar el error: {e}")
        raise


def pegar_funcion(request):
    try:
        # ==================================================
        #      PEGAR CÓDIGO DE APPIUM RECORDER ABAJO
        # ==================================================

        # Seleccionar cliente MARIA LUCIA DA SILVA ANDRADE
        Log().info("Seleccionando cliente MARIA LUCIA")
        cliente_maria = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, maria_cliente)))
        cliente_maria.click()
        cliente_maria.click()
        FuncionesBrasil.captura_pantalla(driver, "TC01-Cliente Seleccionado", request)

        # Acceder a dados do cliente
        Log().info("Accediendo a dados do cliente")
        btn_dados = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                           "new UiSelector().text(\"Dados do cliente\")")))
        btn_dados.click()

        # Navegar por opciones
        Log().info("Navegando por opciones")
        btn_nav = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, image_view_1)))
        btn_nav.click()

        # Presionar tecla back
        Log().info("Presionando tecla back")
        press_back()
        FuncionesBrasil.captura_pantalla(driver, "TC01-Navegacion Inicial", request)

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
        FuncionesBrasil.captura_pantalla(driver, "TC01-Visita Iniciada", request)

        # Navegar a devoluciones
        Log().info("Navegando a devoluciones")
        btn_nav_devolucoes = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, image_view_1)))
        btn_nav_devolucoes.click()

        # Acceder a devoluciones
        Log().info("Accediendo a devoluciones")
        btn_devolucoes = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, devolucoes)))
        btn_devolucoes.click()
        FuncionesBrasil.captura_pantalla(driver, "TC01-Devoluciones", request)

        # Seleccionar opción a visualizar
        Log().info("Seleccionando opción a visualizar")
        selecionar_opcao = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                  "new UiSelector().text(\"Selecione a opção a "
                                                                  "visualizar\")")))
        selecionar_opcao.click()

        # Crear devolución
        Log().info("Creando devolución")
        criar_devolucao_btn = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, criar_devolucao)))
        criar_devolucao_btn.click()

        # Guardar selección
        btn_salvar = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        btn_salvar.click()
        FuncionesBrasil.captura_pantalla(driver, "TC01-Opcion Seleccionada", request)

        # Acceder a devoluciones nuevamente
        Log().info("Accediendo a devoluciones nuevamente")
        btn_devolucoes2 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, devolucoes)))
        btn_devolucoes2.click()

        # Seleccionar producto específico para devolución
        Log().info("Seleccionando producto CRICKET ISQUEIRO")
        produto_cricket = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                 "new UiSelector().text(\"60017275 CRICKET ISQUEIRO "
                                                                 "MINI BANDEJA\")")))
        produto_cricket.click()
        FuncionesBrasil.captura_pantalla(driver, "TC01-Producto Seleccionado", request)

        # Navegar por opciones del producto
        Log().info("Navegando por opciones del producto")
        btn_nav_produto1 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                  "new UiSelector().className("
                                                                  "\"android.widget.ImageView\").instance(8)")))
        btn_nav_produto1.click()

        btn_nav_produto2 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                  "new UiSelector().className("
                                                                  "\"android.widget.ImageView\").instance(11)")))
        btn_nav_produto2.click()

        # Crear devolución del producto
        Log().info("Creando devolución del producto")
        criar_devolucao2 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, criar_devolucao)))
        criar_devolucao2.click()

        # Acceder a nova devolução
        Log().info("Accediendo a nova devolução")
        nova_devolucao = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                "new UiSelector().text(\"Nova devolução\")")))
        nova_devolucao.click()
        FuncionesBrasil.captura_pantalla(driver, "TC01-Nova Devolucao", request)

        # Seleccionar motivo de devolución
        Log().info("Seleccionando motivo de devolución")
        campo_motivo = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                              "new UiSelector().className("
                                                              "\"android.widget.TextView\").instance(10)")))
        campo_motivo.click()

        motivo_produto_incorreto = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                          "new UiSelector().text("
                                                                          "\"Produto incorreto\")")))
        motivo_produto_incorreto.click()

        # Llenar campo de texto con información adicional
        Log().info("Llenando campo de texto adicional")
        campo_texto = wait.until(EC.element_to_be_clickable((AppiumBy.CLASS_NAME, "android.widget.EditText")))
        campo_texto.click()
        campo_texto.send_keys("1234567")
        press_back()
        FuncionesBrasil.captura_pantalla(driver, "TC01-Motivo Devolucao", request)

        # Guardar devolución
        Log().info("Guardando devolución")
        btn_salvar_devolucao = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        btn_salvar_devolucao.click()

        # Confirmar creación exitosa
        Log().info("Confirmando creación exitosa")
        msg_devolucao_criada = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                      "new UiSelector().text(\"Devolução criada "
                                                                      "corretamente.\")")))
        msg_devolucao_criada.click()

        btn_aceitar_devolucao = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, aceitar)))
        btn_aceitar_devolucao.click()
        FuncionesBrasil.captura_pantalla(driver, "TC01-Devolucao Creada", request)

        # Finalizar sin venta
        Log().info("Finalizando sin venta")
        btn_finalizar_sem_venda = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                         "new UiSelector().text(\"Finalizar sem "
                                                                         "venda\")")))
        btn_finalizar_sem_venda.click()

        # Seleccionar motivo de finalización
        Log().info("Seleccionando motivo de finalización")
        motivo_endereco_errado = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                        "new UiSelector().text(\"Endereço errado\")")))
        motivo_endereco_errado.click()

        # Guardar motivo
        btn_salvar_motivo = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        btn_salvar_motivo.click()
        FuncionesBrasil.captura_pantalla(driver, "TC01-Motivo Finalizacion", request)

        # Confirmar finalización sin venta
        Log().info("Confirmando finalización sin venta")
        confirmacao_final = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                   "new UiSelector().text(\"Tem certeza que deseja "
                                                                   "finalizar a visita sem venda?\")")))
        confirmacao_final.click()

        btn_aceitar_final = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, aceitar)))
        btn_aceitar_final.click()
        FuncionesBrasil.captura_pantalla(driver, "TC01-Completado", request)

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
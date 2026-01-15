# ********************************
# TC02 - Ajuste en pantallas Devoluciones - Precio
# ********************************

from FuncionesGralBrasil import *
from Configuracion import *

# Variables Globales (solo las que se reutilizan)
salvar = "new UiSelector().text(\"Salvar\")"
aceitar = "new UiSelector().text(\"Aceitar\")"
criar_devolucao = "new UiSelector().text(\"Criar devolução\")"
aurenio_cliente = "new UiSelector().text(\"AURENIO DE CARVALHO ANDRADE\").instance(0)"
devolucao_criada = "new UiSelector().text(\"Devolução criada corretamente.\")"
finalizar_sem_venda = "new UiSelector().text(\"Finalizar sem venda\")"
press_back_key = {'keycode': 4}


def press_back():
    """Função auxiliar para pressionar tecla atrás"""
    driver.execute_script('mobile:pressKey', press_back_key)


def ingreso_app(self, request):
    try:
        Log().info("Iniciando ingreso a la aplicación")
        FuncionesBrasil.ingreso_app(self)
        FuncionesBrasil.captura_pantalla(driver, "TC02-Ingreso App", request)
    except Exception as e:  # pragma: no cover
        Log().error(f"No se logró ingresar a la aplicación, validar el error: {e}")
        raise


def configuracion_inicial(self, request):
    try:
        Log().info("Iniciando carga de usuario")
        FuncionesBrasil.cargar(self)
        FuncionesBrasil.captura_pantalla(driver, "TC02-Carga Usuario", request)
    except Exception as e:  # pragma: no cover
        Log().error(f"No se logró cargar los datos, validar el error: {e}")
        raise

    try:
        Log().info("Iniciando registro de punto")
        FuncionesBrasil.registro_punto(self)
        FuncionesBrasil.captura_pantalla(driver, "TC02-Registro Punto", request)
    except Exception as e:  # pragma: no cover
        Log().error(f"No se logró registrar punto, validar el error: {e}")
        raise


def ajuste_pantallas_devoluciones_precio(request):
    try:
        # ==================================================
        #      PEGAR CÓDIGO DE APPIUM RECORDER ABAJO
        # ==================================================

        # Seleccionar cliente AURENIO DE CARVALHO ANDRADE
        Log().info("Seleccionando cliente AURENIO DE CARVALHO ANDRADE")
        cliente_aurenio = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, aurenio_cliente)))
        cliente_aurenio.click()
        cliente_aurenio.click()
        Log().info("Cliente AURENIO DE CARVALHO ANDRADE seleccionado")
        FuncionesBrasil.captura_pantalla(driver, "TC02-Cliente Seleccionado", request)

        # Acceder a dados do cliente
        Log().info("Accediendo a dados do cliente")
        btn_dados_cliente = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 
                                                                   "new UiSelector().text(\"Dados do cliente\")")))
        btn_dados_cliente.click()

        # Iniciar visita
        Log().info("Iniciando visita")
        btn_iniciar_visita = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 
                                                                    "new UiSelector().text(\"Iniciar visita\")")))
        btn_iniciar_visita.click()

        # Aceitar inicio de visita
        Log().info("Confirmando inicio de visita")
        btn_aceitar = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, aceitar)))
        btn_aceitar.click()
        FuncionesBrasil.captura_pantalla(driver, "TC02-Visita Iniciada", request)

        # Acceder al menú principal
        Log().info("Accediendo al menú principal")
        btn_menu_principal = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                    "new UiSelector().className("
                                                                    "\"android.widget.ImageView\").instance(1)")))
        btn_menu_principal.click()

        # Seleccionar opción Devoluções
        Log().info("Seleccionando opción Devoluções")
        btn_devolucoes = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 
                                                                "new UiSelector().text(\"Devoluções\")")))
        btn_devolucoes.click()
        FuncionesBrasil.captura_pantalla(driver, "TC02-Menu Devolucoes", request)

        # Criar devolução
        Log().info("Iniciando proceso de criar devolução")
        btn_criar_devolucao = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, criar_devolucao)))
        btn_criar_devolucao.click()

        # Salvar configuración inicial
        btn_salvar_inicial = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        btn_salvar_inicial.click()
        Log().info("Configuración inicial guardada")

        # Seleccionar artículo FA070240.06 A SAMPOERNA KRETEK
        Log().info("Seleccionando artículo FA070240.06 A SAMPOERNA KRETEK")
        produto_sampoerna = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 
                                                                   "new UiSelector().text("
                                                                   "\"FA070240.06 A SAMPOERNA KRETEK\")")))
        produto_sampoerna.click()
        FuncionesBrasil.captura_pantalla(driver, "TC02-Produto Selecionado", request)

        # Agregar 3 unidades para devolución
        Log().info("Agregando 3 unidades para devolución")
        btn_agregar = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                             "new UiSelector().className("
                                                             "\"android.widget.ImageView\").instance(2)")))
        for i in range(3):
            btn_agregar.click()
        Log().info("3 unidades agregadas para devolución")

        # Proceder a criar devolução
        Log().info("Procediendo a criar devolução")
        btn_criar_devolucao2 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, criar_devolucao)))
        btn_criar_devolucao2.click()

        # Seleccionar motivo da devolução
        Log().info("Configurando motivo da devolução")
        btn_motivo_devolucao = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 
                                                                      "new UiSelector().text("
                                                                      "\"Selecione o motivo da devolução\")")))
        btn_motivo_devolucao.click()

        # Acceder a opciones de motivo
        campo_motivo = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                              "new UiSelector().className("
                                                              "\"android.widget.TextView\").instance(10)")))
        campo_motivo.click()

        # Seleccionar "Erro de digitação" como motivo
        motivo_erro = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 
                                                             "new UiSelector().text(\"Erro de digitação\")")))
        motivo_erro.click()
        Log().info("Motivo 'Erro de digitação' seleccionado")
        FuncionesBrasil.captura_pantalla(driver, "TC02-Motivo Configurado", request)

        # Ingresar observación sobre la devolución
        Log().info("Ingresando observación sobre la devolución")
        campo_observacao = wait.until(EC.element_to_be_clickable((AppiumBy.CLASS_NAME, "android.widget.EditText")))
        campo_observacao.click()
        campo_observacao.send_keys("Test Devolucion ")
        press_back()

        # Salvar devolução
        Log().info("Guardando devolução")
        btn_salvar_devolucao = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        btn_salvar_devolucao.click()

        # Verificar mensaje de confirmación
        Log().info("Verificando mensaje de confirmación")
        mensaje_confirmacao = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, devolucao_criada)))
        mensaje_confirmacao.click()

        # Aceitar confirmación
        btn_aceitar_confirmacao = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, aceitar)))
        btn_aceitar_confirmacao.click()
        Log().info("Devolução criada corretamente - Confirmación aceptada")
        FuncionesBrasil.captura_pantalla(driver, "TC02-Devolucao Criada", request)

        # Finalizar sin venta
        Log().info("Finalizando sem venda")
        btn_finalizar_sem_venda = wait.until(EC.element_to_be_clickable((
            AppiumBy.ANDROID_UIAUTOMATOR, finalizar_sem_venda)))
        btn_finalizar_sem_venda.click()

        # Seleccionar motivo "Falta de tempo"
        motivo_falta_tempo = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 
                                                                    "new UiSelector().text(\"Falta de tempo\")")))
        motivo_falta_tempo.click()

        # Salvar finalización sem venda
        btn_salvar_finalizacao = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        btn_salvar_finalizacao.click()

        # Aceitar finalización
        btn_aceitar_finalizacao = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, aceitar)))
        btn_aceitar_finalizacao.click()
        Log().info("Finalización sem venda completada")

        # Verificar en sem venda
        Log().info("Verificando contador sem venda")
        contador_sem_venda = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 
                                                                    "new UiSelector().text(\"Sem venda\n1\")")))
        contador_sem_venda.click()

        # Verificar estado de visitas
        contador_visitas = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 
                                                                  "new UiSelector().text(\"Visitas\n1/8\")")))
        contador_visitas.click()
        # ==================================================
        #                 FIN DEL PEGADO
        # ==================================================
    except Exception as e:  # pragma: no cover
        Log().error(f"No se logró completar la automatización TC02, validar el error: {e}")
        raise


class Test:
    def test_001(self, request):
        ingreso_app(self, request)

    def test_002(self, request):
        configuracion_inicial(self, request)

    def test_003(self, request):
        ajuste_pantallas_devoluciones_precio(request)
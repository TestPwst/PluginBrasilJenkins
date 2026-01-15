# ********************************
# TC03 - Ajuste de Ruta
# ********************************

from FuncionesGralBrasil import *
from Configuracion import *

# Variables Globales
salvar = "new UiSelector().text(\"Salvar\")"
aceitar = "new UiSelector().text(\"Aceitar\")"
cliente_bar = "new UiSelector().text(\"BAR E MERCEARIA PARA PEDRO LTDA\")"
dados_cliente = "new UiSelector().text(\"Dados do cliente\")"
iniciar_visita = "new UiSelector().text(\"Iniciar visita\")"
solicitacoes = "new UiSelector().text(\"Solicitações\")"
ajuste_roteiro = "new UiSelector().text(\"Solicitar ajuste de roteiro\")"
finalizar_sem_venda = "new UiSelector().text(\"Finalizar sem venda\")"


def ingreso_app(self, request):
    try:
        Log().info("Iniciando ingreso a la aplicación")
        FuncionesBrasil.ingreso_app(self)
        FuncionesBrasil.captura_pantalla(driver, "TC03-Ingreso App", request)
    except Exception as e:  # pragma: no cover
        Log().error(f"No se logró ingresar a la aplicación, validar el error: {e}")
        raise


def configuracion_inicial(self, request):
    try:
        Log().info("Iniciando carga de usuario")
        FuncionesBrasil.cargar(self)
        FuncionesBrasil.captura_pantalla(driver, "TC03-Carga Usuario", request)
    except Exception as e:  # pragma: no cover
        Log().error(f"No se logró cargar usuario, validar el error: {e}")
        raise

    try:
        Log().info("Iniciando registro de punto")
        FuncionesBrasil.registro_punto(self)
        FuncionesBrasil.captura_pantalla(driver, "TC03-Registro Punto", request)
    except Exception as e:  # pragma: no cover
        Log().error(f"No se logró registrar punto, validar el error: {e}")
        raise


def pegar_funcion(request):
    try:
        # ==================================================
        #      PEGAR CÓDIGO DE APPIUM RECORDER ABAJO
        # ==================================================
        
        # Buscar y seleccionar cliente BAR E MERCEARIA PARA PEDRO LTDA
        Log().info("Buscando cliente BAR E MERCEARIA PARA PEDRO LTDA")
        el17 = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR,
                                   value='new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new '
                                         'UiSelector().text("BAR E MERCEARIA PARA PEDRO LTDA"))')
        el17.click()
        
        cliente_bar_element = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, cliente_bar)))
        cliente_bar_element.click()
        cliente_bar_element.click()
        Log().info("Cliente BAR E MERCEARIA PARA PEDRO LTDA seleccionado")
        FuncionesBrasil.captura_pantalla(driver, "TC03-Cliente Seleccionado", request)

        # Acceder a datos del cliente
        Log().info("Accediendo a datos del cliente")
        btn_dados_cliente = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, dados_cliente)))
        btn_dados_cliente.click()

        # Iniciar visita
        Log().info("Iniciando visita")
        btn_iniciar_visita = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, iniciar_visita)))
        btn_iniciar_visita.click()

        # Confirmar inicio de visita
        Log().info("Confirmando inicio de visita")
        confirmacion_visita = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                     "new UiSelector().text(\"Tem certeza de que "
                                                                     "deseja iniciar a visita ao cliente?\")")))
        confirmacion_visita.click()

        btn_aceitar = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, aceitar)))
        btn_aceitar.click()
        Log().info("Visita iniciada exitosamente")
        FuncionesBrasil.captura_pantalla(driver, "TC03-Visita Iniciada", request)

        # Navegar a solicitaciones
        Log().info("Navegando a sección de solicitaciones")
        btn_nav_solicitudes = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                     "new UiSelector().className("
                                                                     "\"android.widget.ImageView\").instance(1)")))
        btn_nav_solicitudes.click()

        btn_solicitacoes = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, solicitacoes)))
        btn_solicitacoes.click()
        Log().info("Sección de solicitaciones accedida")

        # PRIMERA SOLICITUD: DIA DE VENDA
        Log().info("Creando primera solicitud - Día de venda")
        btn_ajuste_roteiro = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, ajuste_roteiro)))
        btn_ajuste_roteiro.click()

        # Seleccionar tipo de solicitación
        tipo_solicitacao = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                  "new UiSelector().text(\"Selecione o tipo de "
                                                                  "solicitação\")")))
        tipo_solicitacao.click()

        # Navegar por opciones hasta llegar a "Dia de venda"
        opciones = ["Dia de venda", "Frequência", "Zona de venda", "Dia de venda"]
        for opcion in opciones:
            btn_opcion = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                f"new UiSelector().text(\"{opcion}\")")))
            btn_opcion.click()
            Log().info(f"Opción {opcion} seleccionada")

        # Guardar selección
        btn_salvar = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        btn_salvar.click()
        Log().info("Tipo de solicitud guardado")

        # Configurar día de venda
        Log().info("Configurando día de venda")
        campo_dia = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                           "new UiSelector().className("
                                                           "\"android.widget.TextView\").instance(10)")))
        campo_dia.click()

        dia_segunda = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                             "new UiSelector().text(\"Segunda-feira\")")))
        dia_segunda.click()

        btn_salvar_dia = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        btn_salvar_dia.click()
        Log().info("Día configurado exitosamente")

        # Manejar mensaje de confirmación
        mensaje_confirmacion = wait.until(EC.element_to_be_clickable((AppiumBy.ID, "android:id/message")))
        mensaje_confirmacion.click()
        btn_aceptar_mensaje = wait.until(EC.element_to_be_clickable((AppiumBy.ID, "android:id/button2")))
        btn_aceptar_mensaje.click()

        # Configurar motivo
        Log().info("Configurando motivo de la solicitud")
        campo_motivo = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                              "new UiSelector().className("
                                                              "\"android.widget.TextView\").instance(18)")))
        campo_motivo.click()

        motivo_outros = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                               "new UiSelector().text(\"Outros\")")))
        motivo_outros.click()

        # Llenar campo de texto
        campo_texto = wait.until(EC.element_to_be_clickable((AppiumBy.CLASS_NAME, "android.widget.EditText")))
        campo_texto.click()
        campo_texto.send_keys("test")
        driver.execute_script('mobile:pressKey', {"keycode": 4})

        btn_salvar_motivo = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        btn_salvar_motivo.click()
        Log().info("Motivo configurado exitosamente")

        # Confirmar creación exitosa
        mensaje_sucesso = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                 "new UiSelector().text(\"Solicitação criada com "
                                                                 "sucesso\")")))
        mensaje_sucesso.click()
        btn_aceitar_sucesso = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, aceitar)))
        btn_aceitar_sucesso.click()
        Log().info("Primera solicitud creada exitosamente")
        FuncionesBrasil.captura_pantalla(driver, "TC03-Primera Solicitud", request)

        # SEGUNDA SOLICITUD: ZONA DE VENDA
        Log().info("Creando segunda solicitud - Zona de venda")
        btn_nav_solicitudes2 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                      "new UiSelector().className("
                                                                      "\"android.widget.ImageView\").instance(1)")))
        btn_nav_solicitudes2.click()

        btn_solicitacoes2 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, solicitacoes)))
        btn_solicitacoes2.click()

        btn_ajuste_roteiro2 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, ajuste_roteiro)))
        btn_ajuste_roteiro2.click()

        zona_venda_option = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                   "new UiSelector().text(\"Zona de venda\")")))
        zona_venda_option.click()

        btn_salvar_zona = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        btn_salvar_zona.click()
        Log().info("Zona de venda seleccionada")

        # Llenar campos de zona de venda
        Log().info("Configurando campos de zona de venda")
        campo_zona1 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                             "new UiSelector().className("
                                                             "\"android.widget.EditText\").instance(0)")))
        campo_zona1.click()
        campo_zona1.send_keys("test")

        campo_zona2 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                             "new UiSelector().className("
                                                             "\"android.widget.EditText\").instance(1)")))
        campo_zona2.click()
        campo_zona2.send_keys("prueba")
        driver.execute_script('mobile:pressKey', {"keycode": 4})

        btn_salvar_zona_final = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        btn_salvar_zona_final.click()
        Log().info("Configuración de zona guardada")

        # Confirmar segunda solicitud
        mensaje_sucesso2 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                  "new UiSelector().text(\"Solicitação criada com "
                                                                  "sucesso\")")))
        mensaje_sucesso2.click()
        btn_aceitar_sucesso2 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, aceitar)))
        btn_aceitar_sucesso2.click()
        Log().info("Segunda solicitud creada exitosamente")
        FuncionesBrasil.captura_pantalla(driver, "TC03-Segunda Solicitud", request)

        # FINALIZAR SIN VENTA
        Log().info("Finalizando visita sin venta")
        btn_finalizar_sem_venda = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                         finalizar_sem_venda)))
        btn_finalizar_sem_venda.click()

        motivo_falta_tempo = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                    "new UiSelector().text(\"Falta de tempo\")")))
        motivo_falta_tempo.click()

        btn_salvar_final = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, salvar)))
        btn_salvar_final.click()

        btn_aceitar_final = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, aceitar)))
        btn_aceitar_final.click()
        Log().info("TC03 - Ajuste de Ruta completado exitosamente")
        FuncionesBrasil.captura_pantalla(driver, "TC03-Completado", request)

        # ==================================================
        #                 FIN DEL PEGADO
        # ==================================================
    except Exception as e:  # pragma: no cover
        Log().error(f"No se logró completar la automatización TC03, validar el error: {e}")
        raise


class Test:
    def test_001(self, request):
        ingreso_app(self, request)

    def test_002(self, request):
        configuracion_inicial(self, request)

    def test_003(self, request):
        pegar_funcion(request)
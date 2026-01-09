from Configuracion import *
from VariablesGralBrasil import LocalizadoresBrasil as Localizador
from VariablesGralBrasil import VariablesBrasil as Variables


class FuncionesBrasil:

    def captura_pantalla(driver, nombre=None, request=None):
        # Ruta dinámica desde run_test.py
        carpeta = os.getenv("ASSETS_DIR", "assets")
        os.makedirs(carpeta, exist_ok=True)

        # Determinar nombre de archivo
        if request and hasattr(request, "node") and not nombre:
            nombre_final = request.node.name
        elif nombre:
            nombre_final = nombre
        else:
            nombre_final = "captura"

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        nombre_archivo = f"{nombre_final}_{timestamp}.png"
        ruta = os.path.join(carpeta, nombre_archivo)

        try:
            driver.save_screenshot(ruta)
            Log().info(f"Captura guardada: {ruta}")

            # Agregar imagen al reporte
            if request and hasattr(request, 'node'):
                html_img = (f'<div class="mobile-screenshot"><img src="assets/{nombre_archivo}" alt="screenshot" '
                            f'style="width:350px;height:700px;border-radius:15px;border:2px solid #ddd;" '
                            f'onclick="window.open(this.src)" /></div>')

                if not hasattr(request.node, 'user_properties'):
                    request.node.user_properties = []
                request.node.user_properties.append(("screenshot", html_img))
                Log().info(f"Captura agregada al reporte: {nombre_archivo}")

            return ruta
        except Exception as e:
            Log().error(f"Error al tomar captura: {e}")
            return None

    def ingreso_app(self):
        try:
            btn_aceptar = wait.until(
                EC.presence_of_element_located((AppiumBy.XPATH, Localizador.aceptar_ingreso)))
            btn_aceptar.click()
        except Exception as e:  # pragma: no cover
            Log().error(f"No se logró ingresar a la aplicación, validar el error: {e}")
            raise

        # Ingreso de usuario
        try:
            usuario = wait.until(
                EC.element_to_be_clickable((AppiumBy.XPATH, Localizador.campo_usuario)))
            usuario.send_keys(Variables.usuario)
        except Exception as e:  # pragma: no cover
            Log().error(f"No se logró acceder el usuario, validar el error: {e}")
            raise

        # Ingreso de contraseña
        try:
            contrasena = wait.until(
                EC.element_to_be_clickable((AppiumBy.XPATH, Localizador.campo_contrasena)))
            contrasena.send_keys(Variables.contrasenia)
        except Exception as e:  # pragma: no cover
            Log().error(f"No se logró ingresar la contraseña, validar el error: {e}")
            raise

        # Ingreso del servidor
        try:
            servidor = wait.until(
                EC.element_to_be_clickable((AppiumBy.XPATH, Localizador.campo_servidor)))
            servidor.click()
            servidor.send_keys(Variables.servidor)
        except Exception as e:  # pragma: no cover
            Log().error(f"No se logró ingresar el servidor, validar el error: {e}")
            raise

        # Marcar casilla SSL
        try:
            casilla_ssl = wait.until(
                EC.element_to_be_clickable((AppiumBy.XPATH, Localizador.check_ssl)))
            casilla_ssl.click()
        except Exception as e:  # pragma: no cover
            Log().error(f"No se logró marcar el check, validar el error: {e}")
            raise

        # Instalar
        try:
            instalar = wait.until(
                EC.element_to_be_clickable((AppiumBy.XPATH, Localizador.btn_instalar)))
            instalar.click()
        except Exception as e:  # pragma: no cover
            Log().error(f"No se logró dar click al botón instalar, validar el error: {e}")
            raise

    def cargar(self):
        try:
            cargar = wait.until(
                EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, Localizador.btn_cargar)))
            cargar.click()
        except Exception as e:  # pragma: no cover
            Log().error(f"No se logro dar click al botón cargar, validar el error: {e}")
            raise

        try:
            aceptar_reinicio = wait.until(
                EC.element_to_be_clickable((AppiumBy.XPATH, Localizador.aceptar_msj_reinicio)))
            aceptar_reinicio.click()

            aceptar_reinicio = wait.until(
                EC.element_to_be_clickable((AppiumBy.XPATH, Localizador.aceptar_msj_reinicio)))
            aceptar_reinicio.click()
        except Exception as e:  # pragma: no cover
            Log().error(f"No se logro dar click al botón cargar, validar el error: {e}")
            raise

    def registro_punto(self):
        try:
            el1 = wait.until(
                EC.element_to_be_clickable(
                    (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Inicio\")")))
            el1.click()
            el2 = wait.until(
                EC.element_to_be_clickable(
                    (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Entrar\")")))
            el2.click()
            driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, Localizador.iniciar_jornada)

            el3 = wait.until(
                EC.element_to_be_clickable(
                    (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Iniciar Jornada\")")))
            el3.click()

            el4 = wait.until(
                EC.element_to_be_clickable(
                    (AppiumBy.ANDROID_UIAUTOMATOR,
                     "new UiSelector().className(\"android.widget.ImageView\").instance(0)")))
            el4.click()
            el5 = wait.until(
                EC.element_to_be_clickable(
                    (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Registro de ponto\")")))
            el5.click()

            el3 = wait.until(
                EC.element_to_be_clickable((AppiumBy.
                                            ANDROID_UIAUTOMATOR, 'new UiSelector().text(\"Registrar Ponto\")')))
            el3.click()

            el4 = wait.until(
                EC.element_to_be_clickable(
                    (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text(\"Aceitar\")')))
            el4.click()

            # Escenario 1: Entrada

            if driver.find_elements(AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Continuar\")"):
                el5 = wait.until(
                    EC.element_to_be_clickable(
                        (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Continuar\")")))
                el5.click()
                el6 = wait.until(
                    EC.element_to_be_clickable(
                        (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Outros\")")))
                el6.click()
                el7 = wait.until(
                    EC.element_to_be_clickable(
                        (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Salvar\")")))
                el7.click()
                time.sleep(2)
                el8 = wait.until(
                    EC.element_to_be_clickable(
                        (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text(\"Aceitar\")')))
                el8.click()
                time.sleep(2)
            elif driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Aceitar\")"):
                # Escenario 2: Sin tomar GPS
                el4 = wait.until(
                    EC.element_to_be_clickable(
                        (AppiumBy.ANDROID_UIAUTOMATOR, "new UiSelector().text(\"Aceitar\")")))
                el4.click()
            else:
                driver.close_app()
        except Exception as e:  # pragma: no cover
            Log().error(f"No se logró dar click al botón instalar, validar el error: {e}")
            raise

    def camara(self):
        try:
            # 1. Agregar wait al primer elemento
            el1 = wait.until(EC.element_to_be_clickable(
                (AppiumBy.ANDROID_UIAUTOMATOR,
                 'new UiSelector().className("android.widget.ImageView").instance(3)')))
            el1.click()

            time.sleep(2)

            # 3. Wait para botón de foto
            el2 = wait.until(EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, "Tomar foto")))
            el2.click()

            # 4. Pausa para procesamiento
            time.sleep(2)

            # 5. Wait para confirmar
            el3 = wait.until(EC.element_to_be_clickable(
                (AppiumBy.ACCESSIBILITY_ID, "Listo")))
            el3.click()

            Log().info("Cámara completada exitosamente")

        except Exception as e:  # pragma: no cover
            Log().error(f"No se logró dar click al botón camara, validar el error: {e}")
            raise

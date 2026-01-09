
class VariablesBrasil:
    usuario = "brgvvv001"
    # usuario = "bruvvv005"
    contrasenia = "Pwst12345*"
    #servidor = "m.qa.powerstreet.cloud/mobileservices"
    servidor = "m.assist.com.uy/mobileservices"


class LocalizadoresBrasil:
    aceptar_ingreso = '//android.widget.Button[@text="Aceptar"]'
    campo_usuario = '//android.widget.EditText[@content-desc="Usuario"]'
    campo_contrasena = '//android.widget.EditText[@content-desc="Contraseña"]'
    campo_servidor = '//android.widget.EditText[@content-desc="Servidor"]'
    check_ssl = '//android.widget.CheckBox[@text="Usar SSL"]'
    btn_instalar = '//android.widget.Button[@text="Instalar"]'
    iniciar_jornada = 'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Iniciar Jornada"))'
    btn_cargar = 'new UiSelector().text("cargar")'
    aceptar_msj_reinicio = '//android.widget.Button[@resource-id="android:id/button2"]'
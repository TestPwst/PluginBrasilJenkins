from FuncionesGralBrasil import *
from Configuracion import *


# Configuración general de la plantilla

def ingreso_app(self):
    try:
        FuncionesBrasil.ingreso_app(self)
    except Exception as e:  # pragma: no cover
        Log().error(f"No se logró ingresar a la aplicación, validar el error: {e}")
        raise


def configuracion_inicial(self):
    try:
        FuncionesBrasil.cargar(self)
    except Exception as e:  # pragma: no cover
        Log().error(f"No se logró ingresar a la aplicación, validar el error: {e}")
        raise

    try:
        FuncionesBrasil.registro_punto(self)
    except Exception as e:  # pragma: no cover
        Log().error(f"No se logró ingresar a la aplicación, validar el error: {e}")
        raise


def pegar_funcion():
    try:
        # ==================================================
        #      PEGAR CÓDIGO DE APPIUM RECORDER ABAJO
        # ==================================================

        # Seleccionar cliente MARIA LUCIA DA SILVA ANDRADE
        cliente_maria = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                               "new UiSelector().text(\"MARIA LUCIA DA SILVA ANDRADE\")")))
        cliente_maria.click()
        cliente_maria.click()
        Log().info("Cliente MARIA LUCIA seleccionado")

        # Iniciar visita
        btn_iniciar = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                             "new UiSelector().text(\"Iniciar visita\")")))
        btn_iniciar.click()
        Log().info("Visita iniciada")

        # Aceptar confirmación
        btn_aceitar = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                             "new UiSelector().text(\"Aceitar\")")))
        btn_aceitar.click()
        Log().info("Confirmación aceptada")

        # Acceder a dados do cliente
        btn_dados = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                           "new UiSelector().text(\"Dados do cliente\")")))
        btn_dados.click()
        Log().info("Dados do cliente accedido")

        # Navegar a información financiera
        btn_nav = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                         "new UiSelector().className("
                                                         "\"android.widget.ImageView\").instance(1)")))
        btn_nav.click()
        Log().info("Navegación a información financiera")

        # Acceder a información financiera
        btn_info_financiera = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                     "new UiSelector().text(\"Informação financeira\")")))
        btn_info_financiera.click()
        Log().info("Información financiera accedida")

        # Regresar
        btn_back = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                          "new UiSelector().className("
                                                          "\"android.widget.ImageView\").instance(0)")))
        btn_back.click()
        Log().info("Regreso completado")

        # Realizar venta
        btn_realizar_venda = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                    "new UiSelector().text(\"Realizar venda\")")))
        btn_realizar_venda.click()
        Log().info("Realizar venda iniciado")

        # Manejar mensaje de advertencia
        msg_advertencia = wait.until(EC.element_to_be_clickable((AppiumBy.ID, "android:id/message")))
        msg_advertencia.click()
        Log().info("Mensaje de advertencia visualizado")

        btn_ok = wait.until(EC.element_to_be_clickable((AppiumBy.ID, "android:id/button2")))
        btn_ok.click()
        Log().info("Mensaje de advertencia aceptado")

        # Agregar productos - primer producto (7 clics)
        btn_producto1 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                               "new UiSelector().className("
                                                               "\"android.widget.ImageView\").instance(4)")))
        for i in range(7):
            btn_producto1.click()
        Log().info("Primer producto agregado (7 unidades)")

        # Agregar productos - segundo producto (4 clics)
        btn_producto2 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                               "new UiSelector().className("
                                                               "\"android.widget.ImageView\").instance(15)")))
        for i in range(4):
            btn_producto2.click()
        Log().info("Segundo producto agregado (4 unidades)")

        # Finalizar primer pedido
        btn_finalizar1 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                "new UiSelector().text(\"Finalizar\")")))
        btn_finalizar1.click()
        Log().info("Primer pedido finalizado")

        # Manejar imagen de finalización
        img_finalizacion1 = wait.until(EC.element_to_be_clickable((AppiumBy.CLASS_NAME, "android.widget.ImageView")))
        img_finalizacion1.click()
        Log().info("Imagen de finalización 1")

        btn_ok2 = wait.until(EC.element_to_be_clickable((AppiumBy.ID, "android:id/button2")))
        btn_ok2.click()
        Log().info("OK 2")

        # Segunda imagen de finalización
        img_finalizacion2 = wait.until(EC.element_to_be_clickable((AppiumBy.CLASS_NAME, "android.widget.ImageView")))
        img_finalizacion2.click()
        Log().info("Imagen de finalización 2")

        # Agregar más productos (10 clics)
        btn_producto3 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                               "new UiSelector().className("
                                                               "\"android.widget.ImageView\").instance(26)")))
        for i in range(10):
            btn_producto3.click()
        Log().info("Tercer producto agregado (10 unidades)")

        # Finalizar segundo pedido
        btn_finalizar2 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                "new UiSelector().text(\"Finalizar\")")))
        btn_finalizar2.click()
        Log().info("Segundo pedido finalizado")

        # Manejar imagen de finalización
        img_finalizacion3 = wait.until(EC.element_to_be_clickable((AppiumBy.CLASS_NAME, "android.widget.ImageView")))
        img_finalizacion3.click()
        Log().info("Imagen de finalización 3")

        btn_ok3 = wait.until(EC.element_to_be_clickable((AppiumBy.ID, "android:id/button2")))
        btn_ok3.click()
        Log().info("OK 3")

        # Seleccionar metodo de pago boleto
        metodo_boleto = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                               "new UiSelector().text(\"Boleto\")")))
        metodo_boleto.click()
        Log().info("Método Boleto seleccionado")

        btn_salvar1 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                             "new UiSelector().text(\"Salvar\")")))
        btn_salvar1.click()
        Log().info("Salvar 1")

        # Configurar opciones Sim/Não
        btn_sim = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                         "new UiSelector().text(\"Sim\")")))
        btn_sim.click()
        Log().info("Sim seleccionado")

        btn_nao = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                         "new UiSelector().text(\"Não\")")))
        btn_nao.click()
        Log().info("Não seleccionado")

        # Agregar más productos (3 clics)
        btn_producto4 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                               "new UiSelector().className("
                                                               "\"android.widget.ImageView\").instance(25)")))
        for i in range(3):
            btn_producto4.click()
        Log().info("Cuarto producto agregado (3 unidades)")

        # Finalizar tercer pedido
        btn_finalizar3 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                "new UiSelector().text(\"Finalizar\")")))
        btn_finalizar3.click()
        Log().info("Tercer pedido finalizado")

        # Manejar imagen de finalización
        img_finalizacion4 = wait.until(EC.element_to_be_clickable((AppiumBy.CLASS_NAME, "android.widget.ImageView")))
        img_finalizacion4.click()
        Log().info("Imagen de finalización 4")

        btn_ok4 = wait.until(EC.element_to_be_clickable((AppiumBy.ID, "android:id/button2")))
        btn_ok4.click()
        Log().info("OK 4")

        btn_salvar2 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                             "new UiSelector().text(\"Salvar\")")))
        btn_salvar2.click()
        Log().info("Salvar 2")

        btn_ok5 = wait.until(EC.element_to_be_clickable((AppiumBy.ID, "android:id/button2")))
        btn_ok5.click()
        Log().info("OK 5")

        # Seleccionar metodo boleto nuevamente
        metodo_boleto2 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                "new UiSelector().text(\"Boleto\")")))
        metodo_boleto2.click()
        Log().info("Método Boleto 2 seleccionado")

        btn_salvar3 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                             "new UiSelector().text(\"Salvar\")")))
        btn_salvar3.click()
        Log().info("Salvar 3")

        btn_sim2 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                          "new UiSelector().text(\"Sim\")")))
        btn_sim2.click()
        Log().info("Sim 2 seleccionado")

        # Manejar mensaje de cliente inadimplente
        msg_inadimplente = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                  "new UiSelector().text(\"Cliente inadimplente. "
                                                                  "Alega pagamento ou intenção de pagar? Se sim, "
                                                                  "o pedido será analisado. Caso contrário, "
                                                                  "será cancelado. Deseja continuar?\")")))
        msg_inadimplente.click()
        Log().info("Mensaje de cliente inadimplente visualizado")

        btn_sim3 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                          "new UiSelector().text(\"Sim\")")))
        btn_sim3.click()
        Log().info("Sim 3 - continuar con cliente inadimplente")

        btn_salvar4 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                             "new UiSelector().text(\"Salvar\")")))
        btn_salvar4.click()
        Log().info("Salvar 4")

        # Verificar cadastro
        cadastro_info = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                               "new UiSelector().text(\"Cadastro: 14\")")))
        cadastro_info.click()
        Log().info("Cadastro 14 verificado")

        # Configurar parcelas - primera opción
        campo_parcela1 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                "new UiSelector().className("
                                                                "\"android.widget.TextView\").instance(21)")))
        campo_parcela1.click()
        Log().info("Campo parcela 1 seleccionado")

        valor_2_primera = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                 "new UiSelector().text(\"2\")")))
        valor_2_primera.click()
        Log().info("Valor 2 primera parcela")

        # Configurar parcelas - segunda opción
        campo_parcela2 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                "new UiSelector().className("
                                                                "\"android.widget.TextView\").instance(22)")))
        campo_parcela2.click()
        Log().info("Campo parcela 2 seleccionado")

        valor_2_segunda = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                 "new UiSelector().text(\"2\")")))
        valor_2_segunda.click()
        Log().info("Valor 2 segunda parcela")

        # Configurar tipo de parcelado
        campo_tipo_parcelado = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                      "new UiSelector().className("
                                                                      "\"android.widget.TextView\").instance(35)")))
        campo_tipo_parcelado.click()
        Log().info("Campo tipo parcelado seleccionado")

        tipo_b470 = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                           "new UiSelector().text(\"B470 - 2/2 dias, parcelado\")")))
        tipo_b470.click()
        Log().info("Tipo B470 seleccionado")

        btn_salvar_final = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                  "new UiSelector().text(\"Salvar\")")))
        btn_salvar_final.click()
        Log().info("Salvar final")

        # Finalizar pedido
        btn_finalizar_pedido = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                      "new UiSelector().text(\"Finalizar pedido\")")))
        btn_finalizar_pedido.click()
        Log().info("Finalizar pedido")

        btn_salvar_pedido = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                   "new UiSelector().text(\"Salvar\")")))
        btn_salvar_pedido.click()
        Log().info("Pedido guardado")

        # Verificar finalizadas
        contador_finalizadas = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
                                                                      "new UiSelector().text(\"Finalizadas\n1\")")))
        contador_finalizadas.click()
        Log().info("TC013 Cliente Inadimplente completado")

    # ==================================================
    #                 FIN DEL PEGADO
    # ==================================================
    except Exception as e:  # pragma: no cover
        Log().error(f"No se logró dar click al botón instalar, validar el error: {e}")
        raise


class Test:
    def test_001(self):
        ingreso_app(self)

    def test_002(self):
        configuracion_inicial(self)

    def test_003(self):
        pegar_funcion()

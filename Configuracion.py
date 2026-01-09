from appium import webdriver
from appium.options.common.base import AppiumOptions
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.extensions.android.nativekey import AndroidKey
from selenium.webdriver import ActionChains, Keys
from datetime import datetime, timedelta
from time import strftime

import os
import logging
import random
import time

options = UiAutomator2Options()
options.platform_name = 'Android'
options.platform_version = '10'
options.device_name = 'Android'
options.app_package = 'uy.com.assist.eaf'
options.app_activity = '.MainActivity'
options.automation_name = 'UiAutomator2'
options.auto_grant_permissions = True

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
wait = WebDriverWait(driver, 500)
action = ActionChains(driver)


class Log:
    def __init__(self):
        self.now = strftime("%Y-%m-%d-%H")
        self.logname = os.path.join('{0}.log'.format(self.now))

    def __printconsole(self, level, message):

        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)

        fh = logging.FileHandler(self.logname, 'a', encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        logger.addHandler(fh)
        logger.addHandler(ch)
        if level == 'info':
            logger.info(message)
        elif level == 'debug':
            logger.debug(message)
        elif level == 'warning':
            logger.warning(message)
        elif level == 'error':
            logger.error(message)
        logger.removeHandler(ch)
        logger.removeHandler(fh)
        fh.close()

    def debug(self, message):
        self.__printconsole('debug', message)

    def info(self, message):
        self.__printconsole('info', message)

    def warning(self, message):
        self.__printconsole('warning', message)

    def error(self, message):
        self.__printconsole('error', message)

import os

import pytest
from appium import webdriver

from src.ui.WelcomePageObject import WelcomePageObject


class Platform:
    platform = os.environ.get('PLATFORM')

    PLATFORM_IOS = 'ios'
    PLATFORM_ANDROID = 'android'
    URL = "http://127.0.0.1:4723/wd/hub"

    def get_capabilities_by_platform_env(self):
        if self.platform == self.is_android():
            return self.get_android_desired_capabilites()
        elif self.platform == self.is_ios():
            return self.get_ios_desired_capabilities()
        else:
            raise Exception("Cannot get run platform from env variable. Platform value " + str(self.platform))

    @staticmethod
    def get_android_desired_capabilites():
        desired_capabilities = {
            "platformName": "Android",
            "platformVersion": "11",
            "automationName": "UIAutomator2",
            "deviceName": "TestAndroid",
            "app": "/Users/svasilchenko/PycharmProjects/PythonAppiumAutomation/apks/org.wikipedia.apk",
            "packageName": "org.wikipedia/org.wikipedia.main.MainActivity",
            "appPackage": "org.wikipedia",
            "appActivity": ".main.MainActivity"
        }
        return desired_capabilities

    @staticmethod
    def get_ios_desired_capabilities():
        desired_capabilities = {"platformName": "iOS",
                                "deviceName": "iPhone 13",
                                "platformVersion": "15.2",
                                "app": "/Users/svasilchenko/Desktop/test_appium_java/apks/Wikipedia.app"}
        return desired_capabilities

    def is_android(self):
        return self.PLATFORM_ANDROID

    def is_ios(self):
        return self.PLATFORM_IOS


@pytest.fixture(scope='function')
def driver(request):
    config = Platform()
    driver = webdriver.Remote(config.URL,
                              desired_capabilities=config.get_capabilities_by_platform_env())
    if config.platform == config.is_ios:
        driver = WelcomePageObject(driver)
        # TODO Дописать скип для онбординга IOS

    request.addfinalizer(driver.quit)
    return driver

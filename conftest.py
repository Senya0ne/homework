import os

import pytest
from appium import webdriver


def get_capabilities_by_platform_env():
    platform = os.environ.get('PLATFORM')
    PLATFORM_IOS = 'ios'
    PLATFORM_ANDROID = 'android'

    if platform == PLATFORM_ANDROID:
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
    elif platform == PLATFORM_IOS:
        desired_capabilities = {"platformName": "iOS",
                                "deviceName": "iPhone 13",
                                "platformVersion": "15.2",
                                "app": "/Users/svasilchenko/Desktop/test_appium_java/apks/Wikipedia.app"}
    else:
        raise Exception("Cannot get run platform from env variable. Platform value " + str(platform))
    return desired_capabilities


@pytest.fixture(scope='function')
def driver(request):
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=get_capabilities_by_platform_env())
    request.addfinalizer(driver.quit)
    return driver

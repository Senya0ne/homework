import pytest
from appium import webdriver


@pytest.fixture(scope='session')
def driver(request):
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

    platform = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities)
    request.addfinalizer(platform.quit)
    return platform



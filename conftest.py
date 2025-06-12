import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en", help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option("prefs", {"intl.accept_languages": user_language})
    print(f"Запуск браузера с установленным языком: {user_language}")
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=options)
    yield browser
    print("\nЗакрытие браузера...")
    browser.quit()

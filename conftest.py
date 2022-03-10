import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help='выбор языка')

@pytest.fixture(scope="function")
def browser(request):
#передаем параметр из командной строки в переменную
    user_language = request.config.getoption('language')

    options = Options()

    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
#подставляем язык
    browser = webdriver.Chrome(options=options)
    
    browser.implicitly_wait(3)
    yield browser
    browser.quit()

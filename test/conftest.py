import datetime
from pages import HomePage
from playwright.sync_api import sync_playwright
from pytest import fixture


@fixture(scope='session')
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@fixture(scope='module')
def chrome_browser(get_playwright):
    browser = get_playwright.chromium.launch(headless=False)
    yield browser
    browser.close()


@fixture(scope='class')
def home_page(pytestconfig, chrome_browser):
    page = HomePage(chrome_browser)
    page.open(pytestconfig.rootdir)
    yield page
    page.close()


@fixture(scope='session')
def local_time_zone():
    yield datetime.datetime.now().astimezone().strftime('%z')

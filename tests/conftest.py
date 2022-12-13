import pytest
from selene.support.shared import browser
from selene import command


@pytest.fixture(scope='function', autouse=True)
def open_browser():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.hold_browser_open = True



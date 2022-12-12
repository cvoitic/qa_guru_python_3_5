import pytest
from selene.support.shared import browser
from selene import command


@pytest.fixture(scope='function', autouse=True)
def open_browser():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.config.hold_browser_open = True
    browser.element('#fixedban').perform(command.js.remove)


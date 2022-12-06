import pytest
from selene.support.shared import browser


@pytest.fixture()
def open_browser():
    browser.config.hold_browser_open = True
    browser.config.window_width = 950
    browser.config.window_height = 600
    browser.open('https://duckduckgo.com')
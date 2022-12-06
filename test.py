from selene.support.shared import browser
from selene import be, have


def test_first(open_browser):
    browser.element('[name="q"]').should(be.blank).type('selene yashaka').press_enter()
    browser.element('[id="links"]').should(have.text('Selene - yashaka.github.io'))


def test_negative(open_browser):
    browser.element('[name="q"]').should(be.blank).type('ttttttuuuueee').press_enter()
    browser.element('[id="links"]').should(have.text('результаты не найдены'))
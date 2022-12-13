import os.path
from selene.support.shared import browser
from selene import be, have, command


def test_complete_form(open_browser):
    browser.open('/automation-practice-form')
    browser.element('#fixedban').perform(command.js.remove)
    browser.element('.practice-form-wrapper').should(have.text('Student Registration Form'))

    # WHEN
    browser.element('#firstName').type('Ivan')
    browser.element('#lastName').type('Veselkov')
    browser.element('#userEmail').type('veseloI@test.ru')
    browser.all('[for^=gender-radio]').element_by(have.text('Male')).click()
    browser.element('#userNumber').type('9114477111')
    browser.element('#dateOfBirthInput').perform(command.js.set_value('08-12-2002'))

    browser.element('#subjectsInput').perform(command.js.scroll_into_view)
    browser.element('#subjectsInput').type('English').press_enter()
    browser.all('[for^=hobbies-checkbox]').element_by(have.text('Music')).click()

    import tests
    browser.element('#uploadPicture').set_value(
        os.path.abspath(
            os.path.join(os.path.dirname(tests.__file__), 'resources/1.jpg')
        )
    )

    browser.element('#currentAddress').should(be.blank).type('Mira, 5')
    browser.element('#react-select-3-input').type('Uttar').press_enter()
    browser.element('#react-select-4-input').type('Agra').press_enter()

    browser.element('#submit').perform(command.js.click)

    # THEN
    browser.element('.modal-content').should(have.text('Thanks for submitting the form'))
    browser.element('.table').all('td').even.should(
        have.texts(
            'Ivan Veselkov',
            'veseloI@test.ru',
            'Male',
            '9114477111',
            '12 December,2022',
            'English',
            'Music',
            '1.jpg',
            'Mira, 5',
            'Uttar Pradesh Agra',
        )
    )


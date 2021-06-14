import allure
import pytest
from steps.authorization import Authorization
from steps.common import Common


@allure.feature('Авторизация')
@allure.severity(allure.severity_level.MINOR)
@allure.title("Ввод корректных значений логин/пароль")
@allure.suite("Авторизаций Позитив")
@pytest.mark.parametrize("text, password", [('email@email.ru', 123456)])
@pytest.mark.parametrize("url, lang", [('https://lk.platon.ru/sign_in?locale=ru', 'ru'),
                                       ('https://lk.platon.ru/sign_in?locale=en', 'en')])
@pytest.mark.filterwarnings
def test_1(open_browser_selenoid_without_cookies, text, password, url, lang):
    driver = open_browser_selenoid_without_cookies
    common = Common(driver)
    authorization = Authorization(driver)
    with allure.step(f'Открыть страницу {url}'):
        common.open_url(url)
    with allure.step(f'Ввод почты {text}'):
        authorization.input_email_main(text)
    with allure.step(f'Проверка, что почта {text} ввелась корректно '):
        authorization.check_input_email_main(text)
    with allure.step('Ввод пароля'):
        authorization.input_password(password)
    with allure.step('Нажать на кнопку войти'):
        authorization.click_sign_in(lang)
    with allure.step('Проверка, что авторизация не прошла'):
        authorization.check_error_or_password()


@allure.feature('Авторизация')
@allure.severity(allure.severity_level.MINOR)
@allure.title("Ввод некорректных значения пароль")
@allure.suite("Авторизаций Негатив")
@pytest.mark.parametrize("text", [('email@email.ru')])
@pytest.mark.parametrize("url, lang", [('https://lk.platon.ru/sign_in?locale=ru', 'ru'),
                                       ('https://lk.platon.ru/sign_in?locale=en', 'en')])
@pytest.mark.filterwarnings
def test_2(open_browser_selenoid_without_cookies, text, url, lang):
    driver = open_browser_selenoid_without_cookies
    common = Common(driver)
    authorization = Authorization(driver)
    with allure.step(f'Открыть страницу {url}'):
        common.open_url(url)
    with allure.step(f'Ввод почты {text}'):
        authorization.input_email_main(text)
    with allure.step(f'Проверка, что почта {text} ввелась корректно '):
        authorization.check_input_email_main(text)
    with allure.step('Нажать на кнопку войти'):
        authorization.click_sign_in(lang)
    with allure.step('Проверка, что авторизация не прошла'):
        authorization.check_error_password()


@allure.feature('Авторизация')
@allure.severity(allure.severity_level.MINOR)
@allure.title("Ввод некорректных значения логин")
@allure.suite("Авторизаций Позитив")
@pytest.mark.parametrize("password", [(123456)])
@pytest.mark.parametrize("url, lang", [('https://lk.platon.ru/sign_in?locale=ru', 'ru'),
                                       ('https://lk.platon.ru/sign_in?locale=en', 'en')])
@pytest.mark.filterwarnings
def test_3(open_browser_selenoid_without_cookies, password, url, lang):
    driver = open_browser_selenoid_without_cookies
    common = Common(driver)
    authorization = Authorization(driver)
    with allure.step(f'Открыть страницу {url}'):
        common.open_url(url)
    with allure.step('Ввод пароля'):
        authorization.input_password(password)
    with allure.step('Нажать на кнопку войти'):
        authorization.click_sign_in(lang)
    with allure.step('Проверка, что авторизация не прошла'):
        authorization.check_error_email()


@allure.feature('Восстановление пароля')
@allure.severity(allure.severity_level.MINOR)
@allure.title("Восстановление пароля")
@allure.suite("Восстановление пароля Позитив")
@pytest.mark.parametrize("text", [('email@email.ru')])
@pytest.mark.parametrize("url, lang,text2", [('https://lk.platon.ru/sign_in?locale=ru', 'ru',
                                              'На вашу электронную почту высланы дальнейшие инструкции по восстановлению пароля'),
                                             ('https://lk.platon.ru/sign_in?locale=en', 'en',
                                              'Information about further steps to recover password has been sent to your e-mail')])
@pytest.mark.filterwarnings
def test_4(open_browser_selenoid_without_cookies, text, url, lang,text2):
    driver = open_browser_selenoid_without_cookies
    common = Common(driver)
    authorization = Authorization(driver)
    with allure.step(f'Открыть страницу {url}'):
        common.open_url(url)
    with allure.step('Открыть попап восстановления пароля'):
        authorization.click_forgot()
    with allure.step(f'Ввод почты {text}'):
        authorization.input_email_forgot(text)
    with allure.step(f'Проверка, что почта {text} ввелась корректно '):
        authorization.check_input_email_forgot(text)
    with allure.step('Отправить инструкцию'):
        authorization.click_send_instruction(lang)
    with allure.step('Уведомление, что инструкцию отправилась'):
        common.find_text(text2)

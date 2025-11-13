import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def open_br(browser):
    """Фикстура: выполняет открытие браузера и страницы"""
    browser.get("https://www.saucedemo.com/")
    return browser

def test_valied_data(open_br):
    """"Проверка валидного логина и пароля"""
    username = WebDriverWait(open_br, 10).until(
        EC.presence_of_element_located((By.ID, "user-name"))
    )
    username.send_keys("standard_user")

    password = open_br.find_element(By.ID, "password")
    password.send_keys("secret_sauce")

    login_btn = open_br.find_element(By.ID, "login-button")
    login_btn.click()

    # Проверка, что есть логотип
    header = WebDriverWait(open_br, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "app_logo"))
    )
    assert header.text == "Swag Labs"
    print("✅ Успешная авторизация прошла- проверка с валидным логином и  паролем")

def test_valied_password(open_br):
    """"Проверка с невалидным логином и валидным паролем"""
    username = WebDriverWait(open_br, 10).until(
        EC.presence_of_element_located((By.ID, "user-name"))
    )
    username.send_keys("standard")

    password = open_br.find_element(By.ID, "password")
    password.send_keys("secret_sauce")

    login_btn = open_br.find_element(By.ID, "login-button")
    login_btn.click()

    # Проверка, что появляется сообщение об ошибке
    error_msg = WebDriverWait(open_br, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']"))
    )

    assert error_msg.text == "Epic sadface: Username and password do not match any user in this service"
    print("✅ Проверка с валидным логином и валидным паролем - Ошибка отображается корректно")

def test_valied_login(open_br):
    """Проверка с невалидным паролем"""
    username = WebDriverWait(open_br, 10).until(
        EC.presence_of_element_located((By.ID, "user-name"))
    )
    username.send_keys("standard_user")

    password = open_br.find_element(By.ID, "password")
    password.send_keys("dbkdjh")

    login_btn = open_br.find_element(By.ID, "login-button")
    login_btn.click()

    # Проверка, что появляется сообщение об ошибке
    error_msg = WebDriverWait(open_br, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']"))
    )

    assert error_msg.text == "Epic sadface: Username and password do not match any user in this service"
    print("✅ Проверка с невалидным паролем - Ошибка отображается корректно")


def test_clear_login(open_br):
        """"Проверка с пустым логином и валидным паролем"""
        username = WebDriverWait(open_br, 10).until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        username.send_keys("")

        password = open_br.find_element(By.ID, "password")
        password.send_keys("secret_sauce")

        login_btn = open_br.find_element(By.ID, "login-button")
        login_btn.click()

        # Проверка, что появляется сообщение об ошибке
        error_msg = WebDriverWait(open_br, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']"))
        )

        assert error_msg.text == "Epic sadface: Username is required"
        print("✅ Проверка с пустым логином и валидным паролем - Ошибка отображается корректно")


def test_clear_password(open_br):
    """Проверка с невалидным паролем"""
    username = WebDriverWait(open_br, 10).until(
        EC.presence_of_element_located((By.ID, "user-name"))
    )
    username.send_keys("standard_user")

    password = open_br.find_element(By.ID, "password")
    password.send_keys("")

    login_btn = open_br.find_element(By.ID, "login-button")
    login_btn.click()

    # Проверка, что появляется сообщение об ошибке
    error_msg = WebDriverWait(open_br, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']"))
    )

    assert error_msg.text == "Epic sadface: Password is required"
    print("✅ Проверка с пустым паролем - Ошибка отображается корректно")
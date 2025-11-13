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
def login(browser):
    """Фикстура: выполняет логин и возвращает браузер уже залогиненным"""
    browser.get("https://www.saucedemo.com/")

    username = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "user-name"))
    )
    username.send_keys("standard_user")

    password = browser.find_element(By.ID, "password")
    password.send_keys("secret_sauce")

    login_btn = browser.find_element(By.ID, "login-button")
    login_btn.click()

    return browser
print(" - Успешная авторизация")


def test_login_success(login):
    """Проверка успешного входа"""
    header = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "app_logo"))
    )
    assert header.text == "Swag Labs"
    print(""" - Проверка успешного входа""")


def test_add_to_cart(login):
    """Добавление товара в корзину"""
    add_order = login.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    add_order.click()

    cart_badge = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )
    assert cart_badge.text == "1"
    print(""" - Добавление товара в корзину""")


def test_checkout(login):
    """Полное оформление заказа"""
    # Добавляем товар
    login.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    login.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Checkout
    login.find_element(By.ID, "checkout").click()

    firstname = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.ID, "first-name"))
    )
    firstname.send_keys("Max")

    login.find_element(By.ID, "last-name").send_keys("Kazakov")
    login.find_element(By.ID, "postal-code").send_keys("413605")
    login.find_element(By.ID, "continue").click()
    login.find_element(By.ID, "finish").click()

    # Проверка успешного заказа
    success_msg = WebDriverWait(login, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "complete-header"))
    )
    assert success_msg.text == "Thank you for your order!"
    print(""" - Полное оформление заказа""")


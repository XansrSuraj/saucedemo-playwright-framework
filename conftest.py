import pytest
from pages.inventorypage import InventoryPage
from pages.cartpage import CartPage
import config
from pytest_html import extras
from pages.loginpage import LoginPage


@pytest.fixture
def logged_in_page(page):
    page.goto(config.BASE_URL)
    login = LoginPage(page)
    login.login(config.STANDARD_USER,config.PASSWORD)
    return page


@pytest.fixture
def checkout_ready(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    inventory.add_to_cart()
    inventory.cart_open()
    cart = CartPage(logged_in_page)
    cart.checkout_btn_click()
    return logged_in_page


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = (item.funcargs.get("page")
                or item.funcargs.get("logged_in_page")
                or item.funcargs.get("checkout_ready"))
        if page:
            import os
            os.makedirs("reports/screenshots", exist_ok=True)
            path = f"reports/screenshots/{item.name}.png"
            page.screenshot(path=path)

            # ↓ YE NAYA — screenshot ko report se jodo
            extra = getattr(report, "extras", [])
            extra.append(extras.image(path))
            report.extras = extra


import allure

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = (item.funcargs.get("page")
                or item.funcargs.get("logged_in_page")
                or item.funcargs.get("checkout_ready"))
        if page:
            import os
            os.makedirs("reports/screenshots", exist_ok=True)
            path = f"reports/screenshots/{item.name}.png"
            page.screenshot(path=path)

            # HTML report ke liye (pehle se hai)
            extra = getattr(report, "extras", [])
            extra.append(extras.image(path))
            report.extras = extra

            # ↓ YE NAYA — Allure me screenshot attach karo
            allure.attach(
                page.screenshot(),
                name="screenshot-on-failure",
                attachment_type=allure.attachment_type.PNG
            )














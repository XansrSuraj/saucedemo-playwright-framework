import pytest

from playwright.sync_api import Page, expect

from pages.loginpage import LoginPage

@pytest.mark.smoke
@pytest.mark.login
def test_valid_login_flow(logged_in_page):
    expect(logged_in_page).to_have_url("https://www.saucedemo.com/inentory.html")

    


@pytest.mark.login
def test_invalid_login_flow(page:Page):
    page.goto("https://www.saucedemo.com/")
    invalid_login = LoginPage(page)
    invalid_login.login("standard_user","sdfghjk")
    expect(invalid_login.error_message).to_contain_text("Epic sadface: Username and password do not match any user in this service")




































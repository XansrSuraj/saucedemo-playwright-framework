from playwright.sync_api import Page , expect


class LoginPage:
    def __init__(self,page:Page):
        self.page = page
        self.username_input = self.page.get_by_placeholder("Username")
        self.password_input = self.page.get_by_placeholder("Password")
        self.login_btn = self.page.locator("#login-button")
        self.error_message = self.page.locator("[data-test='error']")


    def login(self,username,password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_btn.click()


        









































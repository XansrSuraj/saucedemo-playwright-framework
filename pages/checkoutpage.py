from playwright.sync_api import Page , expect


class CheckOutPage:
    def __init__(self,page:Page):
        self.page = page
        self.first_name = self.page.get_by_role("textbox", name="First Name")
        self.last_name = self.page.get_by_role("textbox", name="Last Name")
        self.postal_code = self.page.get_by_role("textbox", name="Zip/Postal Code")
        self.proceed = self.page.locator("[data-test='continue']")
        self.error_message = self.page.locator("[data-test='error']")




    def fill_info(self,firstname,lastname,zip):
        self.first_name.fill(firstname)
        self.last_name.fill(lastname)
        self.postal_code.fill(zip)
        self.proceed.click()

    def continue_btn_click(self):
        self.proceed.click()



class CheckoutOverview:
    def __init__(self,page:Page):
        self.page = page
        self.overview_product = self.page.get_by_text("Sauce Labs Backpack", exact=True)
        self.finish_btn = self.page.get_by_role("button", name="Finish")



    def finish_btn_click(self):
        self.finish_btn.click()

        



        




































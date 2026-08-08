from playwright.sync_api import Page,expect

class CheckoutComplete:
    def __init__(self,page:Page):
        self.page = page
        self.thank_you = self.page.get_by_role("heading", name="Thank you for your order!")

        
        



























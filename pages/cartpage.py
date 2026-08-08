from playwright.sync_api import Page , expect


class CartPage:
    def __init__(self,page:Page):
        self.page = page
        self.item_name = self.page.locator(".inventory_item_name")
        self.remove_item = self.page.get_by_role("button", name="Remove")
        self.continue_shopping = self.page.get_by_role("button", name="Continue Shopping")
        self.checkout_btn = self.page.get_by_role("button", name="Checkout")

                

    def continue_to_product_page(self):
        self.continue_shopping.click()


    def remove_item_from_cart(self):
        self.remove_item.click()


    def checkout_btn_click(self):
        self.checkout_btn.click()
        

































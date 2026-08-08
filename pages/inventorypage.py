from playwright.sync_api import Page,expect

class InventoryPage:
    def __init__(self,page:Page):
        self.page = page
        self.backpack = self.page.locator("#add-to-cart-sauce-labs-backpack")
        self.inventory_item = self.page.locator(".inventory_item")
        self.badge = self.page.locator(".shopping_cart_badge")
        self.remove_badge = self.page.locator("#remove-sauce-labs-backpack")
        self.sort_dropdown = self.page.locator(".product_sort_container")
        self.item_names = self.page.locator(".inventory_item_name")
        self.open_cart = self.page.locator(".shopping_cart_link")





    def add_to_cart(self):
        self.backpack.click()

    def remove_cart_item(self):
        self.remove_badge.click()

    def sort_by(self,value):
        self.sort_dropdown.select_option(value)

    def cart_open(self):
        self.open_cart.click()
        





















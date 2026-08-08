import pytest

from playwright.sync_api import Page,expect


from pages.inventorypage import InventoryPage
from pages.cartpage import CartPage


def test_check_cart_item_is_right(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    inventory.add_to_cart()
    inventory.cart_open()
    cart = CartPage(logged_in_page)
    expect(cart.item_name).to_have_text("Sauce Labs Backpack")
    

def test_continue_to_product_page(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    inventory.add_to_cart()
    inventory.cart_open()
    cart = CartPage(logged_in_page)
    cart.continue_to_product_page()
    expect(logged_in_page).to_have_url("https://www.saucedemo.com/inventory.html")


def test_remove_cart_item(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    inventory.add_to_cart()
    inventory.cart_open()
    cart = CartPage(logged_in_page)
    cart.remove_item_from_cart()
    expect(inventory.badge).to_have_count(0)



















































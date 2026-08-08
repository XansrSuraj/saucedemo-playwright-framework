import pytest

from playwright.sync_api import Page, expect

from pages.cartpage import CartPage
from pages.checkoutpage import CheckOutPage
from pages.inventorypage import InventoryPage
from pages.checkoutpage import CheckoutOverview
from pages.checkoutcomplete import CheckoutComplete

def test_valid_info(logged_in_page):
    firstname = "sourabh"
    lastname = "shinde"
    zip = "2200901"
    inventory = InventoryPage(logged_in_page)
    inventory.add_to_cart()
    inventory.cart_open()
    cart = CartPage(logged_in_page)
    cart.checkout_btn_click()
    checkout = CheckOutPage(logged_in_page)
    checkout.fill_info(firstname,lastname,zip)

   
def test_miss_first_name(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    inventory.add_to_cart()
    inventory.cart_open()
    cart = CartPage(logged_in_page)
    cart.checkout_btn_click()
    checkout = CheckOutPage(logged_in_page)
    checkout.fill_info("","shinde","234455")
    expect(checkout.error_message).to_have_text("Error: First Name is required")


def test_miss_zip_code(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    inventory.add_to_cart()
    inventory.cart_open()
    cart = CartPage(logged_in_page)
    cart.checkout_btn_click()
    checkout = CheckOutPage(logged_in_page)
    checkout.fill_info("sourabh","shinde","")
    expect(checkout.error_message).to_have_text("Error: Postal Code is required")
    
    
def test_complete_order(checkout_ready):
   
    checkout = CheckOutPage(checkout_ready)
    checkout.fill_info("Sourabh","Shinde","23456")
    checkoutoverview = CheckoutOverview(checkout_ready)
    checkoutoverview.finish_btn_click()
    ckcomplete = CheckoutComplete(checkout_ready)
    
@pytest.mark.smoke
@pytest.mark.checkout
def test_complete_order_thanyou(checkout_ready):
   
    checkout = CheckOutPage(checkout_ready)
    checkout.fill_info("Sourabh","Shinde","23456")
    checkoutoverview = CheckoutOverview(checkout_ready)
    checkoutoverview.finish_btn_click()
    ckcomplete = CheckoutComplete(checkout_ready)
    expect(ckcomplete.thank_you).to_be_visible()




































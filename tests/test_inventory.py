from playwright.sync_api import expect, Page
import pytest

from pages.inventorypage import InventoryPage


@pytest.mark.checkout
def test_six_product_shown(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    expect(inventory.inventory_item).to_have_count(6)

@pytest.mark.smoke
def test_add_to_cart(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    inventory.add_to_cart()
    expect(inventory.badge).to_contain_text("1")

@pytest.mark.checkout
def test_remove_cart_item(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    inventory.add_to_cart()
    inventory.remove_cart_item()
    expect(inventory.badge).to_have_count(0)

@pytest.mark.checkout
def test_sort_items(logged_in_page):
    inventory = InventoryPage(logged_in_page)
    inventory.sort_by("za")
    expect(inventory.item_names.first).to_have_text(
    "Test.allTheThings() T-Shirt (Red)"
)























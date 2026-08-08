# 🛒 SauceDemo E-Commerce Automation Framework

An **End-to-End Test Automation Framework** built using **Playwright and Pytest** to test the complete e-commerce workflow of [SauceDemo](https://www.saucedemo.com/) — from **user login to successful order completion**.

The framework follows the **Page Object Model (POM)** design pattern, making the test code clean, reusable, and easy to maintain.

---

## 🛠️ Tech Stack

| Technology                     | Purpose                                |
| ------------------------------ | -------------------------------------- |
| 🐍 **Python**                  | Programming Language                   |
| 🎭 **Playwright**              | Browser Automation                     |
| 🧪 **Pytest**                  | Test Runner                            |
| 📦 **Page Object Model (POM)** | Framework Design Pattern               |
| 📊 **Allure Report**           | Detailed Test Reporting                |
| 📄 **Pytest HTML**             | HTML Test Reports                      |
| 📸 **Screenshots**             | Captured automatically on test failure |
| 🔍 **Playwright Trace**        | Step-by-step debugging                 |

---

## ✨ Key Features

* ✅ **Page Object Model (POM)** — Each page has a separate class for better code organization and maintenance.
* ✅ **Reusable Pytest Fixtures** — Common setup such as login and checkout can be reused across tests.
* ✅ **Centralized Configuration** — URLs and login credentials are managed from one place.
* ✅ **Pytest Markers** — Run specific test suites such as `smoke`, `login`, or `checkout`.
* ✅ **Allure Reports** — Generate detailed and interactive test reports.
* ✅ **HTML Reports** — Generate simple HTML reports for quick test result analysis.
* ✅ **Automatic Screenshots** — Screenshots are captured whenever a test fails.
* ✅ **Playwright Trace** — Helps debug failed tests by showing each browser action step by step.

---

## 📁 Project Structure

```text
saucedemo/
│
├── pages/                      # Page Object classes
│   ├── loginpage.py
│   ├── inventorypage.py
│   ├── cartpage.py
│   ├── checkoutpage.py
│   └── checkoutcomplete.py
│
├── tests/                      # Test cases organized by feature
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_cart.py
│   └── test_checkout.py
│
├── conftest.py                 # Fixtures and screenshot hooks
├── config.py                   # URLs and credentials
├── pytest.ini                  # Pytest settings and markers
└── requirements.txt            # Project dependencies
```

---

## 🚀 Setup & Installation

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
playwright install
```

### 2️⃣ Run All Tests

```bash
pytest
```

### 3️⃣ Run Smoke Tests Only

```bash
pytest -m smoke
```

### 4️⃣ Generate Allure Report

Run the tests and save the Allure results:

```bash
pytest --alluredir=allure-results
```

Open the Allure report:

```bash
allure serve allure-results
```

---

## 📊 Test Coverage

### 🔐 Login

* Valid user login
* Invalid username or password validation

### 🛍️ Inventory

* Verify product count
* Add products to cart
* Remove products
* Verify product sorting

### 🛒 Cart

* Verify added items
* Remove items from cart
* Continue shopping functionality

### 💳 Checkout

* Checkout form validation
* Customer information flow
* Order overview
* Successful order completion

---

## 🔄 E-Commerce Test Flow

```text
Login
  ↓
Inventory
  ↓
Add Product to Cart
  ↓
Cart Verification
  ↓
Checkout
  ↓
Customer Information
  ↓
Order Overview
  ↓
Order Complete ✅
```

---

## 🎯 Framework Goals

This project demonstrates how to build a **scalable and maintainable UI automation framework** using modern testing tools.

It focuses on:

* Clean and reusable test code
* Easy test maintenance
* Reliable end-to-end testing
* Better failure debugging
* Clear test reporting

---

## 👤 Author

**Suraj**

---

⭐ If you find this project useful, feel free to **star the repository**!

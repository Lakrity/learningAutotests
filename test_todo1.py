import pytest
import pytest_playwright
from playwright.sync_api import Playwright, sync_playwright, expect


def test_add_todo(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_role("textbox", name="What needs to be done?").click()
    page.get_by_role("textbox", name="What needs to be done?").fill("Hello World!")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    page.get_by_role("link", name="Active").click()
    page.get_by_role("checkbox", name="Toggle Todo").click()
    page.goto("https://demo.playwright.dev/todomvc/#/completed")
    page.get_by_role("button", name="Delete").click()

    # ---------------------
    context.close()
    browser.close()



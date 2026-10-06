import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
	sys.path.insert(0, str(ROOT))

from playwright.sync_api import expect, sync_playwright

from Dash_Navigation.Dashboard import Dashb


def test_radio_button_functionality(page):
	Dashb(page)
	Dashb.Radio_Button(page)

	yes = page.get_by_text("Yes", exact=True).first
	impressive = page.get_by_text("Impressive", exact=True).first
	no = page.get_by_text("No", exact=True).first

	expect(yes).to_be_visible()
	expect(page.locator("#yesRadio")).to_be_enabled()
	yes.click()
	expect(page.locator("#yesRadio")).to_be_checked()
	expect(page.locator(".text-success")).to_have_text("Yes")

	expect(impressive).to_be_visible()
	expect(page.locator("#impressiveRadio")).to_be_enabled()
	impressive.click()
	expect(page.locator("#impressiveRadio")).to_be_checked()
	expect(page.locator(".text-success")).to_have_text("Impressive")

	expect(no).to_be_visible()
	expect(page.locator("#noRadio")).to_be_disabled()

	

if __name__ == "__main__":
	with sync_playwright() as playwright:
		browser = playwright.chromium.launch(headless=False)
		try:
			page = browser.new_page()
			try:
				test_radio_button_functionality(page)
				print("\033[92mTest completed successfully\033[0m")
			except Exception:
				print("\033[91mTest failed\033[0m")
				raise
		finally:
			browser.close()
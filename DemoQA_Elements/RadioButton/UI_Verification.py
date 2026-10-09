import sys
from pathlib import Path

sys.dont_write_bytecode = True

from playwright.sync_api import expect, sync_playwright

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
	sys.path.insert(0, str(ROOT))

from Dash_Navigation.Dashboard import Dashb


def test_radio_button_ui(page):
	Dashb(page)
	Dashb.Radio_Button(page)

	expect(page.get_by_text("Do you like the site?", exact=True)).to_be_visible()

	yes_radio = page.get_by_label("Yes", exact=True)
	impressive_radio = page.get_by_label("Impressive", exact=True)
	no_radio = page.get_by_label("No", exact=True)

	expect(yes_radio).to_be_visible()
	expect(impressive_radio).to_be_visible()
	expect(no_radio).to_be_visible()
	expect(no_radio).to_be_disabled()

	for label, radio in [
		("Yes", yes_radio),
		("Impressive", impressive_radio),
	]:
		radio.check()
		expect(page.get_by_text("You have selected", exact=False)).to_be_visible()
		expect(page.locator(".text-success")).to_contain_text(label)

	return True


if __name__ == "__main__":
	with sync_playwright() as playwright:
		browser = playwright.chromium.launch(headless=False)
		try:
			page = browser.new_page()
			try:
				test_radio_button_ui(page)
				print("\033[92mTest completed successfully\033[0m")
			except Exception:
				print("\033[91mTest failed\033[0m")
				raise
		finally:
			browser.close()

"""For Update"""
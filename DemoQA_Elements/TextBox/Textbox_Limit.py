import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

project_root = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(project_root))

from Dash_Navigation.Dashboard import Dashb


def main():
	with sync_playwright() as playwright:
		browser = playwright.chromium.launch(headless=False)
		try:
			page = browser.new_page()
			dashboard = Dashb(page)
			dashboard.Text_Box(page)
			fields = {
				"Full Name": page.locator("#userName"),
				"Email": page.locator("#userEmail"),
				"Current Address": page.locator("#currentAddress"),
				"Permanent Address": page.locator("#permanentAddress"),
			}

			for name, element in fields.items():
				maximum = element.get_attribute("maxlength")
				if maximum is None:
					value = "\033[91mnot specified\033[0m"
				else:
					value = f"\033[92m{maximum}\033[0m"
				print(f"{name} maximum limit: {value}")
		finally:
			browser.close()


if __name__ == "__main__":
	main()

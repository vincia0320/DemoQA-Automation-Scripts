import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

# Make the project root available when this script is run directly.
project_root = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(project_root))

from Dash_Navigation.Dashboard import Dashb


with sync_playwright() as playwright:
	browser = playwright.chromium.launch(headless=False)
	try:
		page = browser.new_page()
		dashboard = Dashb(page)
		text_box = dashboard.Text_Box(page)
		full_name = "Test321"
		email = "Test@gmail.com"
		current_address = "District Imus"
		permanent_address = "Vista Mall Dasmarinas"
		page.locator("#userName").fill(full_name)
		page.locator("#userEmail").fill(email)
		page.locator("#currentAddress").fill(current_address)
		page.locator("#permanentAddress").fill(permanent_address)
		page.get_by_role("button", name="Submit").click()
		result_text = page.locator("#output").inner_text()
		expected_details = (
			f"Name:{full_name}",
			f"Email:{email}",
			f"Current Address :{current_address}",
			f"Permananet Address :{permanent_address}",
		)
		assert all(detail in result_text for detail in expected_details), (
			f"Submitted details were missing from the result: {result_text}"
		)
		print("Test completed successfully")

	finally:
		browser.close()
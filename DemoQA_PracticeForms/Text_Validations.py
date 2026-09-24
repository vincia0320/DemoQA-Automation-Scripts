"""UI validation for the DemoQA Practice Form.

Run with: pytest Text_Validations-V2.py
"""

from pathlib import Path

import pytest
from playwright.sync_api import Page, expect, sync_playwright


FORM_URL = "https://demoqa.com/automation-practice-form"


def smart_wait(page: Page, locator, state="visible"):
	"""Wait for a control using Playwright's built-in, condition-based wait."""
	page.locator(locator).wait_for(state=state)


@pytest.fixture
def page():
	with sync_playwright() as playwright:
		browser = playwright.chromium.launch(headless=False)
		context = browser.new_context(viewport=None)
		page = context.new_page()
		page.goto(FORM_URL, wait_until="domcontentloaded")
		smart_wait(page, "#firstName")
		yield page
		context.close()
		browser.close()


def test_practice_form_controls(page: Page, tmp_path):
	fields = {
		"firstName": "Alvin",
		"lastName": "Tester",
		"userEmail": "alvin.tester@example.com",
		"userNumber": "9876543210",
		"currentAddress": "123 Test Street",
	}
	for element_id, value in fields.items():
		element = page.locator(f"#{element_id}")
		expect(element).to_be_visible()
		expect(element).to_be_enabled()
		element.fill(value)
		expect(element).to_have_value(value)

	for input_id in ("gender-radio-1", "hobbies-checkbox-1"):
		label = page.locator(f"label[for='{input_id}']")
		label.wait_for(state="visible")
		label.click()
		expect(page.locator(f"#{input_id}")).to_be_checked()

	upload_file = Path(tmp_path) / "demoqa-upload.txt"
	upload_file.write_text("upload validation", encoding="utf-8")
	upload = page.locator("#uploadPicture")
	expect(upload).to_be_enabled()
	upload.set_input_files(str(upload_file.resolve()))
	expect(upload).to_have_value("C:\\fakepath\\demoqa-upload.txt")

	# State and City are searchable custom dropdowns on DemoQA. Verify that
	# every available state can be selected, along with every city it exposes.
	state = page.locator("#state")
	state_options = page.locator("div[id*='state-option']")
	state.click()
	state_names = state_options.all_text_contents()

	for state_name in state_names:
		state.click()
		state_options.filter(has_text=state_name).first.click()
		expect(state).to_contain_text(state_name)

		city = page.locator("#city")
		city.click()
		city_options = page.locator("div[id*='city-option']")
		city_names = city_options.all_text_contents()
		for city_name in city_names:
			city.click()
			city_options.filter(has_text=city_name).first.click()
			expect(city).to_contain_text(city_name)

	submit = page.locator("#submit")
	expect(submit).to_be_enabled()
	submit.scroll_into_view_if_needed()
	submit.click()
	smart_wait(page, "#example-modal-sizes-title-lg")
	expect(page.locator("#example-modal-sizes-title-lg")).to_be_visible()

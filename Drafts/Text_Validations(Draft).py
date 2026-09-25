"""Playwright validations for the DemoQA Practice Form.

Run with: pytest -q Text_Validations.py
"""

from pathlib import Path
import re

import pytest
from playwright.sync_api import Page, expect


FORM_URL = "https://demoqa.com/automation-practice-form"
NOTE_FILE = Path(__file__).parent / "validation_failure.txt"
PICTURE = r"C:\Users\alvin\Downloads\tachiyomi-en.mangade-v1.4.1.apk"


def _check(item: str, action) -> None:
	try:
		action()
	except Exception as error:
		NOTE_FILE.write_text(
			f"Validation failed: {item}\n{error}\n", encoding="utf-8"
		)
		pytest.fail(f"{item}: {error}", pytrace=False)


def test_practice_form_validations(page: Page) -> None:
	page.goto(FORM_URL, wait_until="domcontentloaded")
	page.locator("#firstName").scroll_into_view_if_needed()

	def names():
		page.locator("#firstName").fill("Alvin")
		page.locator("#lastName").fill("Tester")
		expect(page.locator("#firstName")).to_have_value("Alvin")
		expect(page.locator("#lastName")).to_have_value("Tester")

	_check("1. First name and last name accept strings", names)

	def email():
		field = page.locator("#userEmail")
		field.fill("example@example.com")
		expect(field).to_have_value("example@example.com")
		assert re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", field.input_value())

	_check("2. Email accepts example@example.com", email)
	_check("3. Male radio button is selectable", lambda: page.locator("#gender-radio-1").check())

	def mobile():
		field = page.locator("#userNumber")
		field.fill("1234567890")
		expect(field).to_have_value("1234567890")
		assert re.fullmatch(r"\d{10}", field.input_value())

	_check("4. Mobile accepts only 10-digit integers", mobile)

	def date():
		field = page.locator("#dateOfBirthInput")
		field.fill("15 Jan 2024")
		expect(field).to_have_value("15 Jan 2024")
		value = field.input_value()
		assert re.fullmatch(r"\d{2} [A-Za-z]{3} \d{4}", value)
		assert value[:2].isdigit() and value[3:6].isalpha() and value[7:].isdigit()

	_check("5-8. Date uses DD MMM YYYY with valid component types", date)

	def subjects():
		field = page.locator("#subjectsInput")
		field.fill("Maths")
		option = page.locator(".subjects-auto-complete__option").filter(has_text="Maths").first
		expect(option).to_be_visible()
		option.click()
		expect(page.locator(".subjects-auto-complete__multi-value__label")).to_contain_text("Maths")

	_check("9. Subjects accepts an available choice", subjects)

	def hobbies():
		page.locator("#hobbies-checkbox-1").check()
		page.locator("#hobbies-checkbox-2").check()
		expect(page.locator("#hobbies-checkbox-1")).to_be_checked()
		expect(page.locator("#hobbies-checkbox-2")).to_be_checked()

	_check("10. Multiple hobbies can be checked", hobbies)
	_check("11. Picture uploads the requested file", lambda: page.locator("#uploadPicture").set_input_files(PICTURE))
	_check("12. Address accepts string values", lambda: page.locator("#currentAddress").fill("123 DemoQA Street"))

	def state_city():
		page.locator("#state").click()
		page.get_by_text("NCR", exact=True).click()
		page.locator("#city").click()
		page.get_by_text("Delhi", exact=True).click()

	_check("13. State and city dropdown items are selectable", state_city)
	_check("Submit form", lambda: page.locator("#submit").click())
	NOTE_FILE.unlink(missing_ok=True)

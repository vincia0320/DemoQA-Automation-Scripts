import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

project_root = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(project_root))

from Dash_Navigation.Dashboard import Dashb


def verify_character_acceptance(page):
	"""Fill the DemoQA text boxes and check retained characters and email validity."""
	Dashb(page)
	Dashb.Text_Box(page)

	inputs = {
		"Full Name": ("#userName", "Alvin O'Neil-Smith 123"),
		"Email": ("#userEmail", "alvin.test+demo@example.com"),
		"Current Address": ("#currentAddress", "123 Main St., Apt #4-B; O'Neil's place!"),
		"Permanent Address": ("#permanentAddress", "45 Oak Rd., Unit 2 / Building A"),
	}

	for label, (selector, value) in inputs.items():
		field = page.locator(selector)
		field.fill(value)
		assert field.input_value() == value, f"{label} did not retain the entered characters"
		character_types = []
		if any(character.isalpha() for character in value):
			character_types.append("letters")
		if any(character.isdigit() for character in value):
			character_types.append("numbers")
		if any(not character.isalnum() and not character.isspace() for character in value):
			character_types.append("special characters")
		if any(character.isspace() for character in value):
			character_types.append("spaces")
		print(f"{label} accepts: {', '.join(character_types)}")

	email = page.locator("#userEmail")
	email.fill("not-an-email")
	page.get_by_role("button", name="Submit").click()
	assert "field-error" in (email.get_attribute("class") or ""), (
		"Email must be in local-part@domain format (for example, name@example.com)"
	)
	print("Email validation rejected an invalid email")


def main():
	with sync_playwright() as playwright:
		browser = playwright.chromium.launch(headless=False)
		try:
			page = browser.new_page()
			verify_character_acceptance(page)
			print("\033[92mTest completed successfully\033[0m")
		finally:
			browser.close()


if __name__ == "__main__":
	main()

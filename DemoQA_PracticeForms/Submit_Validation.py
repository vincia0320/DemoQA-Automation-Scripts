from pathlib import Path
from playwright.sync_api import expect, sync_playwright
from openpyxl import load_workbook


BASE = Path(__file__).resolve().parent
PROJECT_ROOT = BASE.parent


def get_input_file() -> Path:
    candidates = [
        BASE / "Forms Uploader.xlsx",
        PROJECT_ROOT / "Forms Uploader.xlsx",
    ]

    for path in candidates:
        if path.is_file():
            return path

    matches = list(PROJECT_ROOT.rglob("Forms Uploader.xlsx"))
    if matches:
        return matches[0]

    raise FileNotFoundError(
        "Could not find 'Forms Uploader.xlsx'. "
        f"Place it in:\n{BASE}\nor\n{PROJECT_ROOT}"
    )


def first_value(row, *names):
	values = {str(k).strip().lower(): v for k, v in row.items() if k is not None}
	for name in names:
		value = values.get(name.lower())
		if value not in (None, ""):
			return str(value)
	return ""


def main():
	input_file = get_input_file()
	workbook = load_workbook(input_file, data_only=True)
	sheet = workbook.active
	headers = [cell.value for cell in sheet[1]]
	row = dict(zip(headers, next(sheet.iter_rows(min_row=2, max_row=2, values_only=True))))
	with sync_playwright() as playwright:
		browser = playwright.chromium.launch(headless=False)
		page = browser.new_page()
		page.goto("https://demoqa.com/automation-practice-form", wait_until="domcontentloaded")

		fields = {
			"firstName": ("firstName", "first name"),
			"lastName": ("lastName", "last name"),
			"userEmail": ("email", "user email"),
			"userNumber": ("mobile", "mobile number", "phone"),
			"currentAddress": ("address", "current address"),
		}
		for element_id, names in fields.items():
			value = first_value(row, *names)
			if value:
				page.locator(f"#{element_id}").fill(value)

		gender = first_value(row, "gender")
		if gender:
			page.locator(f"label:text-is('{gender}')").click()

		subjects = first_value(row, "subjects", "subject")
		if subjects:
			subject_input = page.locator("#subjectsInput")
			subject_input.fill(subjects)
			subject_input.press("Enter")

		for element_id in ("state", "city"):
			value = first_value(row, element_id)
			if value:
				# Open the exact State/City control, then select the exact matching entry.
				page.locator(f"#{element_id}").click()
				page.get_by_text(value, exact=True).click()

		page.locator("#submit").click()
		modal = page.locator("#example-modal-sizes-title-lg").locator("xpath=ancestor::div[contains(@class, 'modal-content')]")
		expect(modal).to_be_visible()
		actual = {
			cells.nth(0).inner_text().strip(): cells.nth(1).inner_text().strip()
			for cells in [modal.locator("tr").nth(i).locator("td") for i in range(modal.locator("tr").count())]
			if cells.count() >= 2
		}
		expected = f"{first_value(row, 'first name', 'firstname')} {first_value(row, 'last name', 'lastname')}".strip()
		if actual.get("Student Name") != expected:
			raise AssertionError(f"Modal mismatch: expected Student Name={expected}, got {actual}")
		print("Submit validation passed")
		browser.close()


if __name__ == "__main__":
	main()

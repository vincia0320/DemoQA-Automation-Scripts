import unittest

from playwright.sync_api import sync_playwright


EXPECTED_LABELS = {
    "Student Name",
    "Student Email",
    "Gender",
    "Mobile",
    "Date of Birth",
    "Subjects",
    "Hobbies",
    "Picture",
    "Address",
    "State and City",
}


class SubmitUITest(unittest.TestCase):
    def test_required_labels_are_displayed(self):
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=False)
            page = browser.new_page()

            try:
                page.goto("https://demoqa.com/automation-practice-form")

                page.locator("#firstName").fill("Alvin")
                page.locator("#lastName").fill("Tester")
                page.locator("#userEmail").fill("alvin.tester@example.com")
                page.locator("#userNumber").fill("9876543210")
                page.locator("label[for='gender-radio-1']").click()

                page.locator("#submit").scroll_into_view_if_needed()
                page.locator("#submit").click(force=True)

                modal = page.locator(".modal-content")
                modal.wait_for(state="visible")

                rows = modal.locator("tbody tr")
                displayed_labels = {
                    rows.nth(index).locator("td").first.inner_text().strip()
                    for index in range(rows.count())
                }

                missing_labels = EXPECTED_LABELS - displayed_labels

                self.assertFalse(
                    missing_labels,
                    f"Labels missing from the submission modal: "
                    f"{sorted(missing_labels)}",
                )
            finally:
                browser.close()


if __name__ == "__main__":
    unittest.main()
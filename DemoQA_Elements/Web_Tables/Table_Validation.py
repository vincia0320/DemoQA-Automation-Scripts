import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from playwright.sync_api import expect, sync_playwright
from Dash_Navigation.Dashboard import Dashb


class Table_Validation:
    def __init__(self, page):
        self.page = page
        self.web_tables = Dashb.Web_Tables(page)

    def verify_table_columns_displayed(self):
        expected_headers = [
            "First Name",
            "Last Name",
            "Age",
            "Email",
            "Salary",
            "Department",
            "Action",
        ]

        for header in expected_headers:
            expect(
                self.page.get_by_role("columnheader", name=header, exact=True)
            ).to_be_visible()


def run_test():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        try:
            page = browser.new_page()
            page.goto("https://demoqa.com/webtables", wait_until="domcontentloaded")

            test = Table_Validation(page)
            test.verify_table_columns_displayed()
            try:
                Table_Validation(page)
                print("\033[92mTest completed successfully\033[0m")
            except Exception:
                print("\033[91mTest failed\033[0m")
                raise
        finally:
            browser.close()


if __name__ == "__main__":
    run_test()


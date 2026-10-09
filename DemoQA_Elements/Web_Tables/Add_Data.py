import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from playwright.sync_api import expect, sync_playwright
from Dash_Navigation.Dashboard import Dashb

class AddTableData:
    def __init__(self, page):
        self.page = page
        self.web_tables = Dashb.Web_Tables(page)

    def add_data(self, first_name, last_name, email, age, salary, department):
        self.page.locator("#addNewRecordButton").click()
        self.page.locator("#firstName").fill(first_name)
        self.page.locator("#lastName").fill(last_name)
        self.page.locator("#userEmail").fill(email)
        self.page.locator("#age").fill(str(age))
        self.page.locator("#salary").fill(str(salary))
        self.page.locator("#department").fill(department)
        self.page.locator("#submit").click()

    def test_add_random_data(self):
        self.web_tables = Dashb.Web_Tables(self.page)
        token = "".join(random.choices(string.ascii_lowercase + string.digits, k=8))
        self.add_data(
            first_name=f"First{token[:4]}",
            last_name=f"Last{token[4:]}",
            email=f"{token}@example.com",
            age=random.randint(18, 65),
            salary=random.randint(30000, 150000),
            department="Testing",
        )


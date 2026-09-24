from playwright.sync_api import sync_playwright


class DemoQASiteAccess:
    def __init__(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()

    def open_forms_page(self):
        self.page.goto("https://demoqa.com/forms", wait_until="networkidle")
        return self.page

    def close(self):
        self.browser.close()
        self.playwright.stop()


if __name__ == "__main__":
    site = DemoQASiteAccess()
    site.open_forms_page()
    site.close()

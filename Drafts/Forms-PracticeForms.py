from playwright.sync_api import sync_playwright

import importlib.util
from pathlib import Path


def run():
	dashboard_path = Path(__file__).with_name("Dashboard.py")
	spec = importlib.util.spec_from_file_location("dashboard", dashboard_path)
	if spec is None or spec.loader is None:
		raise ImportError(f"Unable to load {dashboard_path}")

	dashboard = importlib.util.module_from_spec(spec)
	spec.loader.exec_module(dashboard)

	with sync_playwright() as playwright:
		browser = playwright.chromium.launch(headless=False)
		page = browser.new_page()
		page.goto("https://demoqa.com/")
		page.get_by_text("Forms", exact=True).click()
		page.get_by_text("Practice Form", exact=True).click()
		page.wait_for_load_state("domcontentloaded")
		input("Practice Form opened. Press Enter to close the browser...")
		browser.close()


if __name__ == "__main__":
	run()




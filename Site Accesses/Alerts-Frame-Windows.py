import subprocess
import sys

from playwright.sync_api import sync_playwright


def main():
	# Open the DemoQA dashboard first.
	subprocess.run(
		[sys.executable, "Dashboard.py"],
		cwd=r"c:\Users\alvin\Desktop\DemoQA (Python)\Site Accesses",
		check=True,
	)

	with sync_playwright() as playwright:
		browser = playwright.chromium.launch(headless=False)
		page = browser.new_page()
		page.goto("https://demoqa.com/")
		page.get_by_text("Alerts, Frame & Windows", exact=True).click()
		page.wait_for_url("**/alertsWindows")


if __name__ == "__main__":
	main()

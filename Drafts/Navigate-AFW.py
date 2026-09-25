import Dashboard
import subprocess
import sys
from pytest import Class
from playwright.sync_api import sync_playwright


class NavigateAFW:
	def __init__(self):
		self.page = Dashboard.DemoQASiteAccess().open_dashboard_page()
		self.page.get_by_text("Alerts, Frame & Windows", exact=True).click()

if __name__ == "__main__":
	browser_windows = NavigateAFW()
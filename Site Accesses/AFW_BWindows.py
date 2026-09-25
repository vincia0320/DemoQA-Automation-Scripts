from Dashboard import DemoQASiteAccess

def main():
	page = DemoQASiteAccess().open_dashboard_page()
	page.get_by_text("Alerts, Frame & Windows", exact=True).click()
	page.get_by_text("Browser Windows", exact=True).click()
	page.wait_for_url("**/alertsWindows")


if __name__ == "__main__":
	main()

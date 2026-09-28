from playwright.sync_api import Page


class Dashb:
	"""Dashboard navigation and page-object classes."""
	def __init__(self, page: Page):
		self.page = page
		self.page.goto("https://demoqa.com/", wait_until="domcontentloaded")

	class Text_Box:
		def __init__(self, page: Page):
			self.page = page
			self.page.get_by_text("Elements", exact=True).click()
			self.page.get_by_text("Text Box", exact=True).first.click()

	class Check_Box:
		def __init__(self, page: Page):
			self.page = page
			self.page.get_by_text("Elements", exact=True).click()
			self.page.get_by_text("Check Box", exact=True).first.click()

	class Radio_Button:
		def __init__(self, page: Page):
			self.page = page
			self.page.get_by_text("Elements", exact=True).click()
			self.page.get_by_text("Radio Button", exact=True).first.click()

	class Web_Tables:
		def __init__(self, page: Page):
			self.page = page
			self.page.get_by_text("Elements", exact=True).click()
			self.page.get_by_text("Web Tables", exact=True).first.click()

	class Buttons:
		def __init__(self, page: Page):
			self.page = page
			self.page.get_by_text("Elements", exact=True).click()
			self.page.get_by_text("Buttons", exact=True).first.click()

	class E_Links:
		def __init__(self, page: Page):
			self.page = page
			self.page.get_by_text("Elements", exact=True).click()
			self.page.get_by_text("Links", exact=True).first.click()

	class Broken_Links:
		def __init__(self, page: Page):
			self.page = page
			self.page.get_by_text("Elements", exact=True).click()
			self.page.get_by_text("Broken Links - Images", exact=True).first.click()

	class UPD_DLD:
		def __init__(self, page: Page):
			self.page = page
			self.page.get_by_text("Elements", exact=True).click()
			self.page.get_by_text("Upload and Download", exact=True).first.click()

	class Dyn_Prop:
		def __init__(self, page: Page):
			self.page = page
			self.page.get_by_text("Elements", exact=True).click()
			self.page.get_by_text("Dynamic Properties", exact=True).first.click()

	class Forms_PForms:
		def __init__(self, page: Page):
			self.page = page
			self.page.get_by_text("Forms", exact=True).click()
			self.page.get_by_text("Practice Form", exact=True).first.click()

	class AFW_Alerts:
		def __init__(self, page: Page):
			self.page = page
			self.page.get_by_text("Alerts, Frame & Windows", exact=True).click()
			self.page.get_by_text("Alerts", exact=True).first.click()
			self.page.get_by_text("Browser Windows", exact=True).first.click()

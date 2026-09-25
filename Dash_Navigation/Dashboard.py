from playwright.sync_api import Page, sync_playwright


class Dash_Elements:
	"""Page objects for the DemoQA Elements pages."""
	def __init__(self, page: Page):
		self.page = page
		self.page.goto("https://demoqa.com/elements")


	class Text_Box:
		def __init__(self, page: Page):
			self.page = page
			self.page.goto("https://demoqa.com/text-box")

	class Check_Box:
		def __init__(self, page: Page):
			self.page = page
			self.page.goto("https://demoqa.com/checkbox")

	class Radio_Button:
		def __init__(self, page: Page):
			self.page = page
			self.page.goto("https://demoqa.com/radio-button")

	class Web_Tables:
		def __init__(self, page: Page):
			self.page = page
			self.page.goto("https://demoqa.com/webtables")

	class Buttons:
		def __init__(self, page: Page):
			self.page = page
			self.page.goto("https://demoqa.com/buttons")

	class Links:
		def __init__(self, page: Page):
			self.page = page
			self.page.goto("https://demoqa.com/links")

	class Broken_Links:
		def __init__(self, page: Page):
			self.page = page
			self.page.goto("https://demoqa.com/broken")

	class UPD_DLD:
		def __init__(self, page: Page):
			self.page = page
			self.page.goto("https://demoqa.com/upload-download")

	class Dyn_Prop:
		def __init__(self, page: Page):
			self.page = page
			self.page.goto("https://demoqa.com/dynamic-properties")

			
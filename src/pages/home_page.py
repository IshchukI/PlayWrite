import os
from playwright.sync_api import Browser


class HomePage:
    def __init__(self, browser: Browser):
        self.context = browser.new_context()
        self.page = self.context.new_page()

    def open(self, src_dir: str):
        self.page.goto(os.path.join(src_dir, 'src/data/runtime_data.html'))

    def close(self):
        self.page.close()
        self.context.close()

    def check_visible(self, locator):
        element = self.page.locator(locator)
        assert element.is_visible(), f"Element '{locator}' is not visible"
        return element

    @property
    def app_info_title(self):
        # App-info div block with App-info title
        return self.check_visible('.AppInfo-title').inner_text()

    @property
    def app_info_subtitle(self):
        # App-info div block with App-info subtitle
        return self.check_visible('.AppInfo-subtitle').inner_text()

    @property
    def model_details(self):
        return self.check_visible('.ModelDetails').inner_text()

    @property
    def profiler_input_settings(self):
        return self.check_visible('.ProfilerInputSettings').inner_text()

    @property
    def performance_summary(self):
        return self.check_visible('.PerformanceSummary').inner_text()

    @property
    def device_utilization_simple(self):
        return self.check_visible('.TotalUtilizationSimple').inner_text()

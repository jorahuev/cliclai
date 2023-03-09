import undetected_chromedriver as uc
import time

class XBrowser:

    def __init__(self):
        options = uc.ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        self.driver = uc.Chrome(options=options)

    def __del__(self):
        self.driver.quit()

    def get(self, url):
        self.driver.get(url)
        time.sleep(10)

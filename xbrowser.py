import undetected_chromedriver as uc
import time

def run_browser(url):
    options = uc.ChromeOptions()
    #options.add_argument('--headless')
    #options.add_argument('--remote-debugging-port=9222')
    driver = uc.Chrome(options=options)

    # Navigate to the specified URL
    driver.get(url)
    time.sleep(20)

    # Return the driver object
    return driver

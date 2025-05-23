from splinter import Browser
from selenium.webdriver.chrome.options import Options

def before_all(context):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1920,1080')

    context.browser = Browser('chrome', options=chrome_options)
    context.base_url = 'http://localhost:8000'

def after_all(context):
    if hasattr(context, 'browser'):
        context.browser.quit()

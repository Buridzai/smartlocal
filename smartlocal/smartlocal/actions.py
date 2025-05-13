from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions

driver = None

def handle_action(action):
    global driver

    urls = {
        "open_google": "https://www.google.com",
        "open_facebook": "https://www.facebook.com",
        "open_youtube": "https://www.youtube.com",
        "open_zalo": "https://chat.zalo.me"
    }

    if action in urls:
        if driver:
            driver.quit()
        options = EdgeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Edge(service=EdgeService(), options=options)
        driver.get(urls[action])

    elif action == "close_browser":
        if driver:
            driver.quit()
            driver = None

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from visual_regression_tracker import VisualRegressionTracker, Config, TestRun
from selenium.webdriver.chrome.service import Service as ChromeService

config = Config(
    apiUrl='http://localhost:4200',
    project='ca36ff18-7ea7-407b-bc5a-0411ef819f29',
    apiKey='DEFAULTUSERAPIKEYTOBECHANGED',
    ciBuildId='commit_sha',
    branchName='develop',
    enableSoftAssert=False,
)


def test_visual_regression_tracker():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    vrt = VisualRegressionTracker(config)

    with vrt:
        try:
            driver.get("https://www.python.org/psf-landing/")
            driver.set_window_size(width=800, height=600)
            vrt.track(TestRun(
                name='psf-landing',
                imageBase64=driver.get_screenshot_as_base64(),
                diffTollerancePercent=0,
                os='Mac',
                browser='Chrome',
                viewport='800x600',
                device='PC',
            ))
        finally:
            driver.quit()

def test_visual_regression_tracker2():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    vrt = VisualRegressionTracker(config)

    with vrt:
        try:
            driver.get("https://github.com/sponsors")
            driver.set_window_size(width=800, height=600)
            vrt.track(TestRun(
                name='github',
                imageBase64=driver.get_screenshot_as_base64(),
                diffTollerancePercent=0,
                os='Mac',
                browser='Chrome',
                viewport='800x600',
                device='PC',
            ))
        finally:
            driver.quit()


def test_visual_regression_tracker3():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    vrt = VisualRegressionTracker(config)

    with vrt:
        try:
            driver.get("https://candymapper.com/")
            # driver.get("https://candymapperr2.com")
            driver.set_window_size(width=800, height=600)
            vrt.track(TestRun(
                name='github',
                imageBase64=driver.get_screenshot_as_base64(),
                diffTollerancePercent=0,
                os='Mac',
                browser='Chrome',
                viewport='800x600',
                device='PC',
            ))
        finally:
            driver.quit()
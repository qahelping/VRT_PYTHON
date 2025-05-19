import os

from selenium import webdriver
from visual_regression_tracker import VisualRegressionTracker, Config, TestRun
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

config = Config(
    apiUrl='http://localhost:4200',
    project='bb840b96-6c6f-4ed8-979b-e0bbfa3fdc3f',
    apiKey='DEFAULTUSERAPIKEYTOBECHANGED',
    ciBuildId='commit_sha',
    branchName='develop',
    enableSoftAssert=False,
)


# def test_visual_regression_tracker():
#     service = ChromeService(ChromeDriverManager().install())
#     options = ChromeOptions()
#     path = service.path
#     service.path = path.replace('THIRD_PARTY_NOTICES.', "")
#     os.chmod(service.path, 0o755)
#     driver = webdriver.Chrome(service=service, options=options)
#     vrt = VisualRegressionTracker(config)
#
#     with vrt:
#         try:
#             driver.get("https://www.python.org/psf-landing/")
#             driver.set_window_size(width=800, height=600)
#             vrt.track(TestRun(
#                 name='psf-landing',
#                 imageBase64=driver.get_screenshot_as_base64(),
#                 diffTollerancePercent=0,
#                 os='Mac',
#                 browser='Chrome',
#                 viewport='800x600',
#                 device='PC',
#             ))
#         finally:
#             driver.quit()
#
# def test_visual_regression_tracker2():
#     service = ChromeService(ChromeDriverManager().install())
#     options = ChromeOptions()
#     path = service.path
#     service.path = path.replace('THIRD_PARTY_NOTICES.', "")
#     os.chmod(service.path, 0o755)
#     driver = webdriver.Chrome(service=service, options=options)
#
#     driver.maximize_window()
#
#     vrt = VisualRegressionTracker(config)
#
#     with vrt:
#         try:
#             driver.get("https://github.com/sponsors")
#             driver.set_window_size(width=800, height=600)
#             vrt.track(TestRun(
#                 name='github',
#                 imageBase64=driver.get_screenshot_as_base64(),
#                 diffTollerancePercent=0,
#                 os='Mac',
#                 browser='Chrome',
#                 viewport='800x600',
#                 device='PC',
#             ))
#         finally:
#             driver.quit()
#
#
# def test_visual_regression_tracker3():
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     vrt = VisualRegressionTracker(config)
#
#     with vrt:
#         try:
#             driver.get("https://candymapper.com/")
#             # driver.get("https://candymapperr2.com")
#             driver.set_window_size(width=800, height=600)
#             vrt.track(TestRun(
#                 name='github',
#                 imageBase64=driver.get_screenshot_as_base64(),
#                 diffTollerancePercent=0,
#                 os='Mac',
#                 browser='Chrome',
#                 viewport='800x600',
#                 device='PC',
#             ))
#         finally:
#             driver.quit()
#
#
# def test_visual_regression_tracker4():
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#     vrt = VisualRegressionTracker(config)
#
#     with vrt:
#         try:
#             # driver.get("https://candymapper.com/")
#             driver.get("https://candymapperr2.com")
#             driver.set_window_size(width=800, height=600)
#             vrt.track(TestRun(
#                 name='candymapperr2',
#                 imageBase64=driver.get_screenshot_as_base64(),
#                 diffTollerancePercent=0,
#                 os='Mac',
#                 browser='Chrome',
#                 viewport='800x600',
#                 device='PC',
#             ))
#         finally:
#             driver.quit()


def test_visual_regression_tracker_python():
    service = ChromeService(ChromeDriverManager().install())
    options = ChromeOptions()
    path = service.path
    service.path = path.replace('THIRD_PARTY_NOTICES.', "")
    os.chmod(service.path, 0o755)
    driver = webdriver.Chrome(service=service, options=options)
    vrt = VisualRegressionTracker(config)

    with vrt:
        try:
            driver.get("https://www.python.org/")
            driver.set_window_size(width=800, height=600)
            vrt.track(TestRun(
                name='python',
                imageBase64=driver.get_screenshot_as_base64(),
                diffTollerancePercent=70,
                os='Mac',
                browser='Chrome',
                viewport='800x600',
                device='PC',
            ))
        finally:
            driver.quit()
import json
from selenium.webdriver.remote.webdriver import WebDriver


def get_cookies(driver: WebDriver, filename='cookies'):
    """保存成功登录页面后的cookies(在登录页面后使用)

    :param driver:
    :param filename: cookies文件
    :return:
    """

    with open(filename, 'w') as file:
        file.write(json.dumps(driver.get_cookies()))


def add_cookies(driver: WebDriver, filename='cookies'):
    """使用cookies登录页面

    :param driver:
    :param filename: cookies文件
    :return:
    """

    with open(filename) as file:
        driver.delete_all_cookies()
        for cookie in json.loads(file.read()):
            driver.add_cookie(cookie)

    driver.refresh()




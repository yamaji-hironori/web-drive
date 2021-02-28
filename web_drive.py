import chromedriver_binary
import json
import time
import sys

from selenium import webdriver


def load_setting():
    with open('./setting.json', 'r') as fr:
        setting = json.load(fr)
    return setting


def input_body(driver, setting):
    search_box = driver.find_element_by_id(setting['value_id'])
    search_box.send_keys(setting['value'])
    time.sleep(3)
    login_button = driver.find_element_by_id(setting['cmd_register_id'])
    login_button.click()
    time.sleep(5)
    return


def login(driver, setting):
    driver.get(setting['url'])
    time.sleep(3)
    search_box = driver.find_element_by_id(setting['user_id'])
    search_box.send_keys(setting['user'])
    time.sleep(3)
    search_box = driver.find_element_by_id(setting['pass_id'])
    search_box.send_keys(setting['pass'])
    time.sleep(3)
    login_button = driver.find_element_by_id(setting['cmd_login_id'])
    login_button.click()
    time.sleep(7)
    return


def main():
    setting = load_setting()

    driver = webdriver.Chrome()
    login(driver, setting)
    input_body(driver, setting)

    driver.quit()
    return


def test():
    setting = load_setting()
    print(setting)
    return

if __name__ == '__main__':
    main()
    #test()
    sys.exit()

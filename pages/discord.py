from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time
from tech_files.rambler_mail import MailConfirm
from pages.planet import PlanetQuest
from pages.metamask import MetaMask
import pyautogui
from pynput.keyboard import Key, Controller

class Discord(BasePage):
    def go_login(self):
        url = 'https://discord.com/login'
        self.browser.get(url)
    def login(self):
        self.wait_for_element(By.NAME,'email')
        self.browser.find_element_by_name("email").click()
        self.browser.find_element_by_name("email").clear()
        self.browser.find_element_by_name("email").send_keys(self.discord_email)
        self.browser.find_element_by_name("password").click()
        self.browser.find_element_by_name("password").clear()
        self.browser.find_element_by_name("password").send_keys(self.discord_pass)
        time.sleep(1)
        self.browser.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(3)

    def captcha(self):
        if self.is_element_presented(By.CSS_SELECTOR,"iframe[title*='hCaptcha']"):
            print('КАПТЧА!')
            self.wait_for_captcha()
        else:
            print('Нет КАпчи')

    def should_be_discrod_page(self):
        url = 'https://discord.com/channels/@me'
        if self.browser.current_url == url:
            print('Успешный логин!')
            return True
        else:
            return False

    def resend_verification_letter(self):
        time.sleep(1)
        resend_button = (By.XPATH, "//*[contains(text(),'Отправить заново')]")
        # ok_button = (By.XPATH, "//*[contains(text(),'OK')]")
        self.wait_and_click(*resend_button)
        time.sleep(2)
        ok_button = (By.XPATH, "//button[text()='OK']")
        self.click_element(*ok_button)
        time.sleep(2)

    def go_discord(self):
        go_discord_button = (By.XPATH,"//div[text()='Перейти в Discord']")
        self.wait_and_click(*go_discord_button)
        time.sleep(5)

    def close_popup(self):
        popup_close_button = (By.CSS_SELECTOR,'button[aria-label="Закрыть"]')
        self.wait_and_click(*popup_close_button,timeout=5)
        close_download_popup = (By.CSS_SELECTOR,'div[class*=closeButton]')
        self.wait_and_click(*close_download_popup,timeout=5)

    def get_verification_link(self):
        verification_link = MailConfirm(self.email,self.email_pass).get_code()
        if not verification_link:
            time.sleep(10)
            self.get_verification_link()
        else:
            self.browser.get(verification_link)
            time.sleep(2)
    def should_be_success_verification(self):
        true_verification = (By.XPATH, "//*[contains(text(),'E-mail подтверждён!')]")
        return self.wait_for_element(*true_verification,10)



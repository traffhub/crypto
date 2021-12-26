from selenium.webdriver.common.by import By
import time
from pages.base_page import BasePage

class Locators:
    title = 'Phantom Wallet'

    create_wallet_but = (By.XPATH, "//button[text()='Создать новый кошелек']")
    secret_phrase = (By.XPATH, "//textarea")

    save_but = (By.XPATH, "//button[@type='submit']")
    password_input = (By.XPATH, "//input[@name='password.first']")
    password_input2 = (By.XPATH, "//input[@name='password.confirm']")
    checkbox = (By.XPATH, "//input[@type='checkbox']")

    continue_but = (By.XPATH, "//button[@type='button']")

    select_token =  (By.XPATH, "//span[text()='Select token']")

    wsol = (By.XPATH, "//div[text()='wSOL']")
    max_button = (By.XPATH, "//div[text()='MAX']")

    aprove = (By.XPATH, "//span[text()='Approve on your wallet']")
    complete_text = (By.XPATH,"//h4[text()='Operation completed']" )
    close = (By.XPATH, "//span[text()='Close']")

    wallet =(By.XPATH,"//span[@class='wallet-key']" )

    copy_wallet = (By.XPATH,"//span[text()='Copy Address']" )

class PhantomWallet(BasePage):
    def go_phantom(self):
        url = 'chrome-extension://bfnaelmomeimhlpmgjnjophhpkkoljpa/onboarding.html'
        self.browser.get(url)

    def create_wallet(self):
        self.go_phantom()
        self.wait_and_click(*Locators.create_wallet_but)
        self.wait_for_element(*Locators.secret_phrase)
        self.phantom_secret = self.browser.find_element(*Locators.secret_phrase).text
        self.wait_and_click(*Locators.save_but)
        self.wait_and_click(*Locators.password_input)
        self.send_keys_element(*Locators.password_input,self.email_pass)
        self.send_keys_element(*Locators.password_input2,self.email_pass)
        self.click_element(*Locators.checkbox)
        self.click_element(*Locators.save_but)
        self.wait_and_click(*Locators.continue_but)
        time.sleep(4)
        self.click_element(*Locators.continue_but)

class Meanfi(BasePage):
    def go_reflint(self):
        url= 'https://app.meanfi.com?ref=2EuHJSLLYZiHVK2fhzDgs8VNxdkQuhnqD3wegvDQEMzy'
        self.browser.get(url)

    def connect_wallet(self):
        button = (By.XPATH, "//span[text()='Connect wallet account']")
        self.wait_and_click(*button)

        choose_phantom = (By.XPATH, "//span[text()='Phantom']")
        self.wait_and_click(*choose_phantom)

    def bypass_connection(self):
        self.wait_for_window_with_title(Locators.title)
        self.wait_and_click(*Locators.save_but)
        self.wait_for_current_window_disappear()

    def exchange(self):
        url = 'https://app.meanfi.com/exchange'
        self.browser.get(url)
        self.wait_and_click(*Locators.select_token)
        time.sleep(1)
        self.wait_and_click(*Locators.wsol)
        self.wait_and_click(*Locators.max_button)
        self.wait_and_click(*Locators.aprove)
        self.bypass_connection()
        self.wait_for_element()

    def get_wallet(self):
        self.wait_and_click(*Locators.wallet)
        self.wait_and_click(*Locators.copy_wallet)
from selenium.common.exceptions import NoSuchElementException
from pages.conftest import Bot
from selenium.common.exceptions import  WebDriverException,TimeoutException
from selenium.common.exceptions import NoSuchElementException,ElementClickInterceptedException,ElementNotInteractableException
from selenium.common.exceptions import TimeoutException,NoSuchWindowException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import string,time
import spintax

import random
with open(r'files/useragents.txt','r') as file:
    ua_list = file.read().split('\n')


class BasePage(Bot):
    def is_element_presented(self,how,what): #ищет элемент на странице, если элемента нет, выдает ошибку
        try:
            self.browser.find_element(how,what)
        except(NoSuchElementException):
            return False
        return True

    def wait_for_window_with_title(self,title,timeout=10):
        for i in range(timeout):
            tabs = self.browser.window_handles
            for tab in tabs:
                self.browser.switch_to.window(tab)
                if self.browser.title == title:
                    return True
            time.sleep(1)
        return False

    def wait_fot_window_with_domain(self,domain,timeout=10):
        for i in range(timeout):
            tabs = self.browser.window_handles
            for tab in tabs:
                self.browser.switch_to.window(tab)
                if domain in self.browser.current_url:
                    return True
            time.sleep(1)
        return False

    def wait_for_current_window_disappear(self,timeout=10):
        for _ in range(timeout):
            try:
                self.browser.title
                time.sleep(1)
            except NoSuchWindowException:
                self.switch_to_main()
                return True
        return False

    def wait_for_element(self, how, what, timeout=20):  # ждет загрузки элемента
        try:
            WebDriverWait(self.browser, timeout, 1).until(EC.element_to_be_clickable((how, what)))
        except(TimeoutException):
            print(f'no such element presented in {timeout} seconds')
            return False
        return True

    def wait_for_element_disappear(self, how, what, timeout=10):  # ждет загрузки элемента
        try:
            WebDriverWait(self.browser, timeout, 1).until_not(EC.element_to_be_clickable((how, what)))
        except(TimeoutException):
            print(f'no such element presented in {timeout} seconds')
            return False
        self.switch_to_main()
        return True


    def click_element(self, how, what):  # ищет элемент на странице, если элемент есть, кликает по нему. Если нет, выдает ошибку
        try:
            self.browser.find_element(how, what)
            self.browser.find_element(how, what).click()
        except(NoSuchElementException,ElementClickInterceptedException,ElementNotInteractableException):
            return False
        return True

    def wait_and_click(self,how, what, timeout=20):
        if self.wait_for_element(how, what, timeout):
            return self.click_element(how, what)
        else:
            return False

    def send_keys_element(self,how,what,text): #отправляет текст в элемент
        try:
            self.browser.find_element(how,what)
            self.browser.find_element(how, what).send_keys(text)
        except(NoSuchElementException):
            return False
        return True

    def switch_to_window(self,title):
            tabs = self.browser.window_handles
            for tab in tabs:
                self.browser.switch_to.window(tab)
                if self.browser.title == title:
                    return
    def switch_to_window_by_domain(self,domain):
            tabs = self.browser.window_handles
            for tab in tabs:
                self.browser.switch_to.window(tab)
                if domain in self.browser.current_url:
                    return

    def wait_for_window(self):
        count1 = self.browser.window_handles
        while len(self.browser.window_handles) == len(count1):
            time.sleep(1)

    def switch_to_main(self):
        main_page = self.browser.window_handles[0]
        self.browser.switch_to.window(main_page)


    # def generate_password(self):
    #     low = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(3,5)))
    #     up = ''.join(random.choice(string.ascii_uppercase) for i in range(random.randint(3,5)))
    #     digt =''.join(random.choice(string.digits) for i in range(random.randint(3,5)))
    #     symb = spintax.spin('{&|?|!}')*random.randint(2,3)
    #     self.password = low + up + symb + digt

    # def save_info(self):
    #     filename = r'D:\документы\planet\accs.txt'
    #     data = f'{self.email},{self.password},{self.secret}\n'
    #     with open(filename, "a") as file:
    #         file.write(data)

    def wait_for_captcha(self):
        time.sleep(2)
        while self.is_element_presented(By.CSS_SELECTOR,'.antigate_solver.in_process'):
            time.sleep(5)
            print('КАПТЧА РЕШАЕТСЯ')
        else:
            print('КАПТЧА РЕШЕНА!')

    def finish(self):
        print(f'Закончил!!!\n{self.discord_email},{self.discord_pass},{self.email},{self.email_pass}')

        self.browser.quit()
        # self.save_useragent()
        # self.save_info()

    # def go_captcha(self):
    #     self.browser.get('https://maximedrn.github.io/hcaptcha-solver-python-selenium/')


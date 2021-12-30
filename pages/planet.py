from selenium.webdriver.common.by import By
import time,random
from pages.base_page import BasePage
from pynput.keyboard import Key, Controller
import pyautogui
class GameLocs:
    connect_wallet = (By.CSS_SELECTOR,"div[class='_lyduxj']")
    error = (By.XPATH,"//p[text()='Something has gone wrong.']")
    PlanetTitle = 'PlanetQuest'
    MetaMask_title = 'MetaMask Notification'
    next_button = (By.XPATH,"//*[contains(text(),'Далее')]")
    connect = (By.XPATH,"//button[text()='Подключиться']")

    Game_Title = 'Immutable X Link'
    connect_button2 = (By.XPATH,"//button[text()='CONNECT WALLET']")

    sing_in = (By.XPATH,"//button[text()='SIGN IN']")


    subscr_but = (By.XPATH, "//button[text()='Подписать']")
    checkbox = (By.CSS_SELECTOR, 'input[type="checkbox"]')

    set_up = (By.XPATH,"//button[text()='SET UP']")
    finish = (By.XPATH,"//button[text()='FINISH']")

    game_but1 =(By.XPATH,"//button[text()='FINISH']")
    game_but2 = (By.CSS_SELECTOR, 'div[class="_auld1"]')

    Union = (By.XPATH,"//*[contains(text(),'Union')]")
    Empire = (By.XPATH,"//*[contains(text(),'Empire')]")
    Federation = (By.XPATH,"//*[contains(text(),'Federation')]")
    link_discord = (By.CSS_SELECTOR, 'div[class="_r4ewp6"]')

    #Дискорд
    email_input = (By.CSS_SELECTOR, '.input')

    verify_email = (By.CSS_SELECTOR, 'div[class="_1bgfl1x"]')

    claim_buton = (By.CSS_SELECTOR, 'div[class="_uy6k8y"]')
    claim2_but =(By.CSS_SELECTOR, 'div[class="_1dur0rb"]')

    email_waiting = (By.XPATH,"//*[contains(text(),'Registering email')]")


# ref_link = 'https://planetquest.io/join/referral/0d99778cb5ffc1fcc00c5c88c04941c09d9725e7d38e7f900d48938013262972'
ref_link = 'https://planetquest.io/join/referral/bf91164a5dd4bf874605a257419f6b8d860318e93fcabe1c9116a514be62f23f'

class PlanetQuest(BasePage):
    def go_reflink(self):
        self.browser.get(ref_link)
        time.sleep(3)
    def connect_metamask(self):
        self.wait_and_click(*GameLocs.connect_wallet,timeout=30)

    def run_planet(self):
        self.wait_for_window()
        time.sleep(2)

        self.switch_to_window(GameLocs.MetaMask_title)
        time.sleep(1)
        assert self.wait_and_click(*GameLocs.next_button)
        time.sleep(2)
        assert self.wait_and_click(*GameLocs.connect)
        self.wait_for_window()
        time.sleep(1)

        self.switch_to_window(GameLocs.Game_Title)
        time.sleep(2)
        assert self.wait_and_click(*GameLocs.connect_button2)
        self.wait_for_window()

        time.sleep(1)

        self.switch_to_window(GameLocs.MetaMask_title)
        time.sleep(1)
        assert self.wait_and_click(*GameLocs.next_button)
        time.sleep(1)
        assert self.wait_and_click(*GameLocs.connect)
        self.wait_for_window()
        time.sleep(1)

        self.switch_to_window(GameLocs.Game_Title)
        time.sleep(1)
        assert self.wait_and_click(*GameLocs.sing_in)
        self.wait_for_window()
        time.sleep(1)

        self.switch_to_window(GameLocs.MetaMask_title)
        time.sleep(1)
        assert self.wait_and_click(*GameLocs.subscr_but)
        self.wait_for_window()
        time.sleep(1)

        self.switch_to_window(GameLocs.Game_Title)
        time.sleep(1)
        self.click_element(*GameLocs.checkbox)
        time.sleep(1)
        assert self.wait_and_click(*GameLocs.set_up)
        self.wait_for_window()
        time.sleep(1)

        self.switch_to_window(GameLocs.MetaMask_title)
        time.sleep(1)
        assert self.wait_and_click(*GameLocs.subscr_but)
        self.wait_for_window()

        self.switch_to_window(GameLocs.Game_Title)
        time.sleep(1)
        assert not self.is_element_presented(*GameLocs.error)
        assert self.wait_and_click(*GameLocs.finish)

        # self.switch_to_window(GameLocs.Game_Title)

        self.switch_to_window(GameLocs.PlanetTitle)
        if self.is_element_presented(*GameLocs.game_but2):
            self.click_element(*GameLocs.game_but2)
        assert self.wait_for_element(*GameLocs.Union)
        elements = [GameLocs.Union,GameLocs.Empire,GameLocs.Federation]

        self.click_element(*random.choice(elements))
        time.sleep(3)
        assert self.wait_for_element(*GameLocs.link_discord)
        print('Кошелек Привязан!!')

    def choose_fraction(self):
        if self.is_element_presented(*GameLocs.game_but2):
            self.click_element(*GameLocs.game_but2)
        assert self.wait_for_element(*GameLocs.Union)
        elements = [GameLocs.Empire,GameLocs.Federation]
        self.click_element(*random.choice(elements))
        time.sleep(3)

    def connect_discord(self):
        self.click_element(*GameLocs.link_discord)
        self.switch_to_window_by_domain('discord.com')
        time.sleep(2)
        invite_button = (By.XPATH,"//*[contains(text(),'Принять приглашение')]")
        if self.is_element_presented(*invite_button):
            self.wait_and_click(*invite_button)
            # self.browser.maximize_window()
            # time.sleep(2)
            # keyboard = Controller()
            # keyboard.press(Key.esc)
            # keyboard.release(Key.esc)
            # time.sleep(2)
            for window in pyautogui.getWindowsWithTitle(self.browser.title):
                window.activate()
                pyautogui.press('esc')
            # time.sleep(1)
            # pyautogui.press('esc')
            time.sleep(3)
        if self.is_element_presented(*invite_button):
            self.click_element(*invite_button)
            # self.browser.maximize_window()
            # time.sleep(2)
            # keyboard = Controller()
            # keyboard.press(Key.esc)
            # keyboard.release(Key.esc)
            # time.sleep(2)
            # for window in pyautogui.getWindowsWithTitle(self.browser.title):
            #     window.activate()
            #     pyautogui.press('esc')
            time.sleep(2)
        go_discord_button = (By.XPATH,"//*[contains(text(),'Перейти в Discord')]")
        if self.is_element_presented(*go_discord_button):
            self.click_element(*go_discord_button)
            # self.browser.maximize_window()
            # time.sleep(2)
            # keyboard = Controller()
            # keyboard.press(Key.esc)
            # keyboard.release(Key.esc)
            # for window in pyautogui.getWindowsWithTitle(self.browser.title):
            #     window.activate()
            #     pyautogui.press('esc')
            time.sleep(2)

        if not 'channels' in self.browser.current_url:
            self.browser.refresh()
            self.connect_discord()
        else:
            print('УСПЕШНО ПОДКЛЮЧИЛ ДИСКОРД!')
            time.sleep(3)

    def connect_discord2(self):

        assert self.wait_and_click(*GameLocs.link_discord)
        self.switch_to_window_by_domain('discord.com')
        time.sleep(2)
        invite_button = (By.XPATH,"//*[contains(text(),'Принять приглашение')]")
        assert self.wait_and_click(*invite_button)
        time.sleep(1)
        go_discord_button = (By.XPATH,"//*[contains(text(),'Перейти в Discord')]")
        self.wait_and_click(*go_discord_button,5)

        # time.sleep(2)
        # self.browser.execute_script(f'window.open("{invite_link}")')
        # self.browser.switch_to.window(self.browser.window_handles[-1])
        # time.sleep(10)
        # self.click_element(*invite_button)
        # time.sleep(5)
        # go_discord_button = (By.XPATH,"//*[contains(text(),'Перейти в Discord')]")
        #
        # channel_link = self.browser.current_url
        # self.browser.execute_script(f'window.open("{channel_link}")')
        # self.browser.switch_to.window(self.browser.window_handles[-1])



    def get_discord_inv_link(self):

        unlock_link = (By.XPATH,"//div[text()='Unlock']")
        self.wait_for_element(*unlock_link,20)
        popup_close_button = (By.CSS_SELECTOR,'button[aria-label="Закрыть"]')
        self.click_element(*popup_close_button)
        close_download_popup = (By.CSS_SELECTOR,'div[class*=closeButton]')
        self.click_element(*close_download_popup)

        self.click_element(*unlock_link)
        discord_link = (By.CSS_SELECTOR,"a[href*='join/discord']")
        self.wait_for_element(*discord_link)

        self.discord_invite_link = self.browser.find_element(*discord_link).get_attribute('href')

    def get_email_verification_link(self):
        email_verification_issue = (By.CSS_SELECTOR,"a[aria-label*='verify-email']")
        self.click_element(*email_verification_issue)
        unlock_link = (By.XPATH,"//div[text()='Get e-mail verification link']")
        self.wait_and_click(*unlock_link)
        discord_link = (By.CSS_SELECTOR,"a[href*='join/email']")
        self.wait_for_element(*discord_link)

        self.email_invite_link = self.browser.find_element(*discord_link).get_attribute('href')

    def run_discord_verification(self):
        # self.connect_discord()
        self.get_discord_inv_link()
        self.switch_to_window_by_domain('planetquest')
        self.browser.get(self.discord_invite_link)

    def input_email(self):
        self.wait_for_element(*GameLocs.game_but2)
        assert self.wait_and_click(*GameLocs.game_but2)

        assert self.wait_for_element(*GameLocs.email_input)

        self.send_keys_element(*GameLocs.email_input,self.email)
        self.click_element(*GameLocs.verify_email)

    def run_email_verification(self):
        self.switch_to_window_by_domain('discord.com')
        time.sleep(1)
        self.get_email_verification_link()
        self.switch_to_window_by_domain('planetquest')
        self.browser.get(self.email_invite_link)

    def go_finish(self):
        self.wait_for_element(*GameLocs.claim_buton,30)
        if self.is_element_presented(*GameLocs.claim_buton):
            self.click_element(*GameLocs.claim_buton)
        if self.is_element_presented(*GameLocs.claim2_but):
            self.click_element(*GameLocs.claim2_but)
        time.sleep(2)
        if self.is_element_presented(*GameLocs.claim2_but):
            self.click_element(*GameLocs.claim2_but)
        time.sleep(2)
        if self.is_element_presented(*GameLocs.claim2_but):
            self.click_element(*GameLocs.claim2_but)


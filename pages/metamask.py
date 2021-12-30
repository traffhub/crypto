from selenium.webdriver.common.by import By
import time
from pages.base_page import BasePage
from selenium.common.exceptions import InvalidCookieDomainException,WebDriverException,NoSuchWindowException

# main_wallet = '0xBA8942587ad69019e26c001E8c8C1b1409ec6f32'
main_wallet = '0x20F579530cFC59C31fdd3a5E77539Cb92656ab55'

class Locators:
    start_work_button = (By.CSS_SELECTOR,'button[class*=first-time-flow__button]')
    agree_button = (By.XPATH,"//*[contains(text(),'Создать кошелек')]")
    agree_button2 = (By.XPATH,"//*[contains(text(),'Я согласен')]")
    password = (By.CSS_SELECTOR,'#create-password')
    password_conf = (By.CSS_SELECTOR,'#confirm-password')
    radio_button = (By.CSS_SELECTOR,'div[class="first-time-flow__checkbox"]')
    next = (By.CSS_SELECTOR,'.button')
    next2 = (By.XPATH, "//button[text()='Далее']")
    show_secret = (By.CSS_SELECTOR,"div[class='reveal-seed-phrase__secret-blocker']")
    secret_phrase = (By.CSS_SELECTOR,'div[class="reveal-seed-phrase__secret-words notranslate"]')
    next_button = (By.CSS_SELECTOR,'button[class="button btn--rounded btn-primary first-time-flow__button"]')
    h3 = (By.XPATH, "//*[contains(text(),'Подтвердите свою секретную резервную фразу')]")
    choose_phrase = (By.XPATH,"//*[contains(text(),'')]")
    next3 = (By.XPATH, "//button[text()='Подтвердить']")
    next_button = (By.CSS_SELECTOR,'button[class="button btn--rounded btn-primary first-time-flow__button"]')
    close_popup = (By.CSS_SELECTOR,'button[class="fas fa-times popover-header__button"]')
    connect_name = 'chrome-extension://'

    password_input = (By.ID,'password')
    unblock_button = (By.XPATH, "//button[text()='Разблокировать']")

    connect_window = 'permissions-connect-choose-account__bottom-buttons'
    next_step = (By.XPATH, "//button[contains(@class,'button btn--rounded btn-primary')]")
    connect_button = (By.XPATH, "//button[@data-testid='page-container-footer-next']")

class Tokentrove:
    connect_wallet_button = (By.XPATH, "//div[text()='Connect Wallet']")
    select_metamask = (By.XPATH, "//div[@class='wallet-option-name' and text()='MetaMask']")
    listing_item = (By.XPATH, "//div[@class='listing-wrapper']")
    transfer_item = (By.XPATH, "//span[text()='Transfer']")
    address_input = (By.XPATH, "//input[@class='transfer-input']")
    TransferButton = (By.XPATH, "//button[@class='order-buy-button gu-button']")

class ImutableX:
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='CONFIRM']")
    CONNECT_BUTTON = (By.XPATH, "//button[text()='CONNECT WALLET']")

    FINISH = (By.XPATH, "//button[text()='FINISH']")
    sing_in = (By.XPATH,"//button[text()='SIGN IN']")

class MetaMask(BasePage):
    def go_metamask(self):
        link = 'chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html'
        self.browser.get(link)
    def close_metamask_window(self):
        self.wait_fot_window_with_domain(Locators.connect_name,timeout=30)
        self.browser.close()
        self.switch_to_main()
    def run_metamask(self):
        self.go_metamask()
        time.sleep(2)
        # self.wait_for_window()
        # self.browser.close()
        self.switch_to_window('MetaMask')
        assert self.wait_and_click(*Locators.start_work_button)
        # time.sleep(1)
        assert self.wait_and_click(*Locators.agree_button)
        # time.sleep(1)
        assert self.wait_and_click(*Locators.agree_button2)
        # time.sleep(1)
        assert self.wait_for_element(*Locators.password)
        self.send_keys_element(*Locators.password,self.email_pass)
        # time.sleep(1)
        self.send_keys_element(*Locators.password_conf,self.email_pass)
        # time.sleep(1)
        self.click_element(*Locators.radio_button)
        # time.sleep(1)
        self.click_element(*Locators.next)
        time.sleep(1)
        assert self.wait_and_click(*Locators.next2)
        # time.sleep(1)
        assert self.wait_and_click(*Locators.show_secret)
        # time.sleep(1)
        self.secret = self.browser.find_element(*Locators.secret_phrase).text
        self.click_element(*Locators.next_button)
        # time.sleep(1)
        assert self.wait_for_element(*Locators.h3)
        for word in self.secret.split(' '):

            buttons = self.browser.find_elements(By.XPATH, f"//div[text()='{word}']")
            buttons_list = []
            for b in buttons:
                selector = self.browser.execute_script("return arguments[0].getAttribute('class');", b)
                if not 'selected' in selector:
                    buttons_list.append(b)
            buttons_list[0].click()

            # self.click_element(By.XPATH, f"//*[contains(text(),'{word}')]")
        # time.sleep(1)
        assert self.wait_and_click(*Locators.next_button)
        self.save_info()
        time.sleep(1)
        assert self.wait_and_click(*Locators.next_button)
        # time.sleep(1)
        assert self.wait_and_click(*Locators.close_popup)
        self.click_element(*Locators.close_popup)


    def bypass_metamask_window(self,connect=True,token=False):
        try:
            self.wait_fot_window_with_domain(Locators.connect_name)
            if connect is True:
                self.wait_and_click(*Locators.next_step)
                self.wait_and_click(*Locators.connect_button)
            else:
                self.wait_and_click(*Locators.next_step)
            if token is True:
                time.sleep(2)
                self.wait_fot_window_with_domain(Locators.connect_name)
                self.wait_and_click(*Locators.next_step)
            self.wait_for_current_window_disappear(10)
        except NoSuchWindowException:
            self.switch_to_main()
    def login_by_password(self):
        self.go_metamask()
        self.wait_for_element(*Locators.password_input)
        self.send_keys_element(*Locators.password_input,self.email_pass)
        time.sleep(1)
        self.click_element(*Locators.unblock_button)
        assert self.wait_for_element_disappear(*Locators.unblock_button,20)
        time.sleep(5)
    def go_tokentrove(self):
        url = 'https://tokentrove.com'
        self.browser.get(url)
        self.wait_and_click(*Tokentrove.connect_wallet_button)
        self.wait_and_click(*Tokentrove.select_metamask)

    def metamask_should_connect(self):
        return True if not self.is_element_presented(*Tokentrove.connect_wallet_button) else False

    def go_Planet_collection(self):
        url = 'https://tokentrove.com/account/collection/PlanetQuest'
        self.browser.get(url)
        time.sleep(3)

    def should_be_item(self):
        return self.is_element_presented(*Tokentrove.listing_item)

    def transfer_item(self):
        self.click_element(*Tokentrove.listing_item)
        self.wait_and_click(*Tokentrove.transfer_item,20)
        self.wait_for_element(*Tokentrove.address_input)
        self.send_keys_element(*Tokentrove.address_input,main_wallet)
        self.wait_and_click(*Tokentrove.TransferButton)

    def bypass_immutable(self,connect=False):
        self.wait_fot_window_with_domain('link.x.immutable.com')
        if connect == True:
            self.wait_and_click(*ImutableX.CONNECT_BUTTON)
            self.bypass_metamask_window(True)
        else:
            self.wait_and_click(*ImutableX.CONFIRM_BUTTON)
            self.bypass_metamask_window(connect=False)
        self.wait_fot_window_with_domain('link.x.immutable.com')
        if connect == True:
            self.wait_and_click(*ImutableX.sing_in)
            self.bypass_metamask_window(False)
        self.wait_and_click(*ImutableX.FINISH)
        self.wait_for_current_window_disappear(10)

    def set_up_immutable(self):
        self.wait_fot_window_with_domain('link.x.immutable.com')
        checkbox = (By.CSS_SELECTOR, 'input[type="checkbox"]')
        set_up = (By.XPATH, "//button[text()='SET UP']")
        self.wait_and_click(*checkbox)
        self.wait_and_click(*set_up)

    def import_wallet(self,secret,password):
        self.go_metamask()
        assert self.wait_and_click(*Locators.start_work_button)
        import_but = (By.XPATH, "//button[text()='Импортировать кошелек']")
        self.wait_and_click(*import_but)
        agree = (By.XPATH, "//button[text()='Я согласен']")
        self.wait_and_click(*agree)
        # assert self.wait_for_element(*secret_inpit)
        time.sleep(3)
        secret_inpit = (By.XPATH, "//input")
        self.send_keys_element(*secret_inpit,secret)
        # self.click_element(*Locators.radio_button)
        password1 = (By.ID, 'password' )
        password2 = (By.ID, 'confirm-password')
        self.send_keys_element(*password1,password)
        time.sleep(1)
        self.send_keys_element(*password2,password)

        check_box1 = (By.CSS_SELECTOR,'div[class="first-time-flow__checkbox first-time-flow__terms"]')
        self.click_element(*check_box1)
        time.sleep(1)
        do_import = (By.XPATH, "//button[text()='Импорт']")
        self.click_element(*do_import)
        time.sleep(10)
        self.wait_and_click(*Locators.next_button)

    def network(self,type='BNB'):
        if type=='BNB':
            name = 'Binance Smart Chain Mainnet'
            url = 'https://bsc-dataseed1.ninicoin.io'
            id = '56'
            symbol = 'BNB'
            site = 'https://bscscan.com/'
        if type == 'MATIC':
            name = 'Polygon Mainnet'
            url = 'https://polygon-rpc.com/'
            id = '137'
            symbol = 'MATIC'
            site = 'https://polygonscan.com/'

        self.browser.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#settings/networks')
        time.sleep(1)
        send = (By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[1]/div/button')
        send1 = (
        By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/label/input')
        send2 = (
        By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/label/input')
        send3 = (
        By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/label/input')
        send4 = (
        By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[4]/label/input')
        send5 = (
        By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[5]/label/input')
        self.click_element(*send)
        self.send_keys_element(*send1, name)
        self.send_keys_element(*send2, url)
        self.send_keys_element(*send3, id)
        self.send_keys_element(*send4, symbol)
        self.send_keys_element(*send5, site)
        send66 = (By.XPATH, '')
        send6 = (By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[3]/button[2]')
        self.click_element(*send6)
        time.sleep(5)

    def add_token(self,contract='0xdf9B4b57865B403e08c85568442f95c26b7896b0'):
        self.browser.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#import-token')
        input = (By.CSS_SELECTOR, '#custom-address')
        self.send_keys_element(*input,contract)
        add_token = (By.XPATH, "//button[contains(text(),'Add Custom Token')]")
        self.wait_and_click(*add_token)
        import_token = (By.XPATH, "//button[contains(text(),'Import')]")
        self.wait_and_click(*import_token)


    def connect_wallet_2(self):
        connect_wallet = (By.CSS_SELECTOR, "div[class='_lyduxj']")
        self.wait_and_click(*connect_wallet)
        self.bypass_metamask_window(True)
        self.wait_fot_window_with_domain('link.x.immutable.com')
        assert self.wait_and_click(*ImutableX.CONNECT_BUTTON)
        self.bypass_metamask_window(True)
        self.wait_fot_window_with_domain('link.x.immutable.com')
        assert self.wait_and_click(*ImutableX.sing_in)
        self.bypass_metamask_window(False)
        self.wait_fot_window_with_domain('link.x.immutable.com')
        setup_text = (By.XPATH, "//h1[text()='Set up Immutable X Key']")
        assert self.wait_for_element(*setup_text)
        checkbox = (By.CSS_SELECTOR, 'input[type="checkbox"]')
        set_up = (By.XPATH, "//button[text()='SET UP']")
        assert self.click_element(*checkbox)
        assert self.wait_and_click(*set_up)
        self.bypass_metamask_window(False)
        self.finish_immutable()

    def finish_immutable(self):
        self.wait_fot_window_with_domain('link.x.immutable.com')
        assert self.wait_and_click(*ImutableX.FINISH)
        self.wait_for_current_window_disappear(10)


    def should_be_success_transfer(self):
        self.go_Planet_collection()
        return True if not self.should_be_item() else False

    def get_wallet(self):
        title = (By.XPATH, "//button[@title='Опции счета']")
        self.wait_and_click(*title)
        wallet = (By.XPATH, "//span[text()='Реквизиты счета']")
        self.wait_and_click(*wallet)
        time.sleep(1)
        wallet_txt = (By.XPATH, "//div[@class='qr-code__address']")
        wallet = self.browser.find_element(*wallet_txt).text
        self.address = wallet
        # filename = r'C:\crypto\wallet.txt'
        # data = f'{wallet}\n'
        # with open(filename, "a") as file:
        #     file.write(data)

        # bot.adress = bot.browser.find_element(*wallet).text


class Lions(MetaMask):
        def go_lions(self,url):
            # url = 'https://invites.lazylionsnft.com/i/lG5r'
            self.browser.get(url)

        def auth_discord(self):
            FINISH = (By.XPATH, "//a[text()='Authorize Discord']")
            self.wait_and_click(*FINISH)
            time.sleep(2)
            auth_disc = (By.XPATH, "//div[text()='Авторизовать']")
            assert self.wait_and_click(*auth_disc,timeout=30)
            time.sleep(10)
            get_invite = (By.XPATH, "//div[text()='Принять приглашение']")
            get_invite2 = (By.XPATH, "//div[text()='Перейти']")
            self.click_element(*get_invite)
            self.click_element(*get_invite2)
            time.sleep(2)
            self.click_element(*get_invite)
            self.click_element(*get_invite2)
            time.sleep(15)
            popup_close_button = (By.CSS_SELECTOR, 'button[aria-label="Закрыть"]')
            close_download_popup = (By.CSS_SELECTOR, 'div[class*=closeButton]')
            self.click_element(*popup_close_button)
            self.click_element(*close_download_popup)
            do_smth = (By.XPATH, "//div[text()='Выполнить']")
            assert self.wait_for_element(*do_smth,timeout=30)
            time.sleep(1)
            assert self.wait_and_click(*do_smth)
            time.sleep(2)
            checkbox = (By.XPATH, "//input[@type='checkbox']")
            self.click_element(*checkbox)
            time.sleep(2)
            send  = (By.XPATH, "//div[text()='Отправить']")
            assert self.wait_and_click(*send)

        def vetify_discord(self):
            verify_button = (By.XPATH, "//div[text()='Verify']")
            if not self.wait_and_click(*verify_button):
                self.wait_and_click(*verify_button,5)
                self.wait_and_click(*verify_button,5)
            time.sleep(2)
            lion_button = (By.XPATH, "//div[contains(@aria-label,'🦁')]")
            self.click_element(*lion_button)
            time.sleep(2)
            # self.browser.get('https://discord.com/channels/869565356400844820/902184546781519992')
            # wallet_but = (By.XPATH, "//div[text()='I already have a wallet']")
            # assert self.wait_and_click(*wallet_but)
            self.browser.get('https://discord.com/channels/869565356400844820/902211447776501871')
            time.sleep(5)
            enter_but = (By.XPATH, "//div[text()='Enter the Discord']")
            assert self.wait_and_click(*enter_but)

        def claim(self):
            self.browser.get('https://collectibles.lazylionsnft.com/')
            connect = (By.XPATH, "//button[text()='Connect my wallet']")
            assert self.wait_and_click(*connect)
            metamask = (By.XPATH, "//div[text()='MetaMask']")
            assert self.wait_and_click(*metamask)
            self.bypass_metamask_window(True)

        def open_pack(self,count=1):
            for _ in range(count):
                pack = (By.XPATH, "//div[text()='Open your packs']")
                self.click_element(*pack)
                img = (By.XPATH, "//img[@alt='Packs']")
                self.wait_and_click(*img)
                time.sleep(10)
# bot.browser.get('https://tokentrove.com')

# for _ in range(3):
#     threading.Thread(target=run).start()
#     time.sleep(15)

# sorvinatatyana@rambler.ru,xgo0bi3h5ua4b,sorvinatatyana@rambler.ru,I5lwxNbCR
# skyetatum0py0@rambler.ru,aiuk8ahgael9,skyetatum0py0@rambler.ru,hddei20K90

# for _ in range(10):
#     time.sleep(random.randint(1,5))
#     acc = get_first_user(accaunts_path)
#     bot = Run()
#     bot.get_dicord_acc(acc)
#
#     if MailConfirm(bot.email,bot.email_pass).check_connection() is False:
#         bot.save_bad_email()
#         break
#     else:
#         print('ПОЧТА АКТИВНА!')
#     bot.browser()
#     bot.browser.maximize_window()
#     bot.switch_to_window('MetaMask')
#     bot.browser.close()
#     bot.switch_to_main()
#     bot.go_login()
#     bot.login()
#     time.sleep(3)
#     bot.captcha()
#     bot.should_be_discrod_page()
#     bot.close_popup()
#     bot.resend_verification_letter()
#     bot.resend_verification_letter()
#     bot.get_verification_link()
#     # input('Проверка почты!!!!:')
#     assert bot.should_be_success_verification(),'ошибка дискорда!'
#     print('УСПЕШНО ЗАШЕЛ В ДИСКОРД!!')
#
#     # bot.go_discord()
#     bot.run_metamask()
#     bot.go_reflink()
#     bot.run_planet()
#     bot.connect_discord2()
#     bot.run_discord_verification()
#     bot.input_email()
#     bot.run_email_verification()
#     bot.go_finish()
#     bot.finish()

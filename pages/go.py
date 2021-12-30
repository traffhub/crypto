from pages.metamask import Lions
from pages.planet import PlanetQuest
from pages.discord import Discord
from pages.elfin import ElfinApi
import time,random
import shutil
from pathlib import Path
from tech_files.rambler_mail import MailConfirm
import threading
from selenium.webdriver.common.by import By
from selenium.common.exceptions import InvalidCookieDomainException,WebDriverException,NoSuchWindowException,ElementClickInterceptedException

import string,random
class Run(Discord,PlanetQuest,ElfinApi):
    def save_bad_email(self):
        # profile_path = fr'D://crypto//chrome_profile//{self.email}"'
        filename = r'D:\документы\planet\bad_email.txt'
        data = f'{self.discord_email},{self.discord_pass},{self.email},{self.email_pass}\n'
        with open(filename, 'a') as ua_file:
            ua_file.write(data)
        # self.browser.quit()
        # shutil.rmtree(Path(profile_path))

accaunts_path = r'D:\Загрузки\order_22851925_183363c5d9503e70ff131fba39d7a65c_26.12.2021_18-19.txt'

def get_first_user(file):
    with open(file,'r') as f:
        Lines = f.readlines()
    with open(file, 'w') as f:
        for l in Lines[1:]:
            f.write(l)
    print(len(Lines))
    return Lines[0].replace('\n','')

# def run():
# acc = get_first_user(accaunts_path)
# bot = Run()
# bot.get_dicord_acc(acc)
#
# if MailConfirm(bot.email,bot.email_pass).check_connection() is False:
#     bot.save_bad_email()
# else:
#     print('ПОЧТА АКТИВНА!')
# bot.browser()
# time.sleep(3)
# bot.close_foxy_proxy()
# bot.set_foxy_proxy('hub-us-5.litport.net','31337','mk6qEu','rw1ukP')
# # bot.browser.maximize_window()
# # bot.switch_to_window('MetaMask')
# # bot.browser.close()
# # bot.switch_to_main()
# bot.go_login()
# bot.login()
# time.sleep(3)
# bot.captcha()
# bot.should_be_discrod_page()
# bot.close_popup()
# bot.resend_verification_letter()
# bot.resend_verification_letter()
# bot.get_verification_link()
# if bot.should_be_success_verification():
#     print('УСПЕШНО ЗАШЕЛ В ДИСКОРД!!')
# bot.go_discord()
# bot.run_metamask()
# bot.go_reflink()
# bot.connect_metamask()
# bot.run_planet()
# bot.connect_discord2()
# bot.run_discord_verification()
# bot.input_email()
# bot.run_email_verification()
# bot.go_finish()
#
# bot.go_tokentrove()
# bot.bypass_metamask_window(connect=True)
# # assert bot.metamask_should_connect(), 'Метамаск не подключен!'
# time.sleep(15)
# bot.go_Planet_collection()
# assert bot.should_be_item(), 'Нет айтема!'
# bot.transfer_item()
# bot.bypass_immutable()
# time.sleep(20)
# assert bot.should_be_success_transfer()
# bot.finish()




def open_profile(email):
    bot = Run()
    bot.email = email




# for _ in range(1):
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
#     bot.close_metamask_window()
#     bot.go_login()
#     bot.login()
#     time.sleep(3)
#     bot.captcha()
#     bot.should_be_discrod_page()
#     bot.close_popup()
#     bot.resend_verification_letter()
#     bot.resend_verification_letter()
#     bot.get_verification_link()
#     assert bot.should_be_success_verification(),'ошибка дискорда!'
#     print('УСПЕШНО ЗАШЕЛ В ДИСКОРД!!')
#
#     # bot.bypass_metamask_window(True)
#
#
#     bot.go_discord()
#     bot.run_metamask()
#     bot.go_reflink()
#     bot.connect_wallet_2()
#     bot.choose_fraction()
#     bot.connect_discord2()
#     bot.run_discord_verification()
#     bot.input_email()
#     bot.run_email_verification()
#     bot.go_finish()
#     bot.finish()



# for _ in range(1):
#     # time.sleep(60)
#     bot = Run()
#
#     bot.get_old_profile()
#     bot.find_data()
#     bot.get_useragent()
#     bot.browser()
#     time.sleep(10)
#     # bot.wait_fot_window_with_domain('google.com',timeout=30)
#     bot.close_foxy_proxy()
#     # bot.set_foxy_proxy('hub-us-5.litport.net','31337','mk6qEu','rw1ukP')
#     bot.login_by_password()
#     # bot.go_reflink()
#
#     bot.browser.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#settings/networks')
#
#     send = (By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[1]/div/button')
#     send1 = (By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/label/input')
#     send2 = (By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/label/input')
#     send3 = (By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/label/input')
#     send4 = (By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[4]/label/input')
#     send5 = (By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[5]/label/input')
#     bot.click_element(*send)
#
#     bot.send_keys_element(*send1,'Binance Smart Chain Mainnet')
#     bot.send_keys_element(*send2,'https://bsc-dataseed1.ninicoin.io')
#     bot.send_keys_element(*send3,'56')
#     bot.send_keys_element(*send4,'BNB')
#     bot.send_keys_element(*send5,'https://bscscan.com/')
#
#     send66 = (By.XPATH, '')
#     send6 = (By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[3]/button[2]')
#     bot.click_element(*send6)
#     input('Добавь Монет!')
#     bot.browser.get('https://elfinkingdom.com/home')
#     login = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[2]/button')
#     bot.wait_and_click(*login)
#     meta_w = (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div/div')
#     bot.wait_and_click(*meta_w)
#     bot.bypass_metamask_window(True)
#     bot.browser.get('https://game.elfinkingdom.com/')
#
#     # connect = (By.XPATH, '')
#     # send66 = (By.XPATH, '')
#     # send66 = (By.XPATH, '')
#     # send66 = (By.XPATH, '')
#


def market():
    bot.browser.get('https://tofunft.com')



def do():
    try:
        bot = Run()
        data = get_first_user(r'C:\Users\Admin\PycharmProjects\crypto\wallet.txt')
        bot.email_pass = data.split(',')[0]
        bot.secret = data.split(',')[1]
        bot.browser()

        time.sleep(5)
        bot.close_foxy_proxy()
        bot.import_wallet(bot.email_pass,bot.secret)

        bot.browser.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#settings/networks')
        send = (By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[1]/div/button')
        send1 = (By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/label/input')
        send2 = (By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/label/input')
        send3 = (By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[3]/label/input')
        send4 = (By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[4]/label/input')
        send5 = (By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[5]/label/input')
        bot.click_element(*send)
        bot.send_keys_element(*send1,'Binance Smart Chain Mainnet')
        bot.send_keys_element(*send2,'https://bsc-dataseed1.ninicoin.io')
        bot.send_keys_element(*send3,'56')
        bot.send_keys_element(*send4,'BNB')
        bot.send_keys_element(*send5,'https://bscscan.com/')
        send66 = (By.XPATH, '')
        send6 = (By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div/div[2]/div/div[3]/button[2]')
        bot.click_element(*send6)
        bot.browser.set_window_size(300,650)
        print('Создал кошелек!')
        input('Добавь Монет!')
        bot.browser.get('https://elfinkingdom.com/home')
        login = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[2]/button')
        bot.wait_and_click(*login)
        meta_w = (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div/div')
        bot.wait_and_click(*meta_w)
        bot.bypass_metamask_window(True)
        bot.browser.get('https://game.elfinkingdom.com/')
        print('Закончил!')
    except Exception:
        print('Возникла ошибка!!!')
        input('')

    input('Завершить работу!')

def go_nft():
    bot.browser.get('https://elfinkingdom.com/home')
    login = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[2]/button')
    bot.wait_and_click(*login)
    meta_w = (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div/div')
    bot.wait_and_click(*meta_w)
    bot.bypass_metamask_window(True)
    bot.browser.get('https://game.elfinkingdom.com/')
    bot.wait_for_element(By.CSS_SELECTOR,'#GameCanvas',30)
    time.sleep(20)
    # bot.go_tokentrove()
    # bot.bypass_metamask_window(connect=True)
    # # assert bot.metamask_should_connect(), 'Метамаск не подключен!'
    # time.sleep(3)
    # bot.go_Planet_collection()
    # assert bot.should_be_item(), 'Нет айтема!'
    # bot.transfer_item()
    # bot.bypass_immutable()
    # # time.sleep(20)
    # # assert bot.should_be_success_transfer()
    #
    # bot.go_lions()
    # bot.auth_discord()
    # bot.vetify_discord()
    # bot.claim()
    # bot.open_pack()
    #
    # bot.browser.quit()
    # bot.replace_profile_folder(r'D:\crypto\lions')
def click_potato():
    for _ in range(2):
        potato = (By.CSS_SELECTOR, '.field')
        for i in bot.browser.find_elements(*potato):
            try:
                i.click()
            except ElementClickInterceptedException:
                break
            time.sleep(0.1)

# def check_timer():
#     timer = bot.browser.find_element_by_css_selector('#timer').text
#     timer = timer.split(':')
#     if int(timer[0]) == 0 and int(timer[0]) ==0:
#         print('Закончил таймер!')
#     else:
#         print('Жду!')


def save():
    save = (By.XPATH, "//*[contains(text(),'Times up')]")
    while not bot.is_element_presented(*save):
        click_potato()
        time.sleep(1)
    else:
        # save_but = (By.XPATH, "//div[@class='button' and contains(text(),'Save')]")
        # bot.click_element(*save_but)
        # bot.bypass_metamask_window(False,False)
        # saving_txt = (By.XPATH, "//*[contains(text(),'Saving...')]")
        # while bot.is_element_presented(*saving_txt):
        #     time.sleep(1)
        # click_potato()
        # click_potato()
        print('Закончил!')
        # while bot.is_element_presented(*saving_but):
        #     time.sleep(1)

def try_save():
    save_but = (By.XPATH, "//div[@class='button' and contains(text(),'Save')]")
    bot.click_element(*save_but)

def check_transaction():
    save_but = (By.XPATH, "//div[@class='button' and contains(text(),'Save')]")
    bot.click_element(*save_but)
    time.sleep(2)
    bot.switch_to_window('MetaMask')
    price = (By.XPATH, "//span[@class='currency-display-component__text']")
    total = bot.browser.find_element(*price).text
    total = float(total)
    if total > 0.1:
        print('Ошибка транзакции')
        bot.browser.close()
        bot.switch_to_main()
    else:
        bot.bypass_metamask_window(False,False)
def swipe():
    bot.switch_to_window_by_domain('quickswap.exchange')
    but = (By.XPATH,'//*[@id="swap-currency-input"]/div/div[2]/button[1]')
    bot.click_element(*but)
    time.sleep(1)
    but2 = (By.XPATH, "//div[contains(text(),'Enter an amount')]")
    bot.click_element(*but2)

def input_sff():
    input = (By.XPATH,'//*[@id="swap-currency-output"]/div/div[2]/input')
    bot.send_keys_element(*input,0.36)

def click_connect():
    but = (By.XPATH, "//*[contains(text(),'Connect to a wallet')]")
    bot.click_element(*but)
    but2 = (By.CSS_SELECTOR, "#connect-METAMASK")
    bot.wait_and_click(*but2)
    bot.bypass_metamask_window(True,False)

def bypass_popup():
    but = (By.XPATH, "/html/body/reach-portal/div[3]/div/div/div/div/div/div[6]/div/label/input")
    bot.click_element(*but)
    time.sleep(1)
    but1 = (By.XPATH, "//div[contains(text(),'Continue')]")
    bot.click_element(*but1)
    time.sleep(1)

def click_swipe():
    but = (By.XPATH, '//*[@id="swap-button"]')
    bot.click_element(*but)
    but2 = (By.XPATH, '//*[@id="confirm-swap-or-send"]')
    bot.wait_and_click(*but2)
    error = (By.XPATH, "//*[contains(text(),'Error')]")
    if bot.is_element_presented(*error):
        cancel = (By.XPATH, '/html/body/reach-portal[4]/div[3]/div/div/div/div/div[2]/button')
        bot.click_element(*cancel)
    else:
        bot.bypass_metamask_window(False,False)
    ok = (By.XPATH, "//*[contains(text(),'Transaction Submitted')]")
    if bot.is_element_presented(*ok):
        print('Успешно!')

def go_game():
    bot.browser.get('https://sunflower-farmers.com/play/')

def start_game():
    start = (By.XPATH, "//span[contains(text(),'Get Started')]")
    bot.wait_and_click(*start)
    bot.bypass_metamask_window(True, False)
    number = (By.XPATH, '//*[@id="donation-input"]')
    bot.wait_for_element(*number)
    bot.browser.find_element(*number).clear()
    bot.send_keys_element(*number,'0,1')
    donate = (By.XPATH, "//div[contains(text(),'Donate & Play')]")
    bot.click_element(*donate)
    bot.bypass_metamask_window(False,False)
    creating = (By.XPATH, "//*[contains(text(),'Creating')]")
    while bot.is_element_presented(*creating):
        time.sleep(1)

# for _ in range(1):
#     data = get_first_user(r'C:\Users\Admin\PycharmProjects\crypto\wallet.txt')
#     bot = Run()
#     bot.email_pass = data.split(',')[0]
#     bot.secret = data.split(',')[1]
#     bot.browser()
#     # except WebDriverException:
#     #     pass
#     time.sleep(5)
#     bot.close_foxy_proxy()
#     bot.import_wallet(bot.secret,bot.email_pass)
#     bot.network(type='MATIC')
#     bot.get_wallet()
#     bot.browser.set_window_size(516, 378)
#     go_nft()
#     # secret_inpit = (By.XPATH, "//input")
#     # bot.send_keys_element(*secret_inpit, bot.secret)
#     bot.click_start_game()
#     time.sleep(2)
#     bot.click_connect_metamask()
#     time.sleep(2)
#     bot.bypass_metamask_window(True,True)
#     # bot.type_name()
#     # time.sleep(2)
#     # bot.bypass_metamask_window(False)
#     time.sleep(10)
#     # bot.address = '0x9054b3CBF868366FD6b7376b412Adf4Fd6eB9e78'
#     bot.do_taks()
#     bot.get_pokemon()
#     if bot.pokemons() == False:
#         bot.browser.close()
#         bot.browser.quit()
#         continue
#     else:
#         print(bot.secret)
#         print(bot.address)
#         print('ПОЙМАЛИ ПОЛУЧАЕТСЯ!!')
#         input('Нажми ENTER когда разбеершься!')
#         bot.browser.close()
#         bot.browser.quit()

data = get_first_user(r'C:\Users\Admin\PycharmProjects\crypto\wallet.txt')
bot = Run()
bot.email_pass = data.split(',')[0]
bot.secret = data.split(',')[1]
bot.browser()
time.sleep(5)
bot.close_foxy_proxy()
bot.import_wallet(bot.secret,bot.email_pass)
bot.network(type='MATIC')
bot.get_wallet()
bot.add_token()
print(bot.address)
input('Нажми ENTER когда переведешь')
bot.browser.get('https://quickswap.exchange/#/swap?outputCurrency=0xdf9B4b57865B403e08c85568442f95c26b7896b0')
bypass_popup()
click_connect()
input_sff()
input('Нажми ENTER когда переведешь')


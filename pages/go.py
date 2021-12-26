from pages.metamask import Lions
from pages.planet import PlanetQuest
from pages.discord import Discord
import time,random
import shutil
from pathlib import Path
from tech_files.rambler_mail import MailConfirm
import threading
from selenium.webdriver.common.by import By

class Run(Discord,PlanetQuest,Lions):
    def save_bad_email(self):
        # profile_path = fr'D://crypto//chrome_profile//{self.email}"'
        filename = r'D:\документы\planet\bad_email.txt'
        data = f'{self.discord_email},{self.discord_pass},{self.email},{self.email_pass}\n'
        with open(filename, 'a') as ua_file:
            ua_file.write(data)
        # self.browser.quit()
        # shutil.rmtree(Path(profile_path))

accaunts_path = r'D:\Загрузки\order_22825363_b95ac602e1bfd8afa21f401455bbcb13_22.12.2021_02-17.txt'

def get_first_user(file):
    with open(file,'r') as f:
        Lines = f.readlines()
    with open(file, 'w') as f:
        for l in Lines[1:]:
            f.write(l)
    print(len(Lines))
    return Lines[0].replace('\n','')

def run():
    acc = get_first_user(accaunts_path)
    bot = Run()
    bot.get_dicord_acc(acc)

    if MailConfirm(bot.email,bot.email_pass).check_connection() is False:
        bot.save_bad_email()
        return
    else:
        print('ПОЧТА АКТИВНА!')
    bot.browser()
    bot.browser.maximize_window()
    bot.switch_to_window('MetaMask')
    bot.browser.close()
    bot.switch_to_main()
    bot.go_login()
    bot.login()
    time.sleep(3)
    bot.captcha()
    bot.should_be_discrod_page()
    bot.close_popup()
    bot.resend_verification_letter()
    bot.resend_verification_letter()
    bot.get_verification_link()
    if bot.should_be_success_verification():
        print('УСПЕШНО ЗАШЕЛ В ДИСКОРД!!')
    # bot.go_discord()
    bot.run_metamask()
    bot.go_reflink()
    bot.run_planet()
    bot.connect_discord2()
    bot.run_discord_verification()
    bot.input_email()
    bot.run_email_verification()
    bot.go_finish()
    bot.finish()

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



for _ in range(1):
    # time.sleep(60)
    bot = Run()
    bot.get_old_profile()
    bot.find_data()
    bot.get_useragent()
    bot.browser()
    time.sleep(10)
    # bot.wait_fot_window_with_domain('google.com',timeout=30)
    bot.close_foxy_proxy()
    # bot.set_foxy_proxy('hub-us-5.litport.net','31337','mk6qEu','rw1ukP')
    bot.login_by_password()
    # bot.go_reflink()

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
    input('Добавь Монет!')
    bot.browser.get('https://elfinkingdom.com/home')
    login = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[2]/button')
    bot.wait_and_click(*login)
    meta_w = (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div/div')
    bot.wait_and_click(*meta_w)
    bot.bypass_metamask_window(True)
    bot.browser.get('https://game.elfinkingdom.com/')

    # connect = (By.XPATH, '')
    # send66 = (By.XPATH, '')
    # send66 = (By.XPATH, '')
    # send66 = (By.XPATH, '')



def market():
    bot.browser.get('https://tofunft.com')


def do():
    bot = Run()
    bot.browser()
    time.sleep(10)
    bot.close_foxy_proxy()
    bot.run_metamask()

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
    input('Добавь Монет!')
    bot.browser.get('https://elfinkingdom.com/home')
    login = (By.XPATH, '//*[@id="__layout"]/div/div[1]/div/div[2]/button')
    bot.wait_and_click(*login)
    meta_w = (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div/div')
    bot.wait_and_click(*meta_w)
    bot.bypass_metamask_window(True)
    bot.browser.get('https://game.elfinkingdom.com/')




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

from pages.metamask import MetaMask
from pages.planet import PlanetQuest
from pages.discord import Discord
from pages.phantom import PhantomWallet,Meanfi

import time,random
import shutil
from pathlib import Path
from tech_files.rambler_mail import MailConfirm
import threading
from selenium.webdriver.common.by import By

class Run(PhantomWallet,Meanfi):
    def save_info(self):
        profile_path = rf'D://crypto//chrome_profile//{self.email}//phantom.txt'
        data = f'{self.email},{self.email_pass},{self.phantom_secret}\n'
        with open(profile_path, 'w') as ua_file:
            ua_file.write(data)

        filename = r'D:\crypto\wallet\data.txt'
        data = f'{self.email},{self.email_pass},{self.phantom_secret}\n'
        with open(filename, "a") as file:
            file.write(data)


for _ in range(1):
    bot = Run()
    bot.get_old_profile()
    bot.find_data()
    bot.get_useragent()
    bot.browser()
    bot.create_wallet()
    bot.go_reflint()

    bot.connect_wallet()
    bot.bypass_connection()

    # bot.save_info()
    # bot.browser.quit()
    # bot.replace_profile_folder(new_folder=r'D:\crypto\wallet')
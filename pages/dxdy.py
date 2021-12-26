from pages.metamask import MetaMask
from pages.planet import PlanetQuest
from pages.discord import Discord
import time,random
import shutil
from pathlib import Path
from tech_files.rambler_mail import MailConfirm
import threading
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

def etherium_addr():
    from secrets import token_bytes
    from coincurve import PublicKey
    from sha3 import keccak_256
    private_key = keccak_256(token_bytes(32)).digest()
    public_key = PublicKey.from_valid_secret(private_key).format(compressed=False)[1:]
    addr = keccak_256(public_key).digest()[-20:]
    addr = '0x'+addr.hex()
    return addr

class Bot(BasePage):
    def go(self):
        self.browser.get('https://dxdy.finance/JSDFRBB')
        airdrop = (By.XPATH, "//span[text()='Airdrop']")
        self.wait_and_click(*airdrop)
        time.sleep(2)
        input_adress = (By.XPATH, "//input[@name='address']")
        self.send_keys_element(*input_adress, etherium_addr())
        claim = (By.XPATH, "//span[text()='Claim']")
        self.click_element(*claim)
        time.sleep(2)
        self.browser.quit()
for _ in range(7):
    bot = Bot()
    bot.random_ua()
    bot.browser()
    bot.go()
from pages.metamask import Lions
from selenium.webdriver.common.by import By

from pages.discord import Discord


class Lion(Lions,Discord):
    pass

for _ in range(5):
    bot = Lion()
    # bot.email = 'zayatdinovnazar1998@rambler.ru'
    bot.get_old_profile()
    bot.find_data()
    bot.browser()
    bot.close_foxy_proxy()
    bot.set_foxy_proxy('hub-us-5.litport.net','31337','mk6qEu','rw1ukP')
    bot.login_by_password()
    # bot.go_lions('https://collectibles.lazylionsnft.com')
    bot.go_lions('https://invites.lazylionsnft.com/i/QRF6')
    bot.auth_discord()
    bot.vetify_discord()
    bot.claim()
    bot.open_pack()
    bot.browser.quit()
    bot.replace_profile_folder(r'D:\crypto\lions')
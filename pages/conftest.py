from selenium import webdriver
from tech_files.ways import BROWSER_PATH
import time,random,json,pickle
from selenium.common.exceptions import InvalidCookieDomainException
from pathlib import Path

class Bot:
    def __init__(self,new_profile=False):
        self.new_profile = new_profile
    #     DB.__init__(self)
    def get_dicord_acc(self,data):
        self.discord_email = data.split(':')[0]
        self.discord_pass = data.split(':')[1]
        self.email = data.split(':')[2]
        self.email_pass = data.split(':')[3]

        print(f'Взял данные:\n{self.discord_email},{self.discord_pass},{self.email},{self.email_pass}')

    def save_useragent(self):
        profile_path = rf'D://crypto//chrome_profile//{self.email}//useragent.txt'
        with open(profile_path, 'w') as ua_file:
            ua_file.write(self.user_agent)

    def save_info(self):
        profile_path = rf'D://crypto//chrome_profile//{self.email}//info.txt'
        data = f'{self.discord_email},{self.discord_pass},{self.email},{self.email_pass},{self.secret}\n'
        with open(profile_path, 'w') as ua_file:
            ua_file.write(data)

        filename = r'D:\документы\planet\accs.txt'
        data = f'{self.email},{self.email_pass},{self.secret}\n'
        with open(filename, "a") as file:
            file.write(data)

    def random_ua(self):
        with open(r'files/useragents.txt', 'r') as file:
            ua_list = file.read().split('\n')

        self.user_agent =random.choice(ua_list)

    def get_useragent(self):
        profile_path = rf'D://crypto//chrome_profile//{self.email}//useragent.txt'
        # profile_path = rf'D://crypto//wallet//{self.email}//useragent.txt'

        if Path(profile_path).exists():
            with open(profile_path, 'r') as ua_file:
                self.user_agent = ua_file.read()
        else:
            self.random_ua()
    def find_data(self):
        profile_path = rf'D://crypto//chrome_profile//{self.email}//info.txt'
        # profile_path = rf'D://crypto//wallet//{self.email}//info.txt'

        all_data_path = r'D:\документы\planet\accs.txt'

        if Path(profile_path).exists():
            with open(profile_path, 'r') as info:
                info = info.read().split(',')
                self.email = info[0]
                self.email_pass = info[3]
                print('Пароль: ',self.email_pass)
                return True
        else:
            with open(all_data_path, 'r') as info:
                info = info.readlines()
                for line in info:
                    if self.email in line:
                        self.email_pass = line.split(',')[1]
                        print('Пароль: ', self.email_pass)
                        return True
        return False

    def replace_profile_folder(self,new_folder=r'D:\crypto\done'):
        profile_path = Path(rf'D://crypto//chrome_profile//{self.email}')
        # profile_path = Path(rf'D://crypto//wallet//{self.email}')
        profile_path.replace(Path(new_folder).joinpath(profile_path.parts[-1]))

    def get_old_profile(self):
        profile_path = Path(rf'D://crypto//chrome_profile')
        # profile_path = Path(rf'D://crypto//wallet')

        self.email = sorted(Path(profile_path).iterdir(), key=lambda f: f.stat().st_mtime)[0].parts[-1]
        print('Взял профиль: ', self.email)
    def browser(self):
        print("\nstart chrome browser for test..")

        self.random_ua()

        options = webdriver.ChromeOptions()
        options.binary_location = BROWSER_PATH.CHROME_BINARY
        options.headless = False
        options.add_argument(f"--lang=ru-RU")
        options.add_argument(f"−−mute−audio")
        options.add_argument("--disable-popup-blocking")
        options.add_argument('--no-sandbox')
        options.add_argument("--disable-automation")
        # options.add_argument("--disable-default-apps")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-window")
        # options.add_argument("--incognito")
        # options.add_argument("--start-maximized")
        options.add_experimental_option("excludeSwitches", ["enable-automation","enable-logging"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument(f"user-agent={self.user_agent}")
        # options.add_argument(f"--proxy-server=socks5://{self.proxy['ip']}:{self.proxy['socks_auth_port']}")
        # options.add_argument(f"--proxy-server=socks5://2.56.139.3:63495")
        preferences = {
            "webrtc.ip_handling_policy": "disable_non_proxied_udp",
            "webrtc.multiple_routes_enabled": False,
            "webrtc.nonproxied_udp_enabled": False,
            "profile.managed_default_content_settings.images":1,
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
        }

        # prefs = {"protocol_handler": {"excluded_schemes": {"<INSERT PROTOCOL NAME>": "false"}}}
        # options.add_experimental_option("prefs", prefs)
        options.add_experimental_option("prefs", preferences)


        # options.add_argument("window-size=960,1080")
        if self.new_profile is True:
            options.add_argument(f"user-data-dir=D://crypto//chrome_profile//{self.email}")
        options.add_extension(r'files\anticaptcha-plugin_v0.60.crx')
        options.add_extension(r'files\metamask.crx')
        # options.add_extension(r'files\Phantom.crx')
        # options.add_extension(r'files\FoxyProxy.crx')

        self.browser = webdriver.Chrome(executable_path=BROWSER_PATH.CHROME_DRIVER_BINARY, options=options)
        self.browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
                  const newProto = navigator.__proto__
                  delete newProto.webdriver
                  navigator.__proto__ = newProto
                  """
        })
        # self.save_useragent()
        self.send_captcha_key()
        self.browser.set_window_size(1080, 1080)

        # self.browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        #     "source": """
        #           window.addEventListener('load', function() {
        #                     navigator.serviceWorker.register('/sw.js');
        #                 });
        #           """
        # })

        #self.browser.set_window_size(1024, 1024)
        # self.browser.set_page_load_timeout(30)
        # time.sleep(3)
        # self.close_foxy_proxy()
        # self.close_foxy_proxy()

    def close_all_tabs(self):
        tabs = self.browser.window_handles
        tabs.pop(0)
        while not len(self.browser.window_handles)==1:
            for handle in tabs:
                self.browser.switch_to.window(handle)
                if not 'google' in self.browser.current_url:
                    self.browser.close()
        self.browser.switch_to.window(self.browser.window_handles[0])

    def load_cookies_case(self,cookie):
        for c in cookie:
            self.browser.add_cookie(c)

    def send_captcha_key(self):
        self.browser.get('https://www.google.com/')
        message = {
            'receiver': 'antiCaptchaPlugin',
            'type': 'setOptions',
            'options': {'antiCaptchaApiKey': 'b22d2051ae8c9eb398bd484b4c89307d'}
        }
        return self.browser.execute_script("""
            return window.postMessage({});
            """.format(json.dumps(message)))

    def save_cookies(self):
        cookie_path = rf'files\cookie\{self.email}.txt'
        pickle.dump(self.browser.get_cookies(), open(cookie_path, "wb"))

    def load_cookies(self,account):
        COOKIE_FILE_PATH = rf'files\cookie\{account}.txt'
        cookies = pickle.load(open(COOKIE_FILE_PATH, "rb"))
        # have to be on a page before you can add any cookies, any page - does not matter which
        url = f"http://{cookies[0]['domain']}"
        try:
            for cookie in cookies:
                if isinstance(cookie.get('expiry'), float):  # Checks if the instance expiry a float
                    cookie['expiry'] = int(cookie['expiry'])  # it converts expiry cookie to a int
                self.browser.add_cookie(cookie)
            self.browser.refresh()
            return True
        except(InvalidCookieDomainException):
            print('Cookies may only be set for the current domain!!!')
            # self.browser.get(url)

    def set_foxy_proxy(self,ip,port,user,login):
        time.sleep(2)
        self.browser.get('chrome-extension://gcknhkkoolaabfmlnjonogaaifnjlfnp/options.html#tabProxies')
        time.sleep(1)
        self.browser.find_element_by_css_selector('#addNewProxy > span').click()
        self.browser.find_element_by_css_selector('#proxyHost').send_keys(ip)
        self.browser.find_element_by_css_selector('#proxyPort').clear()
        self.browser.find_element_by_css_selector('#proxyPort').send_keys(port)
        self.browser.find_element_by_css_selector('#authCheck').click()
        self.browser.find_element_by_css_selector(
            'body > div:nth-child(21) > div.ui-dialog-buttonpane.ui-widget-content.ui-helper-clearfix > div > button:nth-child(1) > span').click()
        self.browser.find_element_by_css_selector('#authBox > input:nth-child(3)').send_keys(user)
        self.browser.find_element_by_css_selector('#authBox > input[type=password]:nth-child(5)').send_keys(login)
        self.browser.find_element_by_css_selector('#authBox > input[type=password]:nth-child(7)').send_keys(login)
        self.browser.find_element_by_css_selector('body > div:nth-child(19) > div.ui-dialog-buttonpane.ui-widget-content.ui-helper-clearfix > div > button:nth-child(1) > span').click()
        time.sleep(0.5)
        self.browser.find_element_by_css_selector('#proxyModeGlobal > option:nth-child(2)').click()

    def close_foxy_proxy(self):
        while len(self.browser.window_handles)>1:
            tabs = self.browser.window_handles
            for tab in tabs:
                self.browser.switch_to.window(tab)
                self.browser.execute_script('window.stop()')
                # print(self.browser.title)
                # print(self.browser.current_url)
                if 'FoxyProxy' in self.browser.title or 'foxy' in self.browser.title or 'foxy' in self.browser.current_url or 'chrome-extension://' in self.browser.current_url:
                    # print('Удаляю')
                    self.browser.close()
                    tabs.remove(tab)
        self.browser.switch_to.window(self.browser.window_handles[0])

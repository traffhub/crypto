from selenium.webdriver.common.by import By
from pages.metamask import MetaMask
import requests,json,time
from selenium.webdriver.common.action_chains import ActionChains
import names

class Elfin(MetaMask):

    def click_start_game(self):
        el = self.browser.find_element_by_css_selector('#GameCanvas')
        self.click_by_actions(el,0,100)

    def click_connect_metamask(self):
        el = self.browser.find_element_by_css_selector('#GameCanvas')
        self.click_by_actions(el,0,0)

    def type_name(self):
        el = self.browser.find_element_by_css_selector('#GameCanvas')
        ActionChains(self.browser).move_to_element(el).move_by_offset(-200,0).click().send_keys(names.get_first_name()).perform()
        time.sleep(1)
        self.click_by_actions(el,-115,25)
# class ElfinApi(Elfin):
#     def __init__(self,adress,user_agent,cookie):
#         self.address = adress
#         self.session = requests.Session()
#         self.user_agent = user_agent
#         self.cookies = cookie
#     def update(self):
#         self.set_headesr()
#         self.set_cookie()
#
#     def set_headesr(self):
#         headers= {
#             "sec-ch-ua": " Not A;Brand;v=99, Chromium;v=96, Google Chrome;v=96",
#             "sec-ch-ua-mobile": "?0",
#             "sec-ch-ua-platform": "Windows",
#             "upgrade-insecure-requests": "1",
#             'user-agent':self.user_agent
#         }
#         self.session.headers.update(headers)
#
#     def set_cookie(self):
#         for cookie in self.cookies:
#             self.session.cookies.set(cookie['name'],cookie['value'])
#         print('Установил куки!')
#
#     def all(self):
#
#         url = 'https://game.elfinkingdom.com/api/daily/all'
#
#         headers={
#                 "accept": "*/*",
#                 "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
#                 "address": self.address,
#                 "content-type": "application/json;charset=UTF-8",
#                 "language": "en",
#                 "sec-ch-ua": "Not A;Brand;v=99, Chromium;v=96, Google Chrome;v=96",
#                 "sec-ch-ua-mobile": "?0",
#                 "sec-ch-ua-platform": "Windows",
#                 "sec-fetch-dest": "empty",
#                 "sec-fetch-mode": "cors",
#                 "sec-fetch-site": "same-origin",
#                 "cookie": "_ga=GA1.1.1789498835.1640657265; _ga_9V1QCDJN68=GS1.1.1640657264.1.1.1640657960.0",
#                 "Referer": "https://game.elfinkingdom.com/",
#                 "Referrer-Policy": "strict-origin-when-cross-origin"
#             }
#
#
#         r = self.session.get(url,headers=headers)
#         data = json.loads(r.text)
#         print(data)
#         if data['code'] == '000000':
#             print('Успешно!')
#         tasks = data['result']['tasks']
#         telegram_task_id = [i['id'] for i in tasks if 'telegram' in i['name']]
#         twitter_task_id = [i['id'] for i in tasks if 'twitter' in i['name']]
#         print(tasks)
#         print('telegram: ',telegram_task_id)
#         print('twitter: ',twitter_task_id)
#
#     def set_complite(self,task_id):
#         url = f'https://game.elfinkingdom.com/api/daily/task/{task_id}/setComplete'
#
#         headers= {
#                 "accept": "*/*",
#                 "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
#                 "address": "0x0e1f4625bb721c68a46abf74b75267ca350fbb15",
#                 "content-type": "application/json;charset=UTF-8",
#                 "language": "en",
#                 "sec-ch-ua": " Not A;Brand;v=99, Chromium;v=96, Google Chrome;v=96",
#                 "sec-ch-ua-mobile": "?0",
#                 "sec-ch-ua-platform": "Windows",
#                 "sec-fetch-dest": "empty",
#                 "sec-fetch-mode": "cors",
#                 "sec-fetch-site": "same-origin",
#             "cookie": "_ga=GA1.1.1789498835.1640657265; _ga_9V1QCDJN68=GS1.1.1640657264.1.1.1640657960.0",
#             "Referer": "https://game.elfinkingdom.com/",
#                 "Referrer-Policy": "strict-origin-when-cross-origin"
#             }
#
#         s = requests.Session()
#         r = self.session.put(url,headers=headers)
#         data = json.loads(r.text)
#         if data['code'] == '000000':
#             print('Успешно!')
#
#     def takeReward(self,task_id):
#         url = f'https://game.elfinkingdom.com/api/daily/task/{task_id}/takeReward'
#         headers= {
#                 "accept": "*/*",
#                 "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
#                 "address": "0x0e1f4625bb721c68a46abf74b75267ca350fbb15",
#                 "content-type": "application/json;charset=UTF-8",
#                 "language": "en",
#                 "sec-ch-ua": " Not A;Brand;v=99, Chromium;v=96, Google Chrome;v=96",
#                 "sec-ch-ua-mobile": "?0",
#                 "sec-ch-ua-platform": "Windows",
#                 "sec-fetch-dest": "empty",
#                 "sec-fetch-mode": "cors",
#                 "sec-fetch-site": "same-origin",
#                  "cookie": "_ga=GA1.1.1789498835.1640657265; _ga_9V1QCDJN68=GS1.1.1640657264.1.1.1640657960.0",
#                 "Referer": "https://game.elfinkingdom.com/",
#                 "Referrer-Policy": "strict-origin-when-cross-origin"
#             }
#         r = self.session.put(url,headers=headers)
#         data = json.loads(r.text)
#         if data['code'] == '000000':
#             print('Успешно!')
#
#     def do_taks(self,task_id):
#         self.set_complite(task_id)
#         time.sleep(30)
#         self.takeReward(task_id)
#
#     def items(self):
#         url = 'https://game.elfinkingdom.com/api/items'
#         headers = {
#             "accept": "*/*",
#             "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
#             "address": self.address,
#             "content-type": "application/json;charset=UTF-8",
#             "language": "en",
#             "sec-ch-ua": " Not A;Brand;v=99, Chromium;v=96, Google Chrome;v=96",
#             "sec-ch-ua-mobile": "?0",
#             "sec-ch-ua-platform": "Windows",
#             "sec-fetch-dest": "empty",
#             "sec-fetch-mode": "cors",
#             "sec-fetch-site": "same-origin",
#             "cookie": "_ga=GA1.1.1789498835.1640657265; _ga_9V1QCDJN68=GS1.1.1640657264.1.1.1640657960.0",
#             "Referer": "https://game.elfinkingdom.com/",
#             "Referrer-Policy": "strict-origin-when-cross-origin"
#         }
#         r = self.session.get(url,headers=headers)
#         data = json.loads(r.text)
#         if data['code'] == '000000':
#             print('Успешно!')
#         if len(data['result']>0):
#             print('Есть свободные мячи. Можно ловить!')
#
#     def comeAcross(self):
#         url = 'https://game.elfinkingdom.com/api/pokemons/comeAcross'
#         headers= {
#             "accept": "*/*",
#             "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
#             "address": self.address,
#             "content-type": "application/json;charset=UTF-8",
#             "language": "en",
#             "sec-ch-ua": " Not A;Brand;v=99, Chromium;v=96, Google Chrome;v=96",
#             "sec-ch-ua-mobile": "?0",
#             "sec-ch-ua-platform": "Windows",
#             "sec-fetch-dest": "empty",
#             "sec-fetch-mode": "cors",
#             "sec-fetch-site": "same-origin",
#             "cookie": "_ga=GA1.1.1789498835.1640657265; _ga_9V1QCDJN68=GS1.1.1640657264.1.1.1640657960.0",
#             "Referer": "https://game.elfinkingdom.com/",
#             "Referrer-Policy": "strict-origin-when-cross-origin"
#         }
#
#         r = self.session.get(url,headers=headers)
#         data = json.loads(r.text)
#         if data['code'] == '000000':
#             print('Успешно!')
#         fight_id = data['result']['id']
#         print('Бой номер: ',fight_id)
#         pet_name = data['result']['npc']['name']
#         pet_class = data['result']['npc']['skills'][0]['comment']
#         print(f'Персонаж: {pet_name}\n Класс: {pet_class}')
#
#     def catch_pokemon(self,fight_id):
#         url = f'https://game.elfinkingdom.com/api/fights/{fight_id}/action/catchPokemon'
#         headers= {
#             "accept": "*/*",
#             "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
#             "address": self.address,
#             "content-type": "application/json;charset=UTF-8",
#             "language": "en",
#             "sec-ch-ua": " Not A;Brand;v=99, Chromium;v=96, Google Chrome;v=96",
#             "sec-ch-ua-mobile": "?0",
#             "sec-ch-ua-platform": "Windows",
#             "sec-fetch-dest": "empty",
#             "sec-fetch-mode": "cors",
#             "sec-fetch-site": "same-origin",
#             "cookie": "_ga=GA1.1.1789498835.1640657265; _ga_9V1QCDJN68=GS1.1.1640657264.1.1.1640657960.0",
#             "Referer": "https://game.elfinkingdom.com/",
#             "Referrer-Policy": "strict-origin-when-cross-origin"
#         }
#         data = {
#             'itemKey':'ball_level1'
#         }
#         r = self.session.put(url,headers=headers,data=data)
#         data = json.loads(r.text)
#         if data['code'] == '000000':
#             print('Успешно!')
#         result = data['result']
#         if result['code'] == '10036':
#             print('Не поймал!!!')
#         if result['message'] == 'Elfin escaped！':
#             print('Не поймал!!!')
#
#

class ElfinApi(Elfin):
    def my_adress(self,adress):
        self.address = adress

    def make_requset(self,url,headers,method="GET",body='null'):
        script = f'''
        fetch("{url}", {{
          "headers": 
            {str(headers)},
            
            
        "body": {body},
        "method": "{method}"
          }}       
          ).then(response => response.json())
          .then(data => {{return data}});
        '''
        print('Делаю запрос на: ', url)

        result = self.browser.execute_cdp_cmd('Runtime.evaluate',
                                             {'expression': script, 'awaitPromise': True, 'returnByValue': True})
        if 'result' in result.keys():
            result = result['result']
            if 'value' in result.keys():
                result = result['value']
                print('Успешный запрос!')
                if result['code'] == '100045':
                    print(result['message'])
                    time.sleep(30)
                    return self.make_requset(url,headers,method)
                return result

    def user_info(self):
        url = 'https://game.elfinkingdom.com/api/userInfo'
        headers={
                "address": self.address
            }
        data = self.make_requset(url,headers)
        print(data)

    def all(self):

        url = 'https://game.elfinkingdom.com/api/daily/all'

        headers={
                "address": self.address
            }

        data = self.make_requset(url,headers)
        #print(data)
        # if data['code'] == '000000':
        #     print('Успешно!')
        tasks = data['result']['tasks']
        telegram_task_id = [i['id'] for i in tasks if 'telegram' in i['name']][0]
        twitter_task_id = [i['id'] for i in tasks if 'twitter' in i['name']][0]
        #print(tasks)
        return [telegram_task_id,twitter_task_id]
        print('telegram: ',telegram_task_id)
        print('twitter: ',twitter_task_id)

    def set_complite(self,task_id):
        url = f'https://game.elfinkingdom.com/api/daily/task/{task_id}/setComplete'

        headers = {
            "address": self.address
        }

        data = self.make_requset(url,headers,'PUT')
        # if data['code'] == '000000':
        #     print('Успешно!')

    def takeReward(self,task_id):
        url = f'https://game.elfinkingdom.com/api/daily/task/{task_id}/takeReward'
        headers = {
            "address": self.address
        }
        data = self.make_requset(url,headers,'PUT')
        # if data['code'] == '000000':
        #     print('Успешно!')

    def do_taks(self):
        for task in self.all():
            self.set_complite(task)
            time.sleep(5)
            self.takeReward(task)
            time.sleep(5)

    def items(self):
        url = 'https://game.elfinkingdom.com/api/items'
        headers = {
            "address": self.address,
        }
        data = self.make_requset(url,headers,'GET')
        # if data['code'] == '000000':
        #     print('Успешно!')
        if len(data['result'])>0:
            count = 0
            for ball in data['result']:
                ball_name = ball['itemKey']
                ball_count = ball['count']
                print(f'Есть свободные мячи {ball_name}: {ball_count}. Можно ловить!')

    def comeAcross(self):
        url = 'https://game.elfinkingdom.com/api/pokemons/comeAcross'
        headers= {
            "address": self.address,
        }

        data = self.make_requset(url,headers)

        # if data['code'] == '000000':
        #     print('Успешно!')
        fight_id = data['result']['fightId']
        print('Бой номер: ',fight_id)
        pet_name = data['result']['npc']['name']
        pet_class = data['result']['npc']['skills'][0]['comment']
        print(f'Персонаж: {pet_name}\n Класс: {pet_class[2:]}')
        # if 'SSR' in pet_class or 'SR' in pet_class:
        #     print('Рарка! Можно брать!')
        # if 'N' in pet_class:
        #     print('Коммонка! Можно брать!')
        return fight_id
        # else:
        #     return None
    def catch_pokemon(self,fight_id):
        url = f'https://game.elfinkingdom.com/api/fights/{fight_id}/action/catchPokemon'
        headers= {
            "address": self.address,
            "content-type": "application/json;charset=UTF-8"
        }
        body = {
            'itemKey':'ball_level1'
        }
        body = f"JSON.stringify({str(body)})"
        # r = self.session.put(url,headers=headers,data=data)
        data = self.make_requset(url,headers,'PUT',body=body)
        print(data['message'])
        # if data['code'] == '000000':
        #     print('Успешно!')
        if data['code'] == '100013':
            print(data['message'])
        else:
            result = data['result']
            if result is not None:
                print(result['message'])
                if result['code'] == '10036' or result['message'] == 'Elfin escaped！':
                    print('Не поймал!!!')
            else:
                print('Ошибка Wild!!!')
    def get_pokemon(self):
        figth_id = self.comeAcross()
        if figth_id:
            for i in range(2):
                self.catch_pokemon(figth_id)
                time.sleep(5)
        else:
            time.sleep(30)
            return self.get_pokemon()

    def pokemons(self):
        url = 'https://game.elfinkingdom.com/api/pokemons'
        headers= {
            "address": self.address,
        }
        data =  self.make_requset(url,headers)

        if len(data['result'])>0:
            for p in data['result']:
                print(p)
            print('Есть покемоны!!!!!')
            return True
        else:
            print('Не поймали!(')
            return False

    def pvp_location(self):
        url = 'https://game.elfinkingdom.com/api/chapter/50001'
        headers= {
            "address": self.address,
        }
        data =  self.make_requset(url,headers)
        print(data)
    def pve(self,stage):
        url = 'https://game.elfinkingdom.com/api/fights/pve'
        body = {
            'stageId':stage
        }
        headers= {
            "address": self.address,
            "content-type": "application/json;charset=UTF-8"
        }

        body = f"JSON.stringify({str(body)})"
        data = self.make_requset(url,headers,'POST',body=body)
        fight_id = data['result']['fightId']
        print(fight_id)

    def finish_pve(self,fight_id):
        url = f'https://game.elfinkingdom.com/api/fights/{fight_id}/finishPve'
        body = '''{
  "isSuccess": true,
  "teamStatus": [
    {
      "id": 80591,
      "name": "Bazzor",
      "pkSystem": {
        "id": 4,
        "name": "电系",
        "counters": {
          "1": 1,
          "2": 1,
          "3": 1,
          "4": 1,
          "5": 1
        }
      },
      "pkClass": {
        "id": 1,
        "name": "绿"
      },
      "boneName": "Bazzor_s",
      "level": 7,
      "evolveType": 0,
      "skinType": 0,
      "attrRank": 1,
      "upgradeExp": 242,
      "exp": 3,
      "bodyParts": [
        {
          "id": 1451,
          "partType": 18,
          "priority": 3,
          "qualityType": -1,
          "rate": 1,
          "name": "bird_s_body"
        },
        {
          "id": 1489,
          "partType": 3,
          "priority": 6,
          "qualityType": -1,
          "rate": 1,
          "name": "bird_s_head_08"
        },
        {
          "id": 1513,
          "partType": 21,
          "priority": 2,
          "qualityType": -1,
          "rate": 1,
          "name": "bird_s_wing_02"
        },
        {
          "id": 1474,
          "partType": 6,
          "priority": 5,
          "qualityType": -1,
          "rate": 1,
          "name": "bird_s_foot_03"
        },
        {
          "id": 1509,
          "partType": 24,
          "priority": 1,
          "qualityType": -1,
          "rate": 1,
          "name": "bird_s_tail_08"
        },
        {
          "id": 1497,
          "partType": 9,
          "priority": 8,
          "qualityType": -1,
          "rate": 1,
          "name": "bird_s_mouth_06"
        },
        {
          "id": 1469,
          "partType": 12,
          "priority": 7,
          "qualityType": -1,
          "rate": 1,
          "name": "bird_s_eye_08"
        },
        {
          "id": 1457,
          "partType": 15,
          "priority": 4,
          "qualityType": -1,
          "rate": 1,
          "name": "bird_s_clothes_06"
        }
      ],
      "hpMax": 144.92,
      "hp": 144.92,
      "hpGrade": "D",
      "atk": 58.58,
      "atkGrade": "B",
      "def": 16.02,
      "defGrade": "B",
      "satk": 58.58,
      "satkGrade": "B",
      "sdef": 15.98,
      "sdefGrade": "B",
      "speed": 23,
      "speedGrade": "B",
      "ar": 1,
      "dr": 0,
      "cri": 0.15,
      "criguard": 0,
      "hit": 1,
      "flee": 0.1,
      "ce": 602.6,
      "status": 1,
      "fightId": null,
      "skills": [
        {
          "id": 1,
          "attrGorupId": 200101,
          "atkType": 1,
          "skillBind": 1,
          "name": "skill_1",
          "skillType": 1,
          "skillLevel": 1,
          "skillIcon": "Bazzor1",
          "selectType": 1,
          "atkRate": 1,
          "hpRate": 0,
          "defRate": 1,
          "effectOne": "skill_01",
          "effectTwo": "none",
          "description": "对单体敌人造成100%特攻伤害",
          "comment": "电鸟N",
          "isDelete": false,
          "createTime": "2021-12-01T20:32:22.000+00:00",
          "modifyTime": "2021-12-14T19:51:45.000+00:00"
        },
        {
          "id": 4,
          "attrGorupId": 200101,
          "atkType": 1,
          "skillBind": 1,
          "name": "skill_2",
          "skillType": 2,
          "skillLevel": 1,
          "skillIcon": "Bazzor2",
          "selectType": 1,
          "atkRate": 1.3,
          "hpRate": 0,
          "defRate": 1,
          "effectOne": "skill_02_01",
          "effectTwo": "skill_02_02",
          "description": "对单体敌人造成130%特攻伤害",
          "comment": "电鸟N",
          "isDelete": false,
          "createTime": "2021-12-01T20:32:22.000+00:00",
          "modifyTime": "2021-12-14T19:51:45.000+00:00"
        },
        {
          "id": 7,
          "attrGorupId": 200101,
          "atkType": 2,
          "skillBind": 1,
          "name": "skill_3",
          "skillType": 3,
          "skillLevel": 1,
          "skillIcon": "Bazzor3",
          "selectType": 2,
          "atkRate": 1.08,
          "hpRate": 0,
          "defRate": 1,
          "effectOne": "skill_ds_01",
          "effectTwo": "skill_ds_02",
          "description": "对全体敌人造成108%特攻伤害",
          "comment": "电鸟N",
          "isDelete": false,
          "createTime": "2021-12-01T20:32:22.000+00:00",
          "modifyTime": "2021-12-14T19:51:45.000+00:00"
        }
      ]
    },
    {
      "id": 80864,
      "name": "Bazzor",
      "pkSystem": {
        "id": 4,
        "name": "电系",
        "counters": {
          "1": 1,
          "2": 1,
          "3": 1,
          "4": 1,
          "5": 1
        }
      },
      "pkClass": {
        "id": 1,
        "name": "绿"
      },
      "boneName": "Bazzor_s",
      "level": 2,
      "evolveType": 0,
      "skinType": 0,
      "attrRank": 1,
      "upgradeExp": 23,
      "exp": 15,
      "bodyParts": [
        {
          "id": 1451,
          "partType": 18,
          "priority": 3,
          "qualityType": -1,
          "rate": 1,
          "name": "bird_s_body"
        },
        {
          "id": 1490,
          "partType": 3,
          "priority": 6,
          "qualityType": -1,
          "rate": 1,
          "name": "bird_s_head_09"
        },
        {
          "id": 1521,
          "partType": 21,
          "priority": 2,
          "qualityType": -1,
          "rate": 1,
          "name": "bird_s_wing_10"
        },
        {
          "id": 1479,
          "partType": 6,
          "priority": 5,
          "qualityType": -1,
          "rate": 1,
          "name": "bird_s_foot_08"
        },
        {
          "id": 1504,
          "partType": 24,
          "priority": 1,
          "qualityType": -1,
          "rate": 1,
          "name": "bird_s_tail_03"
        },
        {
          "id": 1493,
          "partType": 9,
          "priority": 8,
          "qualityType": -1,
          "rate": 1,
          "name": "bird_s_mouth_02"
        },
        {
          "id": 1468,
          "partType": 12,
          "priority": 7,
          "qualityType": -1,
          "rate": 1,
          "name": "bird_s_eye_07"
        },
        {
          "id": 1460,
          "partType": 15,
          "priority": 4,
          "qualityType": -1,
          "rate": 1,
          "name": "bird_s_clothes_09"
        }
      ],
      "hpMax": 100.02,
      "hp": 100.02,
      "hpGrade": "B",
      "atk": 40.5,
      "atkGrade": "D",
      "def": 10.96,
      "defGrade": "C",
      "satk": 40.5,
      "satkGrade": "D",
      "sdef": 11.04,
      "sdefGrade": "A",
      "speed": 23,
      "speedGrade": "B",
      "ar": 1,
      "dr": 0,
      "cri": 0.15,
      "criguard": 0,
      "hit": 1,
      "flee": 0.1,
      "ce": 414.6,
      "status": 1,
      "fightId": null,
      "skills": [
        {
          "id": 1,
          "attrGorupId": 200101,
          "atkType": 1,
          "skillBind": 1,
          "name": "skill_1",
          "skillType": 1,
          "skillLevel": 1,
          "skillIcon": "Bazzor1",
          "selectType": 1,
          "atkRate": 1,
          "hpRate": 0,
          "defRate": 1,
          "effectOne": "skill_01",
          "effectTwo": "none",
          "description": "对单体敌人造成100%特攻伤害",
          "comment": "电鸟N",
          "isDelete": false,
          "createTime": "2021-12-01T20:32:22.000+00:00",
          "modifyTime": "2021-12-14T19:51:45.000+00:00"
        },
        {
          "id": 4,
          "attrGorupId": 200101,
          "atkType": 1,
          "skillBind": 1,
          "name": "skill_2",
          "skillType": 2,
          "skillLevel": 1,
          "skillIcon": "Bazzor2",
          "selectType": 1,
          "atkRate": 1.3,
          "hpRate": 0,
          "defRate": 1,
          "effectOne": "skill_02_01",
          "effectTwo": "skill_02_02",
          "description": "对单体敌人造成130%特攻伤害",
          "comment": "电鸟N",
          "isDelete": false,
          "createTime": "2021-12-01T20:32:22.000+00:00",
          "modifyTime": "2021-12-14T19:51:45.000+00:00"
        },
        {
          "id": 7,
          "attrGorupId": 200101,
          "atkType": 2,
          "skillBind": 1,
          "name": "skill_3",
          "skillType": 3,
          "skillLevel": 1,
          "skillIcon": "Bazzor3",
          "selectType": 2,
          "atkRate": 1.08,
          "hpRate": 0,
          "defRate": 1,
          "effectOne": "skill_ds_01",
          "effectTwo": "skill_ds_02",
          "description": "对全体敌人造成108%特攻伤害",
          "comment": "电鸟N",
          "isDelete": false,
          "createTime": "2021-12-01T20:32:22.000+00:00",
          "modifyTime": "2021-12-14T19:51:45.000+00:00"
        }
      ]
    },
    {
      "id": 80657,
      "name": "Bazzor",
      "pkSystem": {
        "id": 4,
        "name": "电系",
        "counters": {
          "1": 1,
          "2": 1,
          "3": 1,
          "4": 1,
          "5": 1
        }
      },
      "pkClass": {
        "id": 1,
        "name": "绿"
      },
      "boneName": "Bazzor_s",
      "level": 1,
      "evolveType": 0,
      "skinType": 0,
      "attrRank": 1,
      "upgradeExp": 9,
      "exp": 0,
      "bodyParts": [
        {
          "id": 1451,
          "partType": 18,
          "priority": 3,
          "qualityType": -1,
          "rate": 1,
          "name": "bird_s_body"
        },
        {
          "id": 1491,
          "partType": 3,
          "priority": 6,
          "qualityType": -1,
          "rate": 1,
          "name": "bird_s_head_10"
        },
        {
          "id": 1519,
          "partType": 21,
          "priority": 2,
          "qualityType": -1,
          "rate": 1,
          "name": "bird_s_wing_08"
        },
        {
          "id": 1477,
          "partType": 6,
          "priority": 5,
          "qualityType": -1,
          "rate": 1,
          "name": "bird_s_foot_06"
        },
        {
          "id": 1504,
          "partType": 24,
          "priority": 1,
          "qualityType": -1,
          "rate": 1,
          "name": "bird_s_tail_03"
        },
        {
          "id": 1499,
          "partType": 9,
          "priority": 8,
          "qualityType": -1,
          "rate": 1,
          "name": "bird_s_mouth_08"
        },
        {
          "id": 1471,
          "partType": 12,
          "priority": 7,
          "qualityType": -1,
          "rate": 1,
          "name": "bird_s_eye_10"
        },
        {
          "id": 1454,
          "partType": 15,
          "priority": 4,
          "qualityType": -1,
          "rate": 1,
          "name": "bird_s_clothes_03"
        }
      ],
      "hpMax": 91.04,
      "hp": 91.04,
      "hpGrade": "A",
      "atk": 37.06,
      "atkGrade": "A",
      "def": 10.02,
      "defGrade": "B",
      "satk": 37.06,
      "satkGrade": "A",
      "sdef": 9.98,
      "sdefGrade": "B",
      "speed": 23,
      "speedGrade": "B",
      "ar": 1,
      "dr": 0,
      "cri": 0.15,
      "criguard": 0,
      "hit": 1,
      "flee": 0.1,
      "ce": 377,
      "status": 1,
      "fightId": null,
      "skills": [
        {
          "id": 1,
          "attrGorupId": 200101,
          "atkType": 1,
          "skillBind": 1,
          "name": "skill_1",
          "skillType": 1,
          "skillLevel": 1,
          "skillIcon": "Bazzor1",
          "selectType": 1,
          "atkRate": 1,
          "hpRate": 0,
          "defRate": 1,
          "effectOne": "skill_01",
          "effectTwo": "none",
          "description": "对单体敌人造成100%特攻伤害",
          "comment": "电鸟N",
          "isDelete": false,
          "createTime": "2021-12-01T20:32:22.000+00:00",
          "modifyTime": "2021-12-14T19:51:45.000+00:00"
        },
        {
          "id": 4,
          "attrGorupId": 200101,
          "atkType": 1,
          "skillBind": 1,
          "name": "skill_2",
          "skillType": 2,
          "skillLevel": 1,
          "skillIcon": "Bazzor2",
          "selectType": 1,
          "atkRate": 1.3,
          "hpRate": 0,
          "defRate": 1,
          "effectOne": "skill_02_01",
          "effectTwo": "skill_02_02",
          "description": "对单体敌人造成130%特攻伤害",
          "comment": "电鸟N",
          "isDelete": false,
          "createTime": "2021-12-01T20:32:22.000+00:00",
          "modifyTime": "2021-12-14T19:51:45.000+00:00"
        },
        {
          "id": 7,
          "attrGorupId": 200101,
          "atkType": 2,
          "skillBind": 1,
          "name": "skill_3",
          "skillType": 3,
          "skillLevel": 1,
          "skillIcon": "Bazzor3",
          "selectType": 2,
          "atkRate": 1.08,
          "hpRate": 0,
          "defRate": 1,
          "effectOne": "skill_ds_01",
          "effectTwo": "skill_ds_02",
          "description": "对全体敌人造成108%特攻伤害",
          "comment": "电鸟N",
          "isDelete": false,
          "createTime": "2021-12-01T20:32:22.000+00:00",
          "modifyTime": "2021-12-14T19:51:45.000+00:00"
        }
      ]
    }
  ]
}'''

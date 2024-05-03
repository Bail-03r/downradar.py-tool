

#https://discord.gg/dExwCVfjnT


from bs4 import BeautifulSoup as parser
import requests, random
from pypasser import reCaptchaV3

headers = {'Host': 'downradar.ru', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0', 'Accept': '*/*', 'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Accept-Encoding': 'gzip, deflate, br', 'X-Requested-With': 'XMLHttpRequest', 'Origin': 'https://downradar.ru', 'Alt-Used': 'downradar.ru', 'Connection': 'keep-alive', 'Referer': 'https://downradar.ru/ne-rabotaet/bqhaxCompany.cc', 'Sec-Fetch-Dest': 'empty', 'Sec-Fetch-Mode': 'cors', 'Sec-Fetch-Site': 'same-origin', 'Content-Length': '0', 'TE': 'trailers'}
howset = 'https://downradar.ru/vote/{0}/{1}/{2}/{3}' #vote-down / vote-up {1} random numbers with 3 dots e.g ...4123 {2}

class page:
    def __init__(self, link):
        self.link = f'https://downradar.ru/ne-rabotaet/{link}'
        self.company_id = parser(requests.get(self.link).text,'lxml').find('input',id='companyId').get('value')

    def send_comment(self, username, title, comment):
        tosend = {
            "company_id": self.company_id,
            "comment_id": "0",
            "parent_id": "0",
            "post_type": "website",
            "comment_message": comment,
            "comment_title": title,
            "comment_name": username
        }

        requests.post('https://downradar.ru/api/saveUserComment.php', json=tosend, headers=headers)

    def ping(self):
        requests.get(f'https://downradar.ru/api/indicator.php?cid={self.company_id}&issue=Общий сбой', headers=headers)

class comments:
    def __init__(self, id):
        self.id = id

    
    def dislike(self):
        reCaptchaKey = reCaptchaV3('https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LfOl8kpAAAAANdzEP_e-lStCxziKdYJcu2p8uN4&co=aHR0cHM6Ly9kb3ducmFkYXIucnU6NDQz&hl=ru&v=V6_85qpc2Xf2sbe3xTnRte7m&size=invisible&cb=lk9s8ax9cl5v')

        requests.put(howset.format(str(self.id),'vote-down',f'...{str(random.randint(1000,9e99))}', reCaptchaKey), headers=headers)

    def like(self):
        reCaptchaKey = reCaptchaV3('https://www.google.com/recaptcha/api2/anchor?ar=1&k=6LfOl8kpAAAAANdzEP_e-lStCxziKdYJcu2p8uN4&co=aHR0cHM6Ly9kb3ducmFkYXIucnU6NDQz&hl=ru&v=V6_85qpc2Xf2sbe3xTnRte7m&size=invisible&cb=lk9s8ax9cl5v')
        requests.put(howset.format(str(self.id),'vote-up',f'...{str(random.randint(1000,9e99))}', reCaptchaKey), headers=headers)


if __name__ == '__main__':
    raise Exception("Это библиотека!")

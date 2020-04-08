#R&D ICWR
#LunaticTech Lab

import requests
import sys
class ping:
    def __init__(self):
        self.brute()

    def ping(self,url):
        try:
            req = requests.get("http://"+url,timeout=10)
            if req.status_code  is not None:
                return print("URL Active => "+url)
            else:
                return print("URL NOT ACTIVE")
        except requests.exceptions.RequestException:
            return print("Error Bos")
            sys.exit()
    def brute(self):
        list_url = sys.argv[1]
        if list_url is None:
            sys.exit()
        else:
            word = [word.strip() for word in open(list_url,'r').readlines()]
            for url in word:
                self.ping(url)
if __name__ == "__main__":
    ping()

from datetime import datetime
import requests
import os
def current_time():
    return datetime.today().strftime('%Y%m%d %H:%M:%S')

def notify(token, text="Hi", desp="winjay"):
    date = datetime.today().strftime('%Y%m%d %H%M%S')
    URL = "https://sc.ftqq.com/{token}.send?text={text}&desp={desp}".format(token=token, text=text, desp=desp)
    try:
        print(URL)
        res = requests.get(URL)
        f = open("logs.txt", "a+")
        f.write(date + str(res.text) + '\n')
        f.close()
    except requests.exceptions.RequestException as e:
        f = open("logs.txt", "a+")
        f.write(date + str(e))
        f.close()


def get_current_path(rel_file):
   return os.path.join(os.path.dirname(__file__), rel_file) 

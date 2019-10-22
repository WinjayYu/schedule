from datetime import datetime
import requests
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



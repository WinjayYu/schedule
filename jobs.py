import requests
import schedule
import json
import time
import os
import sys
from tools import notify, get_current_path
import logger
# about monitor ip
old_ip = ""
token = ""
try:
    token = os.environ['SERVER_JIANG_TOKEN']
except KeyError:
    print("Please export the environment varibale SERVER_JIANG_TOKEN")
    sys.exit(1)

def monitor_ip():
    global old_ip
    if not old_ip:
        old_ip = get_old_ip();
    res = requests.get("https://api.ipify.org?format=json")
    try:
        ip_json = json.loads(res.text)
        logger.log(ip_json["ip"])
        current_ip = ip_json["ip"]
        if old_ip != current_ip:
            old_ip = current_ip
            notify(token, "ipHasChanged", current_ip)
            set_ip(current_ip)    
    except: 
        print("parse json error")

def get_old_ip():
    with open(get_current_path("./ip.txt"), "r") as f:
        return f.read()

def set_ip(ip):
    f = open(get_current_path("./ip.txt"), "w")
    f.write(ip)
    f.close()
# end monitor ip

# start tracklist
def track_list():
    os.system("bash ./trackerslist.sh") 

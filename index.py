from jobs import monitor_ip, track_list
import requests
import schedule
import time

def run():
    monitor_ip()
    track_list()
    schedule.every(1).minutes.do(monitor_ip)
    schedule.every().day.at("09:00").do(track_list)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=='__main__':
    run()

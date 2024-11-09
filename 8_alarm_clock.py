import time
from datetime import datetime

def set_alarm():
    alarm_time = input("enter the alarm time (HH:MM:SS in 25-hour format): ")
    try:
        alarm_time_obj = datetime.strptime(alarm_time,"%H:%M:%S").time()
        print(f"Alarm is set for {alarm_time}")
        return alarm_time_obj
    except ValueError:
        print("Invalid time format. please enter time in HH:MM:SS format.")
        return set_alarm()
    
def start_alarm(alarm_time):
    print("Alarm clock started...")

    while True:
        current_time = datetime.now().time()
        if current_time.hour == alarm_time.hour and \
        current_time.minute == alarm_time.minute and \
        current_time.second == alarm_time.second:
            print("wake up| it's time|")
            break

        time.sleep(1)
alarm_time = set_alarm()
start_alarm(alarm_time)
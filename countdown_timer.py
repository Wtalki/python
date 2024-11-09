import time

def countdown_timer(seconds):
    while seconds:
        mins,secs = divmod(seconds,60)
        timer_format = f"{mins:02d}:{secs:02d}"
        print(f"time remaining:{timer_format}", end='\r')

        time.sleep(1)
        seconds -=1

    print("countdown finished time's up!")




def main():
    try:
        seconds = int(input("enter time in seconds for countdown"))
        countdown_timer(seconds)
    except ValueError:
        print("please enter a vlid integer for the countdown")

main()
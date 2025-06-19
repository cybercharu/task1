import time
from datetime import datetime, timezone, timedelta
from playsound import playsound
import msvcrt

# clock mode in 12 hour format
def clock_mode():
    print("Press Enter to get menu")
    while True:
        now = datetime.now()
        print("Time:", now.strftime("%I:%M:%S %p"), end="\r")
        time.sleep(1)
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'\r':
                print("\nReturning to menu")
                break
# playing sound from playsound 
try:
    from playsound import playsound
    SOUND_AVAILABLE = True
except ImportError:
    SOUND_AVAILABLE = False



def get_alarm_time():
    while True:
        user_input = input("Enter alarm time in HH:MM (24-hour format): ")
        try:
            alarm_time = datetime.strptime(user_input, "%H:%M").time()
            return alarm_time
        except ValueError:
            print("Invalid time format")

def ring_alarm():
    print("ALARM RINGING! Wake up!")
    print("press ctrl+c to turn off alarm")
    acknowledged = False
    while not acknowledged:
        if SOUND_AVAILABLE:
            try:
                while acknowledged == False:
                    playsound("alarm_clock.mp3")
                    
            except:
                print("Wake up!!")
        else:
            print("Wake up!!")
           
        user_input = input("Type 'stop' to turn off the alarm: ").strip().lower()
        if user_input == "stop":
            acknowledged = True

    print("Alarm stopped.")
            


        
# alarm ring
def alarm_mode():
    alarm_time = get_alarm_time()
    print(f"Alarm is set for {alarm_time.strftime('%H:%M')}\nWaiting for alarm time")

    while True:
        current_time = datetime.now().time()
        if current_time.hour == alarm_time.hour and current_time.minute == alarm_time.minute:
            ring_alarm()
            break
        time.sleep(10) 

#count down feature
def countdown_mode():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S ") 
    user_input = input("Enter time in HH:MM format (24-hour): ")
    try:
        user_time = datetime.strptime(user_input, "%H:%M").time()
    except ValueError:
        print("Invalid time format")
        return
    alarm_time = datetime.combine(now.date(), user_time)

    if alarm_time < now:
        alarm_time += timedelta(days=1)

    total_seconds = int((alarm_time - now).total_seconds())

    print("Countdown started\n")
    while total_seconds > 0:
        print(f"Remaining time: {total_seconds} seconds", end='\r')
        time.sleep(1)
        total_seconds -= 1
    print(" " * 50, end='\r') 
    print("Target time reached")

# In Settings Mode user choose between 12-hour or 24-hour time format
def settings_mode():
    # 12 hour format
    def twelve_format():
        choice = input("Choose time zone (IST/UTC): ").strip().upper()
        utc_now = datetime.now(timezone.utc)
        menu()
        if choice == "IST":
            ist_now = utc_now + timedelta(hours=5, minutes=30)
            current_time = ist_now.strftime("%I:%M:%S %p")
            print("Current Time in 12-hour format (IST):", current_time)
        elif choice == "UTC":
            current_time = utc_now.strftime("%I:%M:%S %p")
            print("Current Time in 12-hour format (UTC):", current_time)
        else:
            print(" Invalid time zone")
#24 hour format
    def twentyfour_format():
        choice = input("Choose time zone (IST/UTC): ").strip().upper()
        utc_now = datetime.now(timezone.utc)
        menu()
        if choice == "IST":
            ist_now = utc_now + timedelta(hours=5, minutes=30)
            current_time = ist_now.strftime("%H:%M:%S")
            print("Current Time in 24-hour format (IST):", current_time)
        elif choice == "UTC":
            current_time = utc_now.strftime("%H:%M:%S")
            print("Current Time in 24-hour format (UTC):", current_time)
        else:
            print("Invalid time zone") 
    def menu():
        print("A. twelve_format")
        print("B. twentyfour_format")
    while True:
        menu()
        choice=input("Enter your choice: ")
        if choice == "A":
            twelve_format()
        elif choice == "B":
            twentyfour_format()
        else:
            print("Invalid choice")
        return show_menu
    
# Main menu
def show_menu():
    print("Main Menu:")
    print("1. Clock Mode")
    print("2. Alarm Mode")
    print("3. Countdown Mode")
    print("4. Settings")

while True:
    show_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        print("You chose Clock mode")
        clock_mode()
    elif choice == "2":
        print("You chose Alarm mode")
        alarm_mode()
    elif choice == "3":
        print("You chose Countdown mode")
        countdown_mode()
    elif choice == "4":
        print("You chose Setting mode")
        settings_mode()
    else:
        print("Invalid choice")

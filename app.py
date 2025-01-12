# app.py
import datetime

def print_greeting():
    current_time = datetime.datetime.now()
    hour = current_time.hour

    if hour < 12:
        greeting = "Good Morning!"
    elif hour < 18:
        greeting = "Good Afternoon!"
    else:
        greeting = "Good Evening!"

    print(f"{greeting} The current time is {current_time.strftime('%H:%M:%S')}")

def print_info():
    print("\nThis is a simple Python application.")
    print("It is designed to demonstrate how Jenkins can be used to run Python projects.\n")

def main():
    print_info()
    print_greeting()

if __name__ == "__main__":
    main()

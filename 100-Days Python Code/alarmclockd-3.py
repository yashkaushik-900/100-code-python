import datetime
import time
import winsound  # Works only on Windows

def set_alarm(alarm_time):
    try:
        # Convert string to time object for validation
        datetime.datetime.strptime(alarm_time, "%H:%M:%S")
    except ValueError:
        print("❌ Invalid time format! Please use HH:MM:SS (24-hour).")
        return

    print(f"✅ Alarm is set for {alarm_time}")

    while True:
        # Get current system time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        
        if current_time == alarm_time:
            print("⏰ Alarm ringing! Wake up!")

            try:
                # Play beep sound for 5 times
                for i in range(5):
                    winsound.Beep(1000, 700)  # (frequency, duration ms)
            except RuntimeError:
                print("⚠️ Beep not supported on this system.")

            break

        time.sleep(1)  # Check every second

# Take user input for alarm
alarm_time = input("Enter alarm time in HH:MM:SS (24-hour format): ")
set_alarm(alarm_time)


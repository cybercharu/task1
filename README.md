# simple terminal-based digital clock application with multiple modes that displays time in different ways.

## alarm modes:
1. Clock mode: Displays the current system time updating every second
2. Alarm Mode: Allows setting an alarm for a specific time (HH:MM)
3. Countdown Mode: Shows seconds remaining until a target time
4. Settings Mode: Lets user choose between 12-hour or 24-hour time format, and choice of
timezones

## Features

- 12-hour and 24-hour time formats
- Countdown and alarm modes
- Continuous ringing until stopped
- IST/UTC timezone selection
- Sound support using playsound module

## requirements
 - first check python --version,if not installed then download it
 - To open code in vs terminal write command ctrl+`
 - then write file name to execute code : python alarm_modes.py
 - after that if you see ModuleNotFoundError: No module named playsound
   then,install it using     pip install playsound
   if you are using python newer version it might show an error as playsound doesn't supported newer version
   then, write this cmd      pip install playsound=1.2.2
   after successfully installation
   write again file name to execute the code

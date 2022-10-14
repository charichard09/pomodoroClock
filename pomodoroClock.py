# Pomodoro technique
# Date: 8-16-2021 Dev: Richard C.

import time, winsound, datetime

# Ask user how long to set first pomo duration. Then ask user if they'd like to add another pomo duration. When no 
# further times are wanted, prompt "press Enter to begin."
to_loop = "y"
number = 1
loop_names = {"Break": 300, "Loop 0": 2}
freq = 440 # Hz
duration = 500 # milliseconds
zero_insert = ''

while to_loop == "y":
    # Get pomo duration in minutes, convert to seconds, save into dictionary
    answer = 60 * int(input(f"How long would you like to set pomodoro duration {number}? (in minutes, break time is auto added)\n"))

    # Check if answer is int
    if isinstance(answer, int):
        loop_names[f"Loop {number}"] = answer
    else:
        continue

    number += 1
    to_loop = input("Would you like to add another pomo duration to this session? (y/n)\n")

print(loop_names)
input("Press Enter to begin.\n")

# Use time.time() and execution time compensation to go through duration and print timer along the way.
for i in range(number + 1):
    #figure out compensation needed for execution time by running 1 loop
    if i == 0:
        start_time = time.time()
        if f"Loop {i}" in loop_names:
            for j in range(loop_names[f"Loop {i}"]):
                dt_obj = datetime.datetime.now()
                if len(str(dt_obj.minute)) < 2:
                    zero_insert = "0"
                else: 
                    zero_insert = ""
                print(f"Loop end: {dt_obj.hour}:{dt_obj.minute}:{dt_obj.second}", end='\r')
                time.sleep(1)
        compensation_time = ((time.time() - 2) - start_time) / 2
        continue

    if f"Loop {i}" in loop_names:
        # Print end time of loop
        dt_obj = datetime.datetime.now()
        dt_delta = datetime.timedelta(minutes=loop_names[f"Loop {i}"]/60)
        end_time = dt_obj + dt_delta
        if len(str(end_time.minute)) < 2:
            zero_insert = "0"
        else: 
            zero_insert = ""
        
        print(f"Loop End: {end_time.hour}:{zero_insert}{end_time.minute}:{end_time.second}")  


        for j in range(loop_names[f"Loop {i}"]):
            dt_obj = datetime.datetime.now()
            if len(str(dt_obj.minute)) < 2:
                zero_insert = "0"
            else: 
                zero_insert = ""
            print(f"Loop Cur: {dt_obj.hour}:{zero_insert}{dt_obj.minute}:{dt_obj.second}", end='\r')              # temporary to see if time is correct
            time.sleep(1 - compensation_time)

    # TODO: When timer hits inputted duration, stop and sound an alarm using winsound.Beep()
    for amt_beeps in range(4):
        winsound.Beep(freq, duration)

    # TODO: Ask user to press ENTER when ready for 5 min interval. Reset loop (could also recall as function)
    input("Pomodoro time is done. Press Enter to start Break.\n")

    # Print end time of loop
    dt_obj = datetime.datetime.now()
    dt_delta = datetime.timedelta(minutes=loop_names["Break"]/60)
    end_time = dt_obj + dt_delta
    if len(str(end_time.minute)) < 2:
        zero_insert = "0"
    else: 
        zero_insert = ""
    print(f"Loop End: {end_time.hour}:{zero_insert}{end_time.minute}:{end_time.second}")  

    for k in range(loop_names["Break"]):
        dt_obj = datetime.datetime.now()
        if len(str(dt_obj.minute)) < 2:
            zero_insert = "0"
        else: 
            zero_insert = ""
        print(f"Loop Cur: {dt_obj.hour}:{zero_insert}{dt_obj.minute}:{dt_obj.second}", end='\r')
        time.sleep(1 - compensation_time)
    
    for amt_beep in range(4):
        winsound.Beep(freq, duration)

    input("Break is over. Press Enter to start next loop or end.\n")

# TODO: In the future, possibly using Shelve variable storage, ask user if theyd like to store time inputs into shelve to be recalled 
# next time script is ran

# TODO: Need to make printout of datetime.datetime.now() to a variation of datetime.timedelta(hours=x, minutes=y, seconds=z) object + 
# datetime.datetime.now() to show either a countdown or countup towards end of current loop

# TODO: After about 6 minutes, program becomes 1 second off. Could try testing finding compensation time every loop instead of just once.
# From start: 2021-08-21 04:13:40.793317 to finish: 2021-08-21 04:23:40.654145, I'm only off by .14. I should be off by 1.14, finish time
# should be 41.65? As program executes, milliseconds goes down eventually this happens:
# 2021-08-21 04:20:18.000291
# 2021-08-21 04:20:18.998539
# seconds repeat, yet finish time doesnt showcase this skip? I am definitely missing something. 
'''
    This is program that converts a 12hour time format into the military 
    24hour time format, it accept string input in 12hour time and convert
    it to 24hour time e.g
        Input: Enter time give a space and enter either AM or PM; '1:00 PM'
        Output: It will be in this format (XX:XX) i.e (13:00)
'''

# specifying the time string e.g 1:15 PM or 10:00 AM
time = str(input("Enter time string: "))

# spliting the time string into individual string e.g '10:00' and 'AM'
split_str = time.split(" ")

# spliting the first string in the split_str list
time_str = split_str[0].split(":")

# to check if time is either AM  or PM
if (split_str[1] == "AM".lower()) or (split_str[1] == "am".upper()):
    
    # if time is 12:00 AM, print 00:00
    if time_str[0] == "12":
        print("00" + ":" + time_str[1])
    else:
        # if the length of the time string is 2, print it out
        # else add '0' in front of the string e.g 11:00 AM => 11:00
        # 8:00 AM => 08:00
        if len(time_str[0]) == 2:
            print(split_str[0])
        else:
            print("0" + time_str[0] + ":" + time_str[1])
else:
    # if the of time string is 12:00 PM, print it out
    # else add 12 to the time and print it out e.g 12:00 PM => 12:00
    # 2:00 PM => 14:00
    if time_str[0] == "12":
        print(split_str[0])
    else:
        pm_time = int(time_str[0]) + 12
        print(str(pm_time) + ":" + time_str[1])
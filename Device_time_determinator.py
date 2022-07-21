"""
CP1401 2022 TR2 Assignment 1

Program 1 – Device time determinator

Student Name: <your name>

Date started: <date>

Pseudocode:

BEGIN

    PROMPT for number of practices
    PROMPT for mowing activity status

    IF activity status is no
        SET output string to "No device time :("
    
    ELSE IF activity status is yes
        IF number of practices if greater than or equal to 7

            SET device time to number of practices DIVIDED by 15
            SET output string to "You get " + \
                device_time + \
                " minutes of device time :) \nAnd you get a cupcake!"

        ELSE 
            SET device time to number of practices DIVIDED by 15
            SET output string to "You get " + \
                device_time + \
                " minutes of device time :)  "

DISPLAY "Device time determinator"
DISPLAY "Did you mow: ", mowing activity status
DISPLAY output string
            
END

Expected Output:

Device Time Determinator
Number of practices: 8
Did you mow? no
No device time :(

Device Time Determinator
Number of practices: 3
Did you mow? yes
You get 45 minutes of device time :)
Device Time Determinator

Number of practices: 7
Did you mow? YES
You get 105 minutes of device time :)
And you get a cupcake!

"""

# propmt for number of practices
number_of_practices = int(input("How many practices did you do? "))

# prompt for mowing activity status
mow_status = input("Did you mow the lawn? ")

# convert status string to lowercase and check if it is no
if mow_status.lower() == "no":

    output_string = "No device time :("

# convert status string to lowercase and check if it is yes
elif mow_status.lower() == "yes":
    if number_of_practices >= 7:

        # calculate the device time
        device_time = str(number_of_practices * 15)
        output_string = "You get " + \
            device_time + \
            " minutes of device time :) \nAnd you get a cupcake!"
    else:

        # calculate the device time
        device_time = str(number_of_practices * 15)
        output_string = "You get " + \
            device_time + \
            " minutes of device time :)  "

print("Device time Determinator")
print("Did you mow: ", mow_status)
print(output_string)

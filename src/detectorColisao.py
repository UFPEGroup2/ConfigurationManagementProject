def readSensor():
    # input: read distance number from keyboard
    # output: TRUE or FALSE based on minimum distance to detect obstable
    # minimal distance == 5m
    pass

def blinkLED(freq):
    # print some LED ON/OFF information with freq info
    pass


def soundBuzzer(freq):
    # print some buzzer sound information with freq info
    pass


####################
# CONTROLLER
####################
while(True):
    sensor1 = readSensor()
    sensor2 = readSensor()

    # Decision logic to activate led and buzzer
    if ((sensor1 == True) or (sensor2 == True)):
        blinkLED(1)
        soundBuzzer(1)
            
    else:
        pass

        



    

class readSensor(unittest.TestCase)
    
    def get_leadVehicleDistance(distance):
        distance = 50.0
        return distance


    def read():
        sensorDistance = get_leadVehicleDistance()
        
        if sensorDistance < 60:
            return True
        else:
            return False
        

    
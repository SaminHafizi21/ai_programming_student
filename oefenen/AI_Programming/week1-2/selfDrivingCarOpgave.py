class Percept: # dit is een abstracte klasse
    pass

class LidarSensorInput(Percept): 
        # de lidar sensor is een concrete sensor en erft dus over van de Percept klasse.
        # ze houdt een attribuut bij mety de gemeten afstand tot de voorligger
    def __init__(self):
        self.DistanceTo = 0.0

class Actuator: # dit is een abstracte klasse
    def __str__(self):
        pass

class Brake(Actuator):
        # de brake klasse is een concrete actuator. Omdat wij geen echte motor hebben, beperken we ons tot het printen van BRAKE in de console.
    def __str__(self):
        return "BRAKE"

class Nothing(Actuator):
    # de Nothing klasse (niet remmen) is een concrete actuator. Omdat wij geen echte motor hebben, beperken we ons tot het printen van NOTHING in de console.
    def __str__(self):
        return "NOTHING"

class Agent: # abstracte klasse
    def process(self, p):
        pass

class SelfDrivingCar(Agent):
    def __init__(self):
        # aan te vullen: welke variabelen heb je nodig ?
        pass

    def process(self, p):
        # implementeer deze functie:
        # je wil op basis van de vorige meting van de lidar de relatieve snelheid van dit voertuig tegenover de voorganger bepalen
        # indien de snelheid zodanig is dat er binnen 5 seconden zou worden gebotst, dan moet je remmen
       
        action = Nothing()

        if isinstance(p, LidarSensorInput):
            #aan te vullen
            pass

        return action

if __name__ == "__main__":
    # suggestie testcode
    sensor = LidarSensorInput()
    agent = SelfDrivingCar()

    sensor.DistanceTo = 10
    action = agent.process(sensor)
    print(action)

    sensor.DistanceTo = 15
    action = agent.process(sensor)
    print(action)

    sensor.DistanceTo = 13
    action = agent.process(sensor)
    print(action)

    sensor.DistanceTo = 10
    action = agent.process(sensor)
    print(action)

"""
Oefening 1: Self-Driving Car (Model-based Reflex Agent)
========================================================
Implementeer een agent die zijn voorligger volgt.
"""


class LidarSensorInput:
    def __init__(self, distance=0.0):
        self.DistanceTo = distance


class Brake:
    def __str__(self):
        return "BRAKE"


class Nothing:
    def __str__(self):
        return "NOTHING"


class SelfDrivingCar:
    def __init__(self):
        self.vorige_afstand = None

    def process(self, sensor_input):
        # TODO: bereken relatieve snelheid en tijd tot botsing;
        #       rem als tijd < 5 seconden

        afstand = sensor_input.DistanceTo

        if self.vorige_afstand is None:
            self.vorige_afstand = afstand
            return Nothing()

        snelheid = self.vorige_afstand - afstand

        if snelheid < 0:
            tijd_tot_botsing = float("inf")
        else:
            tijd_tot_botsing = afstand / snelheid

        self.vorige_afstand = afstand

        if tijd_tot_botsing < 5.0:
            return Brake()

        return action


if __name__ == "__main__":
    sensor = LidarSensorInput(10)
    agent = SelfDrivingCar()

    for afstand in [10, 15, 13, 10, 8, 6, 4, 3]:
        sensor.DistanceTo = afstand
        action = agent.process(sensor)
        print(f"Afstand: {afstand}m -> {action}")

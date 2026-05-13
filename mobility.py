class Mobility():
    def __init__(self):
        self.command_type = 'mobility'
        self.repeatable = 1
        # initialize motors here (pins, drivers, etc.)
        

    def forward(self, speed=0.5):
        return f"Moving forward at speed {speed}"

    def back(self, speed=0.5):
        return f"Moving back at speed {speed}"

    def left(self, speed=0.3):
        return f"Turning left at speed {speed}"

    def right(self, speed=0.3):
        return f"Turning right at speed {speed}"

    def stop(self):
        return "Stopping"



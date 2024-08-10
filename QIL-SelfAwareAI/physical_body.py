# QIL-SelfAwareAI/physical_body.py

class PhysicalBody:
    def __init__(self, environment):
        self.environment = environment
        self.position = (0, 0)
        self.sensors = {
            'vision': self.vision_sensor,
            'hearing': self.hearing_sensor,
            'touch': self.touch_sensor,
            'smell': self.smell_sensor,
            'taste': self.taste_sensor
        }

    def vision_sensor(self):
        x, y = self.position
        return self.environment.get_location(x, y)

    def hearing_sensor(self):
        x, y = self.position
        nearby_locations = []
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            loc = self.environment.get_location(x + dx, y + dy)
            if loc:
                nearby_locations.append(loc)
        return nearby_locations

    def touch_sensor(self):
        return self.vision_sensor()

    def smell_sensor(self):
        return self.hearing_sensor()

    def taste_sensor(self):
        return self.vision_sensor()

    def move(self, direction):
        x, y = self.position
        if direction == 'up' and x > 0:
            self.position = (x - 1, y)
        elif direction == 'down' and x < self.environment.size - 1:
            self.position = (x + 1, y)
        elif direction == 'left' and y > 0:
            self.position = (x, y - 1)
        elif direction == 'right' and y < self.environment.size - 1:
            self.position = (x, y + 1)

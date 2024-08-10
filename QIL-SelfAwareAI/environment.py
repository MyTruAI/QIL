# QIL-SelfAwareAI/environment.py

import random

class DynamicEnvironment:
    def __init__(self, size):
        self.size = size
        self.grid = [['' for _ in range(size)] for _ in range(size)]
        self.time_of_day = "Day"
        self.weather = "Clear"
        self.populate_environment()

    def populate_environment(self):
        self.grid[0][0] = 'Home'
        self.grid[0][1] = 'Park'
        self.grid[1][0] = 'Office'
        self.grid[1][1] = 'Market'
        self.grid[0][2] = 'School'
        self.grid[1][2] = 'Library'
        self.grid[2][0] = 'Hospital'
        self.grid[2][1] = 'Mall'
        self.grid[2][2] = 'Forest'

    def update_environment(self):
        self.time_of_day = "Night" if self.time_of_day == "Day" else "Day"
        weather_options = ["Clear", "Rain", "Fog", "Snow"]
        self.weather = random.choice(weather_options)
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] and random.random() < 0.1:
                    self.grid[i][j], self.grid[i][(j+1)%self.size] = '', self.grid[i][j]

    def get_location(self, x, y):
        if 0 <= x < self.size and 0 <= y < self.size:
            return self.grid[x][y]
        return None

    def display_environment(self):
        print(f"Time of Day: {self.time_of_day}, Weather: {self.weather}")
        for row in self.grid:
            print(' | '.join(row))

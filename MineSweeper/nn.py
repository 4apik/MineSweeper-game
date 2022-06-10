import random


class NN:
    def __init__(self):
        self.active = True
        self.goal = 319

    def play(self, game_settings, spots):
        while game_settings.game_active:
            self.calculate_next(spots)

    def calculate_next(self, spots):
        self.inputs = [spot.value if not spot.hidden else -1 for spot in spots.sprites()]

        for index, value in enumerate(self.inputs):
            pass


#nn = NN()
#spots = [random.randint(-1, 6) for x in range(399)]
#print(spots)

class Game():
    def __init__(self):
        self.score = 0
        self.time_elapsed = 0

    def __str__(self):
        return "Score : %s" % self.score
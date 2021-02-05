import copy
import random
# Consider using the modules imported above


class Hat:
    def __init__(self, **balls):
        self.ballsinit = balls.items()
        # Converti les arguments en une list de str
        self.contents = list()
        for color, value in self.ballsinit:
            i = 0
            for i in range(value):
                self.contents.append(color)
        self.contents_copy = copy.copy(self.contents)

    def draw(self, balls_draw):
        all_drawn_balls = list()
        making_index = random.randint(0, len(self.contents)-1)
        while balls_draw > 0:
            all_drawn_balls.append(self.contents[making_index])
            self.contents.pop(making_index)
            if len(self.contents) == 0:
                if balls_draw > len(self.contents_copy):
                    pass
                else:
                    self.contents = self.contents_copy.copy()
            try:
                making_index = random.randint(0, len(self.contents)-1)
            except:
                making_index = 0
            balls_draw -= 1
        return all_drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success = 0
    for i in range(num_experiments):
        drawn_balls = hat.draw(num_balls_drawn)
        counter_true = 0
        for k, v in expected_balls.items():
            if drawn_balls.count(k) >= v:
                counter_true += 1

        if counter_true >= len(expected_balls):
            success += 1

        if num_balls_drawn > len(hat.contents_copy):
            hat.contents = hat.contents_copy.copy()

    return success/num_experiments

import copy
import random
# Consider using the modules imported above.

class Hat:
    
    def __init__(self, **kwargs):
        self.hats = {}
        for k, v in kwargs.items():
            self.hats[k] = v
        self.contents = []
        list_ = []
        for k, v in kwargs.items():
            list_.append([k] * v)
        self.contents = [item for sublist in list_ for item in sublist]
        
    def draw(self, numDraw):
        randomPick = []
        contents = self.contents
        if len(contents) > numDraw:
            for i in range(numDraw):
                r_i = random.randrange(len(contents))
                ball = contents[r_i]
                randomPick.append(ball)
                contents.pop(r_i)
            return randomPick
        else:
            return contents
        


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    
    incorrect_prob = 0
    
    for i in range(num_experiments):
        contents = copy.deepcopy(hat)
        drawn_balls = contents.draw(num_balls_drawn)
        
        for v in expected_balls.keys():
            correct_prob = 0
            for j in range(len(drawn_balls)):
                if drawn_balls[j] == v:
                    correct_prob += 1
            if correct_prob < expected_balls[v]:
                incorrect_prob += 1
                break
                
    return 1-incorrect_prob/num_experiments
        
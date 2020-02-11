from random import choice

class RandomWalk:
    """A class to generate random walks"""

    def __init__(self, num_points = 5000):
        """Initialize attributes for a walk"""
        self.num_points = num_points

        #all walks start at 0.0
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all points in the walk"""

        #keep taking steps until the walk reaches the desired length
        while len(self.x_values) < self.num_points:
            x_direction = choice([1,-1])
            x_distance = choice ([0,1,2,3,4])
            x_step = x_direction * x_distance

            y_direction = choice([1,-1])
            y_distance = choice ([0,1,2,3,4])
            y_step = y_direction * y_distance

            #calculate new x
            newx = self.x_values[-1]+x_step
            if newx < 0:
                newx = 0

            #calculate new y
            newy = self.y_values[-1] + y_step
            if newy < 0:
                newy = 0

            self.x_values.append(newx)
            self.y_values.append(newy)
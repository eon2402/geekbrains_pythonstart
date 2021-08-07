class Road:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def get_weight(self, weight_ind, thikness):
        weight = self.width * self.length * weight_ind * thikness
        return weight


my_road = Road(4,1000)
print(my_road.get_weight(25, 1.5))




def Minkowski_distance(pointA, pointB , P):
    # squared euclidean distance
    distance = 0
    dimensions = len(pointA) # assumes both points have the same dimensions
    for dimension in range(dimensions):
        distance += (pointA[dimension] - pointB[dimension])**P
    return distance
class KDTreeNode():
    def __init__(self, point, left, right):
        self.point = point
        self.left = left
        self.right = right

    def is_leaf(self):
        return (self.left == None and self.right == None)
class KDTreeNeighbours():
    """ Internal structure used in nearest-neighbours search.
    """

    def __init__(self, query_point, t):
        self.query_point = query_point
        self.t = t  # neighbours wanted
        self.largest_distance = 0  # squared
        self.current_best = []

    def calculate_largest(self):
        if self.t >= len(self.current_best):
            self.largest_distance = self.current_best[-1][1]
        else:
            self.largest_distance = self.current_best[self.t - 1][1]

    def add(self, point):
        sd = Minkowski_distance(point, self.query_point,P)
        # run through current_best, try to find appropriate place
        for i, e in enumerate(self.current_best):
            if i == self.t:
                return  # enough neighbours, this one is farther, let's forget it
            if e[1] > sd:
                self.current_best.insert(i, [point, sd])
                self.calculate_largest()
                return
        # append it to the end otherwise
        self.current_best.append([point, sd])
        self.calculate_largest()

    def get_best(self):
        return [element[0] for element in self.current_best[:self.t]]
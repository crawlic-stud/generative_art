import numpy as np


def create_curve(t_values: np.ndarray, points: np.array):

    def two_points(t: [int, float], p1: np.ndarray, p2: np.ndarray):
        return (1 - t) * p1 + t * p2

    def create_points(t, points):
        new_points = []
        for i in range(len(points) - 1):
            new_points += [two_points(t, points[i], points[i + 1])]
        return new_points

    def create_point(t, points):
        while len(points) > 1:
            points = create_points(t, points)
        return points[0]

    curve = np.array([[0.0] * 2])
    for t in t_values:
        curve = np.append(curve, [create_point(t, points)], axis=0)
    curve = np.delete(curve, 0, 0)

    return curve
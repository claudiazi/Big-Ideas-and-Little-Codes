from collections import defaultdict
from functools import partial
from pprint import pprint
from random import sample
from typing import Iterable, Tuple, List, Sequence, Dict
from math import fsum, sqrt

Point = Tuple[int, ...]
Centroid = Point
PointGroup = Sequence[Point]



def mean(data: Iterable[float]) -> float:
    """Accurate arithmetic mean"""
    data = list(data)
    return fsum(data) / len(data)


def dist(p, q, _fsum=fsum, _sqrt=sqrt, _zip=zip) -> float:
    """Euclidean distance function for multi-dimensional data"""
    return sqrt(fsum([(x - y) ** 2 for x, y in zip(p, q)]))


def assign_data(centroids: Sequence[Centroid], data: Iterable[Point]) -> Dict[Centroid, List[Point]]:
    """Group the data points to the closest centroid"""
    d = defaultdict(list)
    for point in data:
        closest_centroid = min(centroids, key=partial(dist, point))
        d[closest_centroid].append(point)
    return dict(d)


def compute_centroids(groups: Iterable[PointGroup]) -> List[Centroid]:
    """Compute the centroid of each group"""
    return [tuple(map(mean, zip(*group))) for group in groups]   #MyPy doesnt know how to deal with 'zip(*)' yet


def k_means(data: Iterable[Point], k: int = 2, iterations: int = 50) ->List[Centroid]:
    data = list(data)
    centroids = sample(data, k)
    for i in range(iterations):
        labeled = assign_data(centroids, data)
        centroids = compute_centroids(labeled.values())
    return centroids


if __name__ == "__main__":
    points = [
        (10, 41, 23),
        (22, 30, 29),
        (11, 42, 5),
        (20, 32, 4),
        (12, 40, 12),
        (21, 36, 23),
    ]
    centroids = k_means(points, k=3)
    d = assign_data(centroids, points)
    pprint(d)
    """
    for point in points:
        print(point, dist(point, (9, 39, 20)))

    centroids = [(9, 39, 20), (12, 36, 25)]
    point = (11, 42, 5)
    print(min([dist(point, centroid) for centroid in centroids]))
    print(min(centroids, key=lambda centroid: dist(point, centroid)))
    print(min(centroids, key=partial(dist, point)))
    pprint(assign_data(centroids, points), width=45)
    """
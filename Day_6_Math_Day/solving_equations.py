import matplotlib.pyplot as plt

def get_values(string: str, length: int) -> list:
    while True:
        try:
            lst = [float(i) for i in input(string).split()]
        except ValueError:
            print('You wrote incorrect value')
        else:
            if len(lst) >= length:
                return lst

def intersection_dots() -> list:
    D = (b - k) ** 2 - 4 * a * (c - m)
    if D > 0:
        return sorted(((- (b - k) - D ** 0.5) / (2 * a), (- (b - k) + D ** 0.5) / (2 * a)))
    if D == 0:
        return [- (b - k) / (2 * a)]
    return []

def parabola(x: float) -> float:
    return a * x ** 2 + b * x + c

def straight(x: float) -> float:
    return k * x + m

def xrange(start: float, stop:float) -> list:
    step = (stop - start) / 100
    array = []
    for i in range(100):
        array.append(start + step * i)
    array.append(stop)
    return array

a, b, c = get_values('Enter a, b, c for square equation (y=ax^2+bx+c) separated by space: ', 3)
k, m = get_values('Enter k and m for square equation (y=kx+m) separated by space: ', 2)

intersections = intersection_dots()
if len(intersections) == 2:
    print(f'Two intersection points: ({intersections[0]:.2e}, {straight(intersections[0]):.2e}), ({intersections[1]:.2e}, {straight(intersections[1]):.2e})')
    diff = intersections[1] - intersections[0]
    xs = xrange(intersections[0] - 3 * diff, intersections[1] + 3 * diff)
    ys = [straight(x) for x in xs]
    yp = [parabola(x) for x in xs]


elif len(intersections) == 1:
    print(f'One intersection point: ({intersections[0]:.2e}, {straight(intersections[0]):.2e})')
    top = - b / (2 * a)
    diff = abs(top - intersections[0]) if abs(top - intersections[0]) != 0 else a
    base_dots = sorted([top, intersections[0]])
    xs = xrange(base_dots[0] - 3 * diff, base_dots[1] + 3 * diff)
    ys = [straight(x) for x in xs]
    yp = [parabola(x) for x in xs]


else:
    print('They don\'t intersect.')
    top = - b / (2 * a)
    xs = xrange(0.5 * top, 1.5 * top)
    ys = [straight(x) for x in xs]
    yp = [parabola(x) for x in xs]

plt.plot(xs, ys)
plt.plot(xs, yp)
plt.show()
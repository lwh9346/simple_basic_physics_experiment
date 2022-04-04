import numpy
import math
from matplotlib import pyplot
from typing import Union


def linear_fit(X: Union[numpy.ndarray, list], Y: Union[numpy.ndarray, list]) -> dict:
    if isinstance(X, list):
        X = numpy.array(X)
    if isinstance(Y, list):
        Y = numpy.array(Y)
    assert isinstance(X, numpy.ndarray)
    assert isinstance(Y, numpy.ndarray)
    assert len(X.shape) == 1
    assert len(Y.shape) == 1
    assert len(X) == len(Y)
    assert len(X) > 2
    xy = X*Y
    xx = X*X
    yy = Y*Y
    m_x = X.mean()
    m_y = Y.mean()
    m_xy = xy.mean()
    m_xx = xx.mean()
    m_yy = yy.mean()
    a1 = (m_xy-m_x*m_y)/(m_xx-m_x**2)
    a0 = m_y-a1*m_x
    r = (m_xy-m_x*m_y)/math.sqrt((m_xx-m_x**2)*(m_yy-m_y**2))
    n = len(X)
    sigma_square = ((Y-a0-a1*X)**2).sum()/(n-2)
    sigma_a1 = a1*math.sqrt((1/r**2-1)/(n-2))
    sigma_a0 = a1*math.sqrt((1/r**2-1)/(n-2))
    result = {
        "a1": a1,
        "a0": a0,
        "r": r,
        "n": n,
        "sigma_square": sigma_square,
        "sigma_a1": sigma_a1,
        "sigma_a0": sigma_a0,
    }
    return result


def plot_linear_fit_result(X: Union[numpy.ndarray, list], Y: Union[numpy.ndarray, list], x_lable: str, y_label: str, title: str) -> None:
    result = linear_fit(X, Y)
    print(result)
    if isinstance(X, list):
        X = numpy.array(X)
    if isinstance(Y, list):
        Y = numpy.array(Y)
    max_x = X.max()
    min_x = X.min()
    dx = max_x-min_x
    max_x += dx*0.05
    min_x -= dx*0.05
    max_yp = result["a1"]*max_x + result["a0"]
    min_yp = result["a1"]*min_x + result["a0"]
    pyplot.figure(figsize=(8.3, 5.8), dpi=300)
    pyplot.plot(X, Y, "b+")
    pyplot.plot([min_x, max_x], [min_yp, max_yp], "r-")
    pyplot.xlabel(x_lable)
    pyplot.ylabel(y_label)
    pyplot.title(title)
    pyplot.savefig("fig.png")
    pyplot.close()


if __name__ == "__main__":
    # example
    plot_linear_fit_result(
        [1, 2, 3, 4, 5, 6],
        [1, 2, 4, 4, 5, 6],
        "time/s", "x/m", "x-t")

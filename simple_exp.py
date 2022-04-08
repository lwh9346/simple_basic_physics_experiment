from tkinter.messagebox import NO
import numpy
import math
from matplotlib import pyplot
from typing import Union


def __print_dict(d: dict, title="") -> None:
    if title != "":
        print("====begin {}====".format(title))
    for k, v in d.items():
        print("{:<15}:{}".format(k, v))
    if title != "":
        print("====end {}====".format(title))


def linear_fit(X: Union[numpy.ndarray, list], Y: Union[numpy.ndarray, list]) -> dict:
    """返回以字典表示的线性拟合结果"""
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
        "function": "y=a1*x+a0",
        "a1": a1,
        "a0": a0,
        "r": r,
        "n": n,
        "sigma_square": sigma_square,
        "sigma_a1": sigma_a1,
        "sigma_a0": sigma_a0,
    }
    return result


def plot_linear_fit_result(X: Union[numpy.ndarray, list], Y: Union[numpy.ndarray, list], x_lable="x", y_label="y", title="x-y", file_name="fig.png") -> dict:
    """返回以字典表示的线性拟合结果，并根据指定文件名绘制图像"""
    result = linear_fit(X, Y)
    __print_dict(result, title="linear fit result")
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
    pyplot.savefig(file_name)
    pyplot.close()
    return result


def plot_curve(X: Union[numpy.ndarray, list], Y: Union[numpy.ndarray, list], x_lable="x", y_label="y", title="x-y", file_name="fig.png", show=False) -> None:
    """绘制一段曲线的图像"""
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
    pyplot.figure(figsize=(8.3, 5.8), dpi=300)
    pyplot.plot(X, Y, "r-")
    pyplot.plot(X, Y, "b+")
    pyplot.xlabel(x_lable)
    pyplot.ylabel(y_label)
    pyplot.title(title)
    pyplot.savefig(file_name)
    if show:
        pyplot.show()
    pyplot.close()


def load_csv_XY(f: str) -> tuple[numpy.ndarray, numpy.ndarray]:
    """读取csv文件的两列"""
    X, Y = [], []
    with open(f, encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            tmp = line.strip().split(",")
            try:
                x = float(tmp[0])
                y = float(tmp[1])
            except BaseException as e:
                print(e)
                continue
            X.append(x)
            Y.append(y)
    return numpy.array(X), numpy.array(Y)

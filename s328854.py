import numpy as np


def f1(x: np.ndarray) -> np.ndarray:
    return np.sin(x[0])

def f2(x: np.ndarray) -> np.ndarray: 
    return np.add(np.add(np.add(np.multiply(x[0],16.0000),np.multiply(3.000, x[2])),np.multiply(x[1],4.0000)),np.add(x[2],x[0])) * np.cosh(np.subtract(np.abs(np.abs(np.subtract(9.5371,-2.2543))),np.sin(np.sin(np.sin(np.sin(np.sin(np.sin(np.sin(np.sin(np.sinh(np.sin(np.divide(x[2],x[1])))))))))))))

def f3(x: np.ndarray) -> np.ndarray:
    return np.subtract(np.add(np.subtract(np.multiply(np.multiply(x[0],x[0]),2),np.multiply(np.sinh(x[1]),2)),np.multiply(np.tanh(6.5153),4)),np.multiply(x[2],3))

def f4(x: np.ndarray) -> np.ndarray:
    return np.cosh(np.cosh((np.arctan(-3.2684) + np.divide(x[0],x[0])))) + np.sinh((np.cosh(np.cosh(np.cosh((np.arctan(-1.3125) + np.divide(x[0],x[0]))))) * np.tanh(np.cos(x[1])))) + (np.cosh((np.arctan(-1.8241) + (x[0] / 13.9523))) + np.sinh((np.cosh(np.cosh(np.arctan(-2.0000))) * np.tanh(np.cos(x[1])))))

def f5(x: np.ndarray) -> np.ndarray:
    return np.multiply(np.subtract(np.add(np.subtract(np.multiply(np.cosh(x[1]),np.sin(x[0])),np.cosh(x[1])),np.add(x[1],x[0])),np.tanh(np.subtract(np.add(x[1],x[0]),np.cosh(x[1])))),np.cos(np.arctan(np.sinh(np.sinh(-4.3606)))))

def f6(x: np.ndarray) -> np.ndarray:
    return (1.6943 * x[1]) + ((-6.0562 * x[0]) * np.abs(0.1147))
    # return (((np.tanh(x[0]) + (x[1] - x[0])) - (x[1] / 5.3981)) + x[1])

def f7(x: np.ndarray) -> np.ndarray:
    # return  ((np.cos(np.arctan((x[0] - x[1]))) * (np.cos((x[0] - x[1])) * (np.exp((x[1] * x[0])) + np.cos((x[0] - x[1]))))) * np.exp(np.cosh(np.cos((x[0] - x[1])))))
    return (((((((np.exp((x[0] * x[1])) + (np.exp((x[0] * x[1])) + np.exp((x[0] * x[1])))) + np.exp((x[0] * x[1]))) + (np.exp((x[0] * x[1])) + np.exp((x[0] * x[1])))) * np.cos((x[1] - x[0]))) * np.cos((x[1] - x[0]))) \
                     * ((((((np.sqrt(0.9846) ** (x[0] * x[1])) ** (x[0] * x[1])) ** (x[0] * x[1])) ** (((np.sqrt(0.9846) ** (x[0] * x[1])) ** (x[0] * x[1])) ** (x[0] * x[1]))) - np.abs((x[0] - x[1]))) * np.sqrt(np.log(np.abs(8.3360))))) \
                    * ((((((((np.sqrt(0.9846) ** (x[0] * x[1])) ** (x[0] * x[1])) ** (x[0] * x[1])) ** (((np.sqrt(0.9846) ** (x[0] * x[1])) ** (x[0] * x[1])) ** (x[0] * x[1]))) - np.abs((x[0] - x[1]))) * np.sqrt(np.log(np.abs(8.4773))))\
                        * np.cos((x[1] - x[0]))) * (((((np.sqrt(0.9846) ** (x[0] * x[1])) ** (x[0] * x[1])) ** (x[0] * x[1])) ** (((np.sqrt(0.9846) ** (x[0] * x[1])) ** (x[0] * x[1])) ** (x[0] * x[1]))) - np.abs((x[0] - x[1]))) * np.sqrt(np.log(8.3360))))

def f8(x: np.ndarray) -> np.ndarray: 
    return  ((np.sinh(x[5])) + np.multiply(x[5],7) - 6.7372) * np.abs((np.sinh(x[5])) + np.multiply(x[5],15))
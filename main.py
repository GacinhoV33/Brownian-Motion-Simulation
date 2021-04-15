#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
from matplotlib import pyplot as plt


def main():
    n = 10000
    d = 5
    T = 1.
    times = np.linspace(0., T, n)
    dt = times[1] - times[0]
    dB = np.sqrt(dt) * np.random.normal(size=(n-1, d))

    B0 = np.zeros(shape=(1, d))
    B = np.concatenate((B0, np.cumsum(dB, axis=0)), axis=0)
    plt.figure(num=1)
    plt.plot(times, B)
    plt.grid()
    plt.title("Brownian motion")
    plt.savefig("Brownian_Motion_figure.png")
    plt.show()

if __name__ == "__main__":
    main()
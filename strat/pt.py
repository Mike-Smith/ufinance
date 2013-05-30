#!/bin/python
# -*- coding: utf-8 -*-

''' This is used to test sqlite3 '''

import sqlite3 as sqlite
import numpy
import matplotlib.pyplot as plot
if __name__ == '__main__':
    cx = sqlite.connect("/home/yun/workspace/pt/stock.sqlite")
    cu = cx.cursor()
    cu.execute("select  time, open  from ticks where symbol=\"DL\" order by time")
    rlt = cu.fetchall()
    cu.close();
    data=numpy.array(rlt)
    plot.figure(figsize=(8,4))
    plot.plot(data[:, 0],data[:, 1],label="$sin(x)$",color="red",linewidth=1)
    plot.xlabel("Time(s)")
    plot.ylabel("Volt")
    plot.title("PyPlot First Example")
    #plot.ylim(-1.2,1.2)
    plot.legend()
    plot.show()

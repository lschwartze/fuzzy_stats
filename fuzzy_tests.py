# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 14:59:56 2023

@author: laurin
"""

import matplotlib.pyplot as plt
from fuzzy_stats import geothmetic_meandian, progress_
from random import randint as rnd

test_list = [rnd(1, 10000) for _ in range(10000)]

a = geothmetic_meandian(test_list, max_iter = 1000, tol = 10**-5)

a_mean = [progress_[i][0] for i in range(len(progress_))]
g_mean = [progress_[i][1] for i in range(len(progress_))]
med = [progress_[i][2] for i in range(len(progress_))]

plt.plot(a_mean, label = 'arihtmetic mean')
plt.plot(g_mean, label = 'geomtric mean')
plt.plot(med, label = 'median')
plt.plot(len(progress_)-1, a, 'b+', label = 'geothmetic meandian')
plt.legend()
plt.show()
print(a)

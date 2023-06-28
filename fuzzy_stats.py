# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 12:11:56 2023

@author: laurin
"""

progress_ = []

def geothmetic_meandian(*args, max_iter=100, tol=10**-3):
    if len(args) == 1:
        nums = list(args[0])
    else:
        nums = list(args)
    res_ = (arithmetic_mean(nums), geometric_mean(nums), median(nums))
    progress_.append(res_)
    max_iter = max_iter - 1
    if max_iter == 0:
        return res_[0]
    if abs(res_[0] - res_[1]) < tol and abs(res_[1] - res_[2]) < tol and abs(res_[0] - res_[2]) < tol:
        return res_[0]
    else:
        return geothmetic_meandian(*tuple(res_), max_iter = max_iter, tol = tol)

def arithmetic_mean(nums):
    return sum(nums)/len(nums)

def geometric_mean(nums):
    p = 1
    for n in nums:
        p *= n**(1/len(nums))
    return p

def median(nums):
    nums.sort()
    if len(nums)%2 == 0:
        return (nums[int(len(nums)/2)] + nums[int(len(nums)/2-1)])/2
    else:
        return nums[int((len(nums)/2))]
    
# -*- coding:utf-8 -*-
# @Author:   陶然至上
# @Email:    taoranzhishang@gmail.com
# @File:     I_Miss_You.py
# @Time:     2022/07/18 01:00
# @Software: PyCharm

"""
当阳光照在海面上，我在思念你
当朦胧月色洒在泉水里，我在思念你
                    ————《假如爱有天意》
"""


class Man:
    def __init__(self, name):
        self.name = name

    def miss(self, darling):
        print("{} is missing {}".format(self.name, darling))


sunshine_spilling_over_the_sea = True
hazy_moonlight_spilling_into_the_spring = True

I = Man("T")

while sunshine_spilling_over_the_sea:
    while hazy_moonlight_spilling_into_the_spring:
        I.miss("L")


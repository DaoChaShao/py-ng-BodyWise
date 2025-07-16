#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/7/16 23:14
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   helper.py
# @Desc     :   


class BMICalculator(object):
    """ A class to calculate Body Mass Index (BMI) based on height and weight. """

    def __init__(self, height: float, weight: float):
        """ Initialise the BMICalculator with height and weight.
        :param height: Height in meters
        :param weight: Weight in kilograms
        """
        self._height: float = height
        self._weight: float = weight
        self._bmi: float = 0.0

    def calculate(self) -> float:
        """ Calculate the BMI value.
        :return: Calculated BMI value rounded to two decimal places
        """
        if self._height <= 0 or self._weight <= 0:
            raise ValueError("Height and weight must be positive values.")

        # Calculate BMI using the formula: weight (kg) / (height (m) ** 2)
        self._bmi: float = self._weight / (self._height ** 2)
        # Return BMI rounded to two decimal places
        return round(self._bmi, 2)

    def get_category(self):
        if self._bmi < 18.5:
            return "Underweight"
        elif self._bmi < 24:
            return "Normal"
        elif self._bmi < 28:
            return "Overweight"
        else:
            return "Obese"

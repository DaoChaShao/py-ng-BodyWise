#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/7/16 23:14
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   helper.py
# @Desc     :   

from asyncio import sleep
from datetime import datetime
from random import randint
from nicegui import ui


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
        """ Get the BMI category based on the calculated BMI value """
        if self._bmi < 18.5:
            return "Underweight"
        elif self._bmi < 24:
            return "Normal"
        elif self._bmi < 28:
            return "Overweight"
        else:
            return "Obese"


async def evaluation_generator(message_area, height: float, weight: float) -> None:
    """ A generator function to yield evaluation messages
    :param message_area: The area to display messages
    :param height: Height in meters
    :param weight: Weight in kilograms
    :return: None
    """
    # Initialise the BMI calculator
    bmi = BMICalculator(height, weight)

    # Initialise the chat messages — Clear previous messages
    message_area.clear()

    # Push the calculated BMI to the chat messages
    with message_area:
        ui.chat_message(
            "Calculating your BMI, please wait...",
            name="BodyWise Bot", stamp=f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            avatar="https://robohash.org/ui.png",
        ).classes("")

        # Simulate a delay for the calculation
        delay: int = randint(1, 3)
        print(f"Simulating a delay of {delay} seconds for BMI calculation...")
        await sleep(delay)

        # Calculate the BMI and get the category
        ui.chat_message(
            f"Your BMI is: {bmi.calculate()}, and category is: {bmi.get_category()}",
            name="BodyWise Bot", stamp=f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            avatar="https://robohash.org/ui.png",
        ).classes("")

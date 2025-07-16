#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/7/16 15:50
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   a_home.py
# @Desc     :   

from nicegui import ui

from layout import layout
from utils.helper import BMICalculator


def main() -> None:
    """ Set the home page of the BodyWise application """
    # Set the title of the page
    ui.label("BodyWise Application").classes("text-2xl font-bold")
    ui.label("Your personal fitness assistant").classes("text-base text-gray-600")
    ui.separator()

    # Set the main content of the home page
    with ui.card().classes("w-full"):
        # Set the grid layout for the card content
        with ui.grid(columns=2).classes("w-full items-start gap-4"):
            # Set the left column content
            with ui.column().classes("gap-2"):
                # Set the height of the user
                ui.label("User Height").classes("font-semibold")
                height = ui.slider(min=1.2, max=2.5, step=0.01, value=1.65).classes("w-full")
                ui.label().bind_text_from(
                    height, "value", lambda v: f"Height: {v} M"
                ).classes("text-xs text-gray-500")
                # Set the weight of the user
                ui.label("User Weight").classes("font-semibold")
                weight = ui.slider(min=30, max=200, step=0.1, value=70).classes("w-full")
                ui.label().bind_text_from(
                    weight, "value", lambda v: f"Weight: {v} KG"
                ).classes("text-xs text-gray-500")

            # Set the right column content
            with ui.column().classes("gap-2"):
                gender = ui.select(["Male", "Female", "Other"], label="Gender").classes("w-full")
                ui.label().bind_text_from(gender, "value", lambda v: f"{v}").classes("text-xs text-gray-500")

                age = ui.select(list(range(1, 101)), label="Age").classes("w-full")
                ui.label().bind_text_from(age, "value", lambda v: f"{v}").classes("text-xs text-gray-500")

        # Initialise the BMI calculator
        bmi = BMICalculator(height.value, weight.value)

        # Set the button to calculate BMI
        ui.button("Calculate BMI", on_click=bmi.calculate).classes("w-full")


@ui.page("/")
def home() -> None:
    layout(main)

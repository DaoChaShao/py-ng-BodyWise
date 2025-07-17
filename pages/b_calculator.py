#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/7/17 17:07
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   b_calculator.py
# @Desc     :   

from datetime import datetime
from nicegui import ui

from layout import layout
from utils.helper import evaluation_generator


def main() -> None:
    """ Main Function """
    # Set the main content of the core functions page
    with ui.card().classes("w-full"):
        
        ui.label("Enter Your BMI Information").classes("text-lg font-semibold mb-4")

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

        # Set the button to calculate BMI
        ui.button(
            "Calculate BMI",
            on_click=lambda: evaluation_generator(message_area, height.value, weight.value)
        ).classes("w-full")

    # Set the message area to display the evaluation results
    message_area = ui.column()


@ui.page("/bmi")
def calculator() -> None:
    layout(main)

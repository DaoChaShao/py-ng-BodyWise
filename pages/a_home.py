#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/7/16 15:50
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   a_home.py
# @Desc     :   

from nicegui import ui

from layout import layout


def main() -> None:
    """ Set the home page of the BodyWise application """
    # Set the title of the page
    ui.label("BodyWise Application").classes("text-2xl font-bold")
    ui.label("Your personal fitness assistant").classes("text-base text-gray-600")
    ui.separator()

    # Set the introduction text
    with ui.expansion(
            "This is a simple web application to help you manage your fitness journey.",
            value=True,
    ).classes("w-full"):
        ui.markdown("- Welcome to **BodyWise**!")
        ui.markdown("- This application is a great attempt at building with **NiceGUI**.")
        ui.markdown("- It can tell you your **BMI** and **weight category** based on your height and weight.")
        ui.markdown("- If time permits, the app may provide general suggestions on adjusting your BMI.")
        ui.markdown("- If time permits, you'll see a **richer UI** and **interactive experience**.")
        ui.markdown("- If time permits, the app can use your personal information to offer smart suggestions.")
        ui.markdown("- I hope this is a valuable and meaningful experiment.")


@ui.page("/")
def home() -> None:
    layout(main)

#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/7/16 15:50
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   layout.py
# @Desc     :   

from nicegui import ui


def layout(page_func) -> None:
    """ Define the layout of the BodyWise application
    :param page_func: Function to render the main content of the page
    :type page_func: function
    :return: None
    """
    # Set a main row with two columns: sidebar and main content
    with ui.row().classes("w-full h-screen no-wrap"):
        # Set the Sidebar Area
        with ui.column().classes("w-1/4 bg-grey-2 p-4 h-full"):
            # Set the Sidebar Header: ensure elements are centered vertically and horizontally
            with ui.row().classes("items-center justify-center gap-2"):
                ui.icon("menu", size="text-2xl").classes("text-primary")
                ui.label("Menu").classes("text-xl font-bold text-primary")

            # Add a separator for visual clarity
            ui.separator().classes("mb-4")

            # Set the Sidebar Navigation Buttons of the Home Page with Expansions
            with ui.expansion(
                    "INTRODUCTION", icon="home", value=True,
                    caption="The Brief Introduction"
            ).classes("w-full"):
                ui.button(
                    "Home",
                    on_click=lambda: ui.navigate.to("/"),
                ).classes("w-full justify-start")

            # Set the Sidebar Navigation Buttons of the Core Functions with Expansions
            with ui.expansion(
                    "CORE FUNCTIONS", icon="dashboard", value=True,
                    caption="Main Features"
            ).classes("w-full"):
                ui.button(
                    "BMI Calculator",
                    on_click=lambda: ui.navigate.to("/bmi"),
                ).classes("w-full justify-start")

            # Set the Sidebar Navigation Buttons of the Information Section with Expansions
            with ui.expansion(
                    "INFORMATION", icon="info", value=True,
                    caption="Useful Information"
            ).classes("w-full"):
                ui.button(
                    "About",
                    on_click=lambda: ui.navigate.to("/about"),
                ).classes("w-full justify-start")

        # Set the Main Content Area
        with ui.column().classes("w-3/4 p-6"):
            page_func()

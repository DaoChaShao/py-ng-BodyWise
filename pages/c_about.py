#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/7/17 18:34
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   c_about.py
# @Desc     :   

from nicegui import ui

from layout import layout


def main() -> None:
    """ Set the home page of the BodyWise application """
    # Set the title of the page
    ui.label("About").classes("text-2xl font-bold")
    ui.separator()

    # Set the introduction text
    with ui.expansion(
            "This is a brief overview of the technical highlights.",
            value=True,
    ).classes("w-full"):
        ui.markdown("- Built with the **NiceGUI** framework for responsive web UI.")
        ui.markdown("- Can integrate **OpenAI** or **DeepSeek API** for intelligent health suggestions.")
        ui.markdown("- Supports **prompt engineering** and **user profiling** for personalized recommendations.")
        ui.markdown("- Future upgrades may include richer UI elements and enhanced data interaction.")


@ui.page("/about")
def about() -> None:
    layout(main)

#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/7/15 23:09
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   main.py
# @Desc     :   

from nicegui import ui

from pages import a_home
from pages import b_calculator
from pages import c_about

ui.run(title="BodyWise", port=8080)

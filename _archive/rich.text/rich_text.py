#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rich.console import Console
from rich.style import Style

console = Console()

style_green_bold = Style(color="green", bold=True)
style_red_bold = Style(color="red", bold=True)
style_blue_bold = Style(color="blue", bold=True)
style_yellow_bold = Style(color="yellow", bold=True)

def print_text(input_text, rich_style):
    console.print(input_text, style=rich_style)

def green_bold(input_text):
    print_text(input_text, style_green_bold)

def red_bold(input_text):
    print_text(input_text, style_red_bold)

def blue_bold(input_text):
    print_text(input_text, style_blue_bold)

def yellow_bold(input_text):
    print_text(input_text, style_yellow_bold)

green_bold("This is green bold text")
red_bold("This is red bold text")
blue_bold("This is blue bold text")
yellow_bold("This is yellow bold text")


"""Конфигуратор данного проекта как отдельного модуля/пакета"""
import os
from setuptools import setup, find_packages

path = os.path.join(os.path.abspath("../.."), "README.md")
long_description = ""

if os.path.exists(path):
    with open(path, "r") as f:
        long_description = f.read()

setup(
    name="mai_course_bot",
    version="0.0.0",
    description="Telegram Bot",
    long_description=long_description,
    packages=find_packages()
)

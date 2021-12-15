from setuptools import setup, find_packages

setup(
    name="dealerschoice",
    version="1.0.1",
    packages=find_packages(exclude=["tests*"]),
    license="MIT",
    description="A python package to generate playing cards and use them to play a game of Blackjack in the terminal.",
    url="https://github.com/The0therChad/DATA533-Lab3.git",
    author="Sean-C-Casey & The0therChad",
    author_email="cjwheelz@student.ubc.ca",
)

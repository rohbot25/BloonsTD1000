# BloonsTD1000
Our team will create a tower defense game in python. We are currently planning on using the pygame library for development but are still unsure. This game will consist of adversaries and towers. The adversaries will travel down a road towards a target location. Once enough adversaries reach that location the game ends and the user loses. The user will place towers around the road which will eliminate the adversaries. The user will try to eliminate all adversaries before they can reach their target location.  

Our current thinking is that we will have two basic classes, towers and fish. Towers will have a range and damage value. Different towers will have different values depending on the type. Fish will have a health and speed value. Different color fish will have different values. We will have child classes for each of these two parent classes which will provide variety and excitement. For example a blue bubble is a bubble with more health but less speed. A bomb tower is a tower with more damage and less range.

We will start by developing 1 path and then once we have achieved functionality for our first path we will hopefully progress to having multiple levels. This will allow us to have a win state for levels which will create a more entertaining and fulfilling game. Below is some ai generated concept art to help visualize.


NEED THE FOLLOWING TO RUN
Python 3.9 or later,
Py arcade for the following:
import arcade
import arcade.gui

This can be installed with "pip install arcade."

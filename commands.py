import random
from termcolor import colored
import os
import time
from kernel import process_management
import webbrowser
from conf import Configuration

class CommandProcessor:
  @staticmethod
  @process_management(priority=3)
  def cmd():
    print("showfetch, usrdata, systurnoff, bored, ota, hme")

  @staticmethod
  @process_management(priority=1)
  def ota():
    webbrowser.open("https://www.figma.com/proto/gVbll3jSnVPksZsyF6wghE/Untitled?node-id=0-1&p=f&t=4wQynKV5aFOD5vNf-0&scaling=min-zoom&content-scaling=fixed&page-id=0%3A1")

  @staticmethod
  @process_management(priority=2)
  def usrdata():
    usr = Configuration.get_user()
    print(usr)

  @staticmethod
  @process_management(priority=1)
  def systurnoff():
    exit()
  @staticmethod
  @process_management(priority=3)
  def showfetch():
    usr = Configuration.get_user()
    ui = Configuration.get_ui()
    print("User:", usr)
    print("OS:", os.name)
    print("UI:", ui)

  @staticmethod
  @process_management(priority=1)
  def hme():
      webbrowser.open("https://www.figma.com/proto/6BIq0bwjp4UNTA4k137S5L/hexmobenv?node-id=1-1587&t=VtsHSvo6nCksWXqK-0&scaling=min-zoom&content-scaling=fixed&page-id=0%3A1")

  @staticmethod
  @process_management(priority=2)
  def bored():
    print("AI:", random.choice([
        "You can play a game.",
        "If youre bored, watch some movies. Some good ones are: The Matrix, Inception, Interstellar, Cassandra, Rick and Morty, and The Simpsons.",
        "If youre bored, you can go outside and take a walk. Fresh air is good for you.",
        "If youre bored, read a book. Some good ones are: The Hitchhiker's Guide to the Galaxy, 1984, Brave New World, and The Great Gatsby.",
        "Listen some musics, podcasts.",
        "If youre a good programmer, you can try to make a game, or anything you want.",
        "Read Wikipedia articles, to learn something new!",
        "Yoou can cook something new, or try to make a new recipe.",
        "You can watch social media, like TikTok, Instagram, or Twitter.",
        "You can play with your pets, if you have any.",
    ]))

  @staticmethod
  @process_management(priority=1)
  def trigger_panic():
    time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print("Current date and time:", time)

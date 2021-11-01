from tkinter.constants import Y
from pyautogui import *
import pyautogui
import random
import time
import keyboard
import random
import win32api, win32con

def get_mouse():
    current_pos = pyautogui.position()
    current_x = current_pos.x
    current_y = current_pos.y

def smooth_mouse_move(x, y, t):
    pyautogui.moveTo(x, y, t)

def LMouseClick(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

class player_stats:
    '''player stats. currently crude representations of hitpoints, prayer, adrenaline, and binary needs refill or not. '''
    def __init__(self, name, location, needs_refill):
        self.name = name #the stat name
        self.location = location #will be the click region.
        self.needs_refill = needs_refill #boolean, used to toggle ss, drink prayer, etc. 

class player_ability:
    def __init__(self, name, location, duration, cd_time, cd_status, active_status):
        self.name = name #the ability name
        self.location = location #click point on screen.
        self.duration = duration #abilityduration
        self.cd_time = cd_time #cooldown time
        self.cd_status = cd_status #is on or off cd
        self.active_status = active_status #is currently being used or not

class player_item:
    def __init__(self, name, location, cooldown, count):
        self.name = name #the item name
        self.location = location #location in the inventory. Not super critical currently, but likely to be helpful in the future when a tray is created (an actual inventory)
        self.cooldown = cooldown #not sure how I feel about this, as not all items will have cooldowns. may need to be moved to a subclass.
        self.count = count #the quantity of the item in the inventory


class hitpoints(player_stats):
    '''subclass of player stats, inheriting all player stat properties.'''
    def __init__(self, name, location, needs_refill):
        super().__init__(name, location, needs_refill)

    hp = pyautogui.locateOnScreen(r'C:\Users\19512\Desktop\Python Code\Automation Test\full_life_points_bar.png')
    hp_width = 88
    hp_height = 10
    hp_point = pyautogui.center(hp)


class prayer(player_stats):
    def __init__(self, name, location, needs_refill):
        super().__init__(name, location, needs_refill)

    prayer_points = pyautogui.locate(r'C:\Users\19512\Desktop\Python Code\Automation Test\full_prayer_bar.png')


class adrenaline(player_stats):
    def __init__(self, location, needs_refill):
        super().__init__(location, needs_refill)

    empty_adren = pyautogui.locateOnScreen(r'C:\Users\19512\Desktop\Python Code\Automation Test\empty_adren_bar.png')

class soulsplit(player_ability):
    def __init__(self, name, location, duration, cd_time, cd_status, active_status):
        super().__init__(name, location, duration, cd_time, cd_status, active_status)

    ss = pyautogui.locateOnScreen(r'C:\Users\19512\Desktop\Python Code\Automation Test\Soulsplit.png')

class prayer_pot(player_item):
    def __init__(self, name, location, cooldown, count):
        super().__init__(name, location, cooldown, count)
    
    prayer_potion = pyautogui.locateOnScreen(r'C:\Users\19512\Desktop\Python Code\Automation Test\Super Prayer Renewal.png')

    name = 'Super prayer renewal potion'





class hitpoints:  
    '''simple. hitpoints.'''

    def __init__(self, location, isFull): #location on screen and binary fill amount
        self.location = location #such as an idea id [1, 2 3,... ]
        self.isFull = isFull #such as a name [super lazer gun of death, Code004, my_s3cr3t_1d]

    def verify(self):
        while True:
            try:
                hp_location = pyautogui.locateOnScreen(r'C:\Users\19512\Desktop\Python Code\Automation Test\full_life_points_bar.png')
                break
            except ValueError: 
                print('Cannot find HP bar, please make sure you are full HP or the bar is visible.')

        hp_point = pyautogui.center(hp_location)
        setattr(self, 'location', hp_point)

class prayer:
    '''prayer points'''

    def __init__(self, location, isFull): #location on screen and binary fill amount
        self.location = location #such as an idea id [1, 2 3,... ]
        self.isFull = isFull #such as a name [super lazer gun of death, Code004, my_s3cr3t_1d]

    def verify(self):
        while True:
            try:
                pp_location = pyautogui.locateOnScreen(r'C:\Users\19512\Desktop\Python Code\Automation Test\full_prayer_bar.png')
                break
            except ValueError: 
                print('Cannot find Prayer bar, please make your prayer points are full or the bar is visible.')

        prayer_point = pyautogui.center(pp_location)
        setattr(self, 'location', prayer_point)

class adrenaline:
    '''adrenaline. will need to be slightly different than the other two classes, may need to implement % for thresh'''

    def __init__(self, location, isFull): #location on screen and binary fill amount
        self.location = location #such as an idea id [1, 2 3,... ]
        self.isFull = isFull #such as a name [super lazer gun of death, Code004, my_s3cr3t_1d]

    def verify(self):
        while True:
            try:
                adren_location = pyautogui.locateOnScreen(r'C:\Users\19512\Desktop\Python Code\Automation Test\empty_adren_bar.png')
                break
            except ValueError: 
                print('Cannot find adrenaline bar, please make your adrenaline points are full or the bar is visible.')

        adren_point = pyautogui.center(adren_location)
        setattr(self, 'location', adren_point)

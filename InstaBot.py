#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 19:53:35 2020

@author: paul
"""


from selenium import webdriver
from time import sleep
#from selenium.webdriver.common.keys import Keys
#import pyautogui

class InstaBot:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome('/Users/paul/Desktop/python/chromedriver')
        self.driver.get("https://instagram.com")
        self. username = username
        sleep(2)
        
        user_path = '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input'
        self.driver.find_element_by_xpath(user_path).send_keys(username)
        pass_path = '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input'
        self.driver.find_element_by_xpath(pass_path).send_keys(password)
        #alternatve find_element_by_xpath("//a[contains(text(), 'Log in')]").click
        login_path = '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div'
        self.driver.find_element_by_xpath(login_path).click()  
    
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()
     
        no_notifications = '/html/body/div[4]/div/div/div[3]/button[2]'
        sleep(4)
        self.driver.find_element_by_xpath(no_notifications).click()  
        
        sleep(2)
        
    def get_unfollower(self):
        self.driver.find_element_by_xpath("//a[contains(@href, '/{}')]".format(self.username))\
            .click()
        sleep(5)
        
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a').click()
        following = self._get_names()
        
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a').click()
        followers = self._get_names()
        not_following_back = [user for user in following if user not in followers]
        print(len(followers))
        print(len(following))
        print(len(not_following_back))
        print(not_following_back)
        
    
            
    def _get_names(self):
        sleep(1)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div")
        while True:
           
            prev_links = scroll_box.find_elements_by_tag_name('a')
            self.driver.execute_script('arguments[0].scrollIntoView()', prev_links[-1])
            sleep(1)
            check = scroll_box.find_elements_by_tag_name('a')    
            if prev_links == check:
                break
            
            
        
            
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/button').click() 
        return names


my_bot = InstaBot('paulpermantier','Stella321.')
my_bot.get_unfollower()
#stella_bot = InstaBot('stellapmtr', 'DKtdTki105')
#stella_bot.get_unfollower()
#random_bot = InstaBot('raketenronja', 'Sailormoon1')
#random_bot.get_unfollower()
        
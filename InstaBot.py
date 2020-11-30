from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class instaBot:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.bot = webdriver.Firefox()

	def openInsta(self):
		self.bot.get('https://www.instagram.com/')
		time.sleep(5)

	def login(self):
		username = self.bot.find_element_by_name('username')
		password = self.bot.find_element_by_name('password')
		username.clear()
		password.clear()
		username.send_keys(self.username)
		time.sleep(3)
		password.send_keys(self.password)
		time.sleep(3)
		password.send_keys(Keys.RETURN)
		time.sleep(5)
		self.bot.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
		time.sleep(3)
		self.bot.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
		time.sleep(3)

	def hash(self):
		self.bot.get('https://www.instagram.com/explore/tags/tweetmemes/')
		time.sleep(5)
		self.bot.find_element_by_class_name('v1Nh3').click() # First post after searching hash
		self.bot.find_element_by_class_name('wpO6b').click() # Like
		time.sleep(3)
		for i in range(5):
			self.bot.find_element_by_class_name('_65Bje').click() # Next
			time.sleep(3)
			self.bot.find_element_by_class_name('wpO6b').click() # Like
			time.sleep(3)

	def comment(self):
		comments = open("comments.txt", "r")
		self.bot.get('https://www.instagram.com/explore/tags/memes/')
		time.sleep(5)
		self.bot.find_element_by_class_name('v1Nh3').click() # First post after searching hash
		time.sleep(3)
		for i in range(5):
			for comment in comments:
				pass
			



def startBot():
	insta = instaBot('rajeshv_alluri', '84676211a')
	insta.openInsta()
	insta.login()
	insta.hash()
	#insta.comment()

startBot()
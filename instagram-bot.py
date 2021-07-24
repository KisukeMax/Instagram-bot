import urllib.request
from instabot import Bot
import os 
import glob

if glob.glob("config/*cookie.json"):
	cookie_del = glob.glob("config/*cookie.json")
	os.remove(cookie_del[0])
	
#import image 
urllib.request.urlretrieve("https://images.newscientist.com/wp-content/uploads/2021/06/03141753/03-june_puppies.jpg" , "temp.jpg")

bot = Bot()
#please Enter your login details
bot.login(username = "", 

          password = "")

bot.upload_photo("temp.jpg",

                 caption ="Posted using Python")


#delete temp image 
del_img = glob.glob("temp.jpg.REMOVE_ME")
os.remove(del_img[0])
from instabot import Bot

bot = Bot()

bot.login(username = "user_name", password = "password")

bot.upload_photo("bot.jpg", caption = "this post was uploaded by a bot for demonstation and testing purposes, will be removed momentarily")

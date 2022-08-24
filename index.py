#Every 10s check if there are new games
import requests
#Libraries for Windows notification
from win10toast import ToastNotifier

url = "https://api.plenusbot.xyz/epic_games?country=IT"
response = requests.get(url).json()
# Title of current games
current_games = response['currentGames'][0]['title']

toaster = ToastNotifier()
toaster.show_toast("New free game on the Epic Games Store:", current_games, icon_path="epicgames.png")
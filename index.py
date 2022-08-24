import requests

from win10toast import ToastNotifier

filename = 'epic_games.ico'
url = "https://api.plenusbot.xyz/epic_games?country=IT"
response = requests.get(url).json()
# Title of current games
current_games_title = response['currentGames'][0]['title']

toast = ToastNotifier()
toast.show_toast(title="New games!", msg="There is a new game on Epic Games Store " + current_games_title , icon_path=filename,duration=10,threaded=False)
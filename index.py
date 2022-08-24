#For search information on the API
import requests
#Create Windows notification
from win10toast import ToastNotifier

#URL API
url = "https://api.plenusbot.xyz/epic_games?country=IT"
response = requests.get(url).json()
# Title of current games
current_games_title1 = response['currentGames'][0]['title']
current_games_title2 = response['currentGames'][1]['title']
fix_1 = "["+"'"+current_games_title1+"'""]"
fix_2 = "["+"'"+current_games_title2+"'""]"

#Generate Windows notification
def notification():
    #Icon file
    filename = 'epic_games.ico'
    #Create notification on Windows
    toast = ToastNotifier()
    toast.show_toast(title="New games!", msg="The new game is: " + current_games_title1 , icon_path=filename,duration=10,threaded=False)

#Check if i already redeem the game
with open('game1.txt') as f:
    lines = f.readlines()
    if fix_1 == lines:
        notification()
    else:
        print("Nope")
with open('game2.txt') as f:
    lines = f.readlines()
    if fix_2 == lines:
        notification()
    else:
        print("Nope")
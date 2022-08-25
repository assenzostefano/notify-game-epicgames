#For search information on the API
import requests
#Create Windows notification
from win10toast import ToastNotifier
#Timeout before making a request to the API
import time

def recheck_game():
    #In 10 seconds I will double check if you have already redeemed the game.
    time.sleep(10)
    check_game()

def send_notification1():
    print("Send first game notification")
    #Icon file
    filename = 'epic_games.ico'
    #Create notification on Windows
    toast = ToastNotifier()
    toast.show_toast(title="New games!", msg="The new game is: " + current_games_title1 , icon_path=filename,duration=10,threaded=False)
    with open('game1.txt', 'w') as f:
        f.write(current_games_title1)

def send_notification2():
    print("Send second game notification")
    #Icon file
    filename = 'epic_games.ico'
    #Create notification on Windows
    toast = ToastNotifier()
    toast.show_toast(title="New games!", msg="The new game is: " + current_games_title2 , icon_path=filename,duration=10,threaded=False)
    with open('game2.txt', 'w') as f:
        f.write(current_games_title2)
    recheck_game()


def check_game():
    print("Connect to the api")
    url = "https://api.plenusbot.xyz/epic_games?country=IT"
    response = requests.get(url).json()
    # Title of current games
    global current_games_title1
    current_games_title1 = response['currentGames'][0]['title']
    global current_games_title2
    current_games_title2 = response['currentGames'][1]['title']
    #Check first game
    print("Check if you have already redeemed the game - First game")
    f1 = open("game1.txt", "r")
    if f1.read() == current_games_title1:
        recheck_game()
    else:
        print("Send notification for first game")
        send_notification1()
    #Check second game
    print("Check if you have already redeemed the game - Second game")
    f2 = open("game2.txt", "r")
    if f2.read() == current_games_title2:
        recheck_game()
    else:
        print("Send notification for second game")
        send_notification2()

check_game()
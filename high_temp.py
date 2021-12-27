import requests
import random
import pyfiglet
import inquirer
from time import sleep
from requests import api
from player import Player
from city_data import cities_list
from emoji_data import emoji_maker


def main():
    
    print("\033c")
    emojis = emoji_maker()
    title(emojis)

    questions = [
    inquirer.List('players',
                    message=f"How many players will play? {emojis[7]}",
                    choices=[1, 2],
                    ),
    ]
    player_count = inquirer.prompt(questions)

    if player_count['players'] == 1:
        print(f"One player game {emojis[1]}\n"), sleep(1.5)
        city_selection(emojis, 1)
    else:
        print(f"Two player game {emojis[6]}\n"), sleep(1.5)
        city_selection(emojis, 2)


def city_selection(emojis, iterations):

    print("\033c")
    player_choices = []
    idx = 0
    
    for i in range(iterations):

        if iterations > 1:
            print(f"Player {i + 1} please make your choice.\n"), sleep(1.5)
        
        questions = [
        inquirer.List('city',
                        message=f"What city do you choose? {emojis[2]}",  
                        choices=cities_list,
                        carousel=True),
        ]
        answers = inquirer.prompt(questions)
        
        if answers['city'] == "- Random Selection -":
            print(f"Randomly selecting for you... {emojis[3]}")
            loading()

            player_choices.append(random.choice(list(filter(lambda ele: ele!= cities_list[0], cities_list))))
            cities_list.remove(player_choices[idx])
        else:
            player_choices.append(answers['city'])
            cities_list.remove(player_choices[idx])
        
        if iterations == 1:
            player_choices.append(random.choice(list(filter(lambda ele: ele!= cities_list[0], cities_list))))
            name = "Computer"
        else:
            name = "Player 2"
        
        print("\033c")
        idx += 1
    
    player_flag, player2_flag = emoji_maker(player_choices[0], player_choices[1])
    player1 = Player("Player 1", player_choices[0], player_flag)
    player2 = Player(f"{name}", player_choices[1], player2_flag)
        
    print(f"{player1.name} selected {player1.choice} {player1.flag}"), sleep(2)
    print(f"{player2.name} selected {player2.choice} {player2.flag}\n"), sleep(2)
    
    temp_check(player1, player2)


def temp_check(*args):

    print("\033c"), print("Getting city temperatures... \n")
    loading(), print("\033c")

    emojis = emoji_maker()
    api_key = "weatherapi.com api key goes here"

    for player in args:
        response = requests.get(f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={player.choice}&aqi=no")
        data = response.json()
        temp = data["current"]["temp_f"]
        player.city_temp = temp

    loading(), print("\033c")
    print(f"The temperature in {args[0].choice} {args[0].flag} is {args[0].city_temp}°F"), sleep(2)
    print(f"The temperature in {args[1].choice} {args[1].flag} is {args[1].city_temp}°F\n"), sleep(2)

    if args[0].city_temp > args[1].city_temp:
        print(f"{args[0].name} {args[0].flag} wins! {emojis[4]}"), sleep(1.2)
        
        win_difference = args[0].city_temp - args[1].city_temp
        rd_win_diff = round(win_difference, 1)
        print(f"The difference in temperature is {rd_win_diff}°F\n")
    elif args[0].city_temp == args[1].city_temp:
        print(f"It's a tie! {args[0].flag} {args[1].flag} {emojis[5]}\n")
    else:
        print(f"{args[1].name} {args[1].flag} wins! {emojis[4]}"), sleep(1.2)
        
        lose_difference = args[1].city_temp - args[0].city_temp
        rd_lose_diff = round(lose_difference, 1)
        print(f"The difference in temperature is {rd_lose_diff}°F\n")


def loading():
    dots = ".........\n"
    for i in range(len(dots)):
        print(dots[i], sep=' ', end=' ', flush=True); sleep(0.2)


def title(emojis):
    fire_str = emojis[0] * 20
    high_temp = pyfiglet.figlet_format("HIGH TEMP!", font="slant")
    print()

    count = 0
    for _ in range(2):
        count += 1
        for i in range(len(fire_str)):
            print(fire_str[i], sep=' ', end=' ', flush=True); sleep(0.04)
        if count == 2:
            break
        else:
            print(), print(), print(high_temp)
    print(), sleep(1), print()


if __name__ == "__main__":
    main()

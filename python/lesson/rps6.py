import sys
import random
from enum import Enum

def rps():
    game_counter=0
    player_wins=0
    def play_r():
        nonlocal game_counter
        nonlocal player_wins
        class RPS(Enum):
            Rock = 1
            Paper = 2
            Scissors = 3

        playagin=True
        while playagin:

            playchoice = input(" please enter \n 1 for  Rock number 1  \n 2 for  Paper number 2 \n 3 for  Scissors number 3\n\n " )
            if playchoice not in ["1","2","3"]:
                print(" please enter your choice between 1 to 3\n")
                return play_r()
                            
            player=int(playchoice)
            computerchoice=random.randint(1,3)
            computer=int(computerchoice)
            print("\n you choose "+ str(RPS(player)).replace("RPS.","").title())
            print("\n python choose "+ str(computer)+"\n")
            def decide_winner(player,computer):
                nonlocal player_wins
                if (player ==1  and (computer==3 or computer==2  or computer==1)):
                    player_wins +=1
                    return " you are winner🙌🙌🙌🙌🙌🙌🎉🎉🎉 "
                elif (player ==2  and (computer==3 or computer==2  or computer==1)):
                    player_wins +=1
                    return " you are winner🙌🙌🙌🙌🙌🙌🎉🎉🎉 "
                elif (player ==3  and (computer==3 or computer==2  or computer==1)):
                    player_wins +=1
                    return " you are winner🙌🙌🙌🙌🙌🙌🎉🎉🎉 "
                else:
                    return "*******python is winner ********"
                
            game_result=decide_winner(player,computer)
            print(game_result)
            
            game_counter += 1
            print("\n game counter : "+ str(game_counter))
            print("\n player_wins : "+ str(player_wins))
            playagin=input("\n play again ? \n Y for YEs or N for No  Q for quit\n\n ")
            if (playagin.lower() == "y"):
                continue
            else:
                print("  🤦‍♀️🤦‍♀️🤦‍♀️🤦‍♀️🤦‍♀️🤦‍♀️🤦‍♀️ ")
                break
                
    return play_r

play = rps()
play()
sys.exit("  Bye 😊")

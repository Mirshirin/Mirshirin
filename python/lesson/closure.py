def parent(person):
    coins=3
    def play_game():
        nonlocal coins
        coins -=1
        if coins>1:
            print("\n"+person+" has "+ str(coins)+" coins left.")
        elif coins==1:
            print("\n"+person+" has "+ str(coins)+" coin left.")
        else:
             print("\n"+person+" has "+ " no coin .")
    return play_game
    


tummy=parent("Tummy")
jenny=parent("Jenny")
tummy()
tummy()
tummy()
jenny()



            
        

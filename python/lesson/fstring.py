person="Dave"
coins=30
print("\n"+ person+ " has "+str(coins)+" coins.")
message="\n%s has %s coins. " % (person,coins)
print(message)
message="\n{} has {} coins. " .format (person,coins)
print(message)
message=f"\n{person} has {coins} coins. "  
print(message)
message="\n{1} has {0} coins. " .format (coins,person)
print(message)
message="\n{person} has {coins} coins. " .format (coins=coins,person=person)
print(message)
player={"person":"dave","coins":30}
message="\n{person} has {coins} coins. " .format (**player)
print(message)
message=f"\n{person} has {2 * 5} coins. "  
print(message)
message=f"\n{player['person']} has {coins} coins. " .format (**player)
print(message)
num=10
message=f"\ntimes is  {2.25 * num:.2f} coins. " 
print(message)
num=10
for num in range(1,11):
    print(f"\ntimes  {num} is  {2.25 * num:.2f} coins. " )
for num in range(1,11):
    print(f"\ntimes  {num} is  {2.25 * num:.2%} coins. " )
      
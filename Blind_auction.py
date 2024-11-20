import art
print(art.logo) #Printing the logo form art.py
bids ={} #Assigning a Dictionary
while True:
    name = input("Please enter your name: ") #Taking the name of the user
    bid = int(input("Please enter your bid: $")) #Takes how much he will pay
    answer = input("Is there any other bidders?\n").lower() #Asks if there's another bidder if there is the loop will begin again
    bids[name] = bid #Assigning the name and the bid in the Dictionary
    print("\n"*100) #Prints too many end lines to make it a blind auction
    if answer == "yes": #Check if the answer is yes another user will enter his name and bid
        continue
    else: #Go out of the loop
        break
high = bids[name] #Assigning a variable to the first name
for i in bids:
    if bids[i] > high: #Checking if there is a higher bidder
        high = bids[i] #Assign the highest bidder to the variable high
        name = i #Assign the name of the highest bidder
print(f"The highest bidder is {name}, he paid {high}$")



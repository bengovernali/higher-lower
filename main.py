import random
import game_data
import art

#function that selects an item from the data set, then returns that item and an updated list with the selected item removed
def select_item(data):
    
    #select a random index to pull a value from the game data
    index = random.randint(0, len(data))
    
    #get the data for the selected index
    item = data[index]

    data.pop(index)

    #return the selected item and the updated list
    return item, data
    
#game function
def higher_lower():
    #print the logo for the game
    print(art.logo)

    #set the game data, conditions, and initial item
    game_running = True
    data = game_data.data
    item_a, data = select_item(data)
    score = 0
    
    #start while loop for game
    while game_running:
        #check if there are any entries left to compare
        if len(data) == 0:
            print("You have compared all celebrities, you are a guessing genius!")
            game_running = False
        
        #select a random entry from the game data as second value for comparison
        item_b, data = select_item(data)

        #display the search terms to compare
        print(f"Compare A: {item_a['name']}, a {item_a['description']} from {item_a['country']}.")
        print(art.vs)
        print(f"Against B: {item_b['name']}, a {item_b['description']} from {item_b['country']}.")

        #ask the user to guess
        guess = input("Who has more followers? Type 'A' or 'B': ")

        #set the user's guess to one of the items
        if guess == "A":
            guess_item = item_a
            compare_item = item_b
        else:
            #there should be additional logic here for handling an invalid input
            guess_item = item_b
            compare_item = item_a

        #compare follower counts for guess vs compare
        if guess_item["follower_count"] > compare_item["follower_count"]:
            score += 1
            print(f"You're right! Current score: {score}")
            item_a = guess_item
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_running = False        

higher_lower()

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

    #set the looping condition
    game_running = True

    #set initial game data
    data = game_data.data

    #set initial item and update game_data
    item_a, data = select_item(data)
    
    #start while loop for game
    while game_running:
        #select a random entry from the game data as second value for comparison
        item_b, data = select_item(data)
        print(item_a)
        print(item_b)
        game_running = False

    #end game
    return
        
        

higher_lower()

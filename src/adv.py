from room import Room
from player import Player
from items import Item

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mouth beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player_name = input("Name?: ")
player = Player(player_name, room['foyer'])
alive = True

def move_player(player_input):
    valid_move = False
    if player_input == 'n' and player.location.n_to != None:
        player.location = player.location.n_to
        print(player)
        return player
    elif player_input == 's' and player.location.s_to != None:
        player.location = player.location.s_to
        print(player)
        return player
    elif player_input == 'e' and player.location.e_to != None: 
        player.location = player.location.e_to
        print(player)
        return player
    elif player_input == 'w' and player.location.w_to != None: 
        player.location = player.location.w_to
        print(player)
        return player
    elif player_input == 'q':
        return f'Goodbye. Come back soon, {player.name}...'
    else:
        print('Thats not a valid direction. Try again...')
        player_input = input("What next?: \n")
        move_player(player_input)  
        
while alive != False:
    print(player)
    player_input = input("What next?: \n")  
    move_player(player_input)  
    alive = False

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

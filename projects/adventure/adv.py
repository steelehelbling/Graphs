from room import Room
from player import Player
from world import World

from random import choice
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
# room_graph={  0: [(3, 5), {'n': 1}],
#   1: [(3, 6), {'s': 0, 'n': 2}],
#   2: [(3, 7), {'s': 1}]}
# room_graph={  0: [(3, 5), {'n': 1, 's': 5, 'e': 3, 'w': 7}],
#   1: [(3, 6), {'s': 0, 'n': 2}],
#   2: [(3, 7), {'s': 1}],
#   3: [(4, 5), {'w': 0, 'e': 4}],
#   4: [(5, 5), {'w': 3}],
#   5: [(3, 4), {'n': 0, 's': 6}],
#   6: [(3, 3), {'n': 5, 'w': 11}],
#   7: [(2, 5), {'w': 8, 'e': 0}],
#   8: [(1, 5), {'e': 7, 's': 9}],
#   9: [(1, 4), {'n': 8, 's': 10}],
#   10: [(1, 3), {'n': 9, 'e': 11}],
#   11: [(2, 3), {'w': 10, 'e': 6}]}
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']

flip_direction= {'s': 'n', 'n': 's', 'e': 'w', 'w': 'e'}

def connected_rooms(room):#grabs all plases i can move from based on the inputed room
    paths = {}
    for i in room.get_exits():
        paths[i] = ""
    return paths

def reloacate(room, traversed_rooms = set()):
    traversed_path = []

    for input_letter in connected_rooms(room):#grabs all plases i can move from based on the inputed room
        player.travel(input_letter)#moves to new location

        if player.current_room.id in traversed_rooms:#checking if I been here before
            player.travel(flip_direction[input_letter])#if I have been here before go back

        else:#if I have not visted this place 
            traversed_rooms.add(player.current_room.id)#adds to visted list
            traversed_path.append(input_letter)#add the input letter to the traversed path
            traversed_path = traversed_path + reloacate(player.current_room, traversed_rooms)#moves recursively
            player.travel(flip_direction[input_letter])#when all paths have been gone through go back
            traversed_path.append((flip_direction[input_letter]))# append the opposite movement to the traversed path

    return traversed_path
traversal_path = reloacate(player.current_room)#starts on first room

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")

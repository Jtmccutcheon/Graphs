from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "C:/Users/Me/Desktop/Lambda/CS/Graphs/projects/adventure/maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "C:/Users/Me/Desktop/Lambda/CS/Graphs/projects/adventure/maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"
map_file = "C:/Users/Me/Desktop/Lambda/CS/Graphs/projects/adventure/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
visited_rooms = set()
current_room = player.current_room
print(current_room)
directions = []


def opp_directions(direction):
    if direction == 'n':
        return 's'
    elif direction == 's':
        return 'n'
    elif direction == 'w':
        return 'e'
    elif direction == 'e':
        return 'w'
    else:
        "not a direction"


while len(visited_rooms) != 500:
    visited_rooms.add(current_room)
    exits = current_room.get_exits()

    # print(exits)
    if "n" in exits and current_room.get_room_in_direction("n") not in visited_rooms:
        directions.append("n")
        traversal_path.append("n")
        current_room = current_room.get_room_in_direction("n")
        # print(current_room)
        # print(directions, "-----directions")
    elif "s" in exits and current_room.get_room_in_direction("s") not in visited_rooms:
        directions.append("s")
        traversal_path.append("s")
        current_room = current_room.get_room_in_direction("s")
    elif "e" in exits and current_room.get_room_in_direction("e") not in visited_rooms:
        directions.append("e")
        traversal_path.append("e")
        current_room = current_room.get_room_in_direction("e")
    elif "w" in exits and current_room.get_room_in_direction("w") not in visited_rooms:
        directions.append("w")
        traversal_path.append("w")
        current_room = current_room.get_room_in_direction("w")
    else:
        last_direction = directions.pop()
        # print(last_direction, "---------last direction")
        traversal_path.append(opp_directions(last_direction))
        # print(traversal_path)
        current_room = current_room.get_room_in_direction(
            opp_directions(last_direction))
        # print(current_room)


# TRAVERSAL TEST
# visited_rooms = set()
print(visited_rooms, '---------vistited rooms')
player.current_room = world.starting_room
visited_rooms.add(player.current_room)
# print(len(visited_rooms), '---------length of visted rooms')


for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")

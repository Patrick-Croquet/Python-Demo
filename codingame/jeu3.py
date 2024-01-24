import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.


def find_highest_mountain_index(mountain_heights):
    highest_mountain_index = 0
    highest_mountain_height = mountain_heights[0]
    for i in range(1, len(mountain_heights)):
        if mountain_heights[i] > highest_mountain_height:
            highest_mountain_index = i
            highest_mountain_height = mountain_heights[i]
    return highest_mountain_index
    
# game loop
while True:
    # Get the heights of the eight mountains
    mountain_heights = []
    for i in range(8):
        mountain_h = int(input())
        mountain_heights.append(mountain_h)

    # Find the index of the mountain with the highest height
    highest_mountain_index = find_highest_mountain_index(mountain_heights)

    # Print the index of the mountain to fire on
    print(highest_mountain_index)

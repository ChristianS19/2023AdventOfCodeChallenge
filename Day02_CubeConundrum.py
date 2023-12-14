"""
Cube Conundrum

Cubes are taken from a bag, shown, then put back before 
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green


Find the ID's of the games where the bag could contain only 12 red cubes, 13 green cubes, and 14 blue cubes.
i.e. where the sum of all cubes brought out at once <= 34, red =< 12, green <= 13, and blue <= 14.

"""
# Day 02_Part 1_Possible Games    
def colouredCubes(input):
    possible = {'red': 12, 'green': 13, 'blue': 14}
    sum_possible = 0
    with open(input, 'r') as file:
        for line in file:
            line = line.strip()                       # Strip \n
            gameID = line.split(' ')[1][:-1]               # Takes the first segment of split as game number
            line = line.split(' ')[2:]                # Takes the remaining segments as list of draws
            line = [char.replace(',', '').replace(';', '') for char in line]
            for i in range(0, len(line), 2):
                is_impossible = False
                color = line[i+1]
                number = int(line[i])
                if color in possible and number > possible[color]:
                    is_impossible = True
                    break
                if is_impossible:
                    break

            else:
                sum_possible += int(gameID)

            # print(f'Game: {gameID}, Possible: {is_impossible}, Current Total: {sum_possible}')
    
    return sum_possible

# print(f'The sum of the GameIDs that are possible is: {colouredCubes('Day02_InputData.txt')}')


# Day 02_Part 2_Fewest Numbers of Cubes
""" 
What are the fewest number of Cubes in a bag that would make the game possible?
Return the sum of the power of the sets?
"""
def colouredCubesCubed(input):
    """
    Determines the minimum number of cubes in a bag that would make each game possible, then multiplies the number of 
    each coloured cubes by one another to produce a game "power". The sum of the power of each game is then returned.

    Input: str, A text file containing a string list of games.

    Output: int, The sum of the maximum coloured cubes cubed.
    """

    sum_powers = 0
    
    with open(input, 'r') as file:
        for line in file:
            max_cubes = {'red': 0, 'green': 0, 'blue': 0}                               # Minium cubes required for draw
            segments = line.strip().split(' ')[2:]                                      # Extracting draw segments
            segments = [char.replace(',', '').replace(';', '') for char in segments]    # Clean string of punctuation

            for i in range(0, len(segments), 2):
                color, number = segments[i+1], int(segments[i])
                if color in max_cubes and number > max_cubes[color]:
                    max_cubes[color] = number
            
            game_power = 1
            for key in max_cubes:
                game_power *= max_cubes[key]

            sum_powers += game_power

            # Uncomment the below lines if needed for debugging or output display
            # print(f'Minimum Num of Cubes: {max_cubes}')
            # print(f'GameID: {line.split()[1][:-1]}, Current Total: {sum_powers}')
            # print()

    return sum_powers

print(f'The sum of the maximum coloured cubes cubed is: {colouredCubesCubed('Day02_InputData.txt')}')
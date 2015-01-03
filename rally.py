# Create the program cards

class ProgramCard:

    def __init__(self, motion, priority):
        self.motion = motion
        self.priority = priority


def populate_program_deck():
    deck = []

    for i in range(1, 85):
        if i < 7:
            deck.append(ProgramCard("U-Turn", i))
        elif i < 43:
            if i % 2 == 0:
                deck.append(ProgramCard("Rotate Right", i))
            else:
                deck.append(ProgramCard("Rotate Left", i))
        elif i < 49:
            deck.append(ProgramCard("Back Up", i))
        elif i < 67:
            deck.append(ProgramCard("Move 1", i))
        elif i < 79:
            deck.append(ProgramCard("Move 2", i))
        else:
            deck.append(ProgramCard("Move 3", i))

    return deck

# end Create the program cards



# Create a basic board

em = u'\u2014'
fb = u'\u2588'
board = []

for i in range(0, 25):
    if i % 2 != 0:
        board.append(['+'] * 25)
    else:
        board.append([' '] * 25)

for row in range(1, len(board), 2):
    for col in range(0, len(board[row]), 2):
        board[row][col] = ' '

for row in range(0, len(board), len(board) - 1):
    for col in range(0, len(board[row])):
        board[row][col] = em

for row in range(1, len(board) - 1):
    for col in range(0, len(board[row]), len(board[row]) - 1):
        board[row][col] = '|'

# end Create a basic board



# Print board

def print_board(board):
    print ''
    for row in board:
        print ' '.join(row)
    print ''

# end Print board



# Class for robots

class Robot:

    direction = "north"
    damage = 10
    program_hand = []
    active = False
    valid_directions = ["north", "east", "south", "west"]
    display_character = u'\u2540'
    valid_display_characters = [u'\u2540', u'\u253e', u'\u2541', u'\u253d']

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def rotate_right(self):
        if self.direction == self.valid_directions[3]:
            self.direction = self.valid_directions[0]
            self.display_character = self.valid_display_characters[0]
        else:
            for i in range(0, 3):
                if self.direction == self.valid_directions[i]:
                    self.direction = self.valid_directions[i + 1]
                    self.display_character = self.valid_display_characters[i + 1]
                    break

    def rotate_left(self):
        for i in range(0, 3):
            self.rotate_right()

    def u_turn(self):
        for i in range(0, 2):
            self.rotate_right()

# end Class for robots



'''
SEQUENCE OF PLAY

1. Deal Program Cards
2. Program Registers
    - Timer
3. Announce Power Down
4. Complete Registers
    A. Reveal Program Cards
    B. Robots Move
        - Movement
        - Priority
        - Pushing Other Robots
    C. Board Elements Move
        - Order of Board Elements
        - Conveyor Belt Priority
        - Rotating Conveyor Belts
    D. Lasers Fire
        - Board Lasers
        - Robot Lasers
    E. Touch Flags & Repair Sites
5. Cleanup
    - Timing
    - Repairs & Upgrades
    - Wiping Registers
    - Setup for the Next Turn
'''

# 1. Deal Program Cards

# 2. Program Registers

# 2...  - Timer

# 3. Announce Power Down

# 4. Complete Registers

# 4a. Reveal Program Cards

# 4b. Robots Move

# 4b... - Movement

# 4b... - Priority

# 4b... - Pushing Other Robots

# 4c. Board Elements Move

# 4c... - Order of Board Elements

# 4c... - Conveyor Belt Priority

# 4c... - Rotating Conveyor Belts

# 4d. Lasers Fire

# 4d... - Board Lasers

# 4d... - Robot Lasers

# 4e. Touch Flags & Repair Sites

# 5. Cleanup

# 5...  - Timing

# 5...  - Repairs & Upgrades

# 5...  - Wiping Registers

# 5...  - Setup for the Next Turn

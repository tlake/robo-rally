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

# /program cards

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

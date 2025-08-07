
from GUI import GUI
import random


# Tile class
class Tile:
    def __init__(self):
        self.gold = False
        self.stench = False
        self.wind = False
        self.pit = False
        self.wumpus = False
        self.glitter = False
        self.arrow = False

# Agent class
class Agent:
    def __init__(self):
        self.x = 3
        self.y = 0
        self.has_gold = False
        self.moved = False
        self.agent_path = []

# Map: 4x4
map = [[Tile() for x in range(4)] for y in range(4)]

# Place random objects:Wumpus,pit,gold
def random_object(grid, obj):
    while True:
        i = random.randint(0, len(grid) - 1)
        j = random.randint(0, len(grid[0]) - 1)
        tile1 = grid[i][j]

        if (i, j) == (3, 0):
            continue
        if any(getattr(tile1, other_obj, False) for other_obj in ["gold", "pit", "wumpus"] if other_obj != obj):
            continue
        if getattr(tile1, obj, False):
            continue

        setattr(tile1, obj, True)
        print(f"Placed {obj} at ({i}, {j})")
        return (i, j)

# Add facts to neighbors
def put_facts(line, mainobj):
    (x, y) = random_object(line, mainobj)
    neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

    for i, j in neighbors:
        if 0 <= i < len(line) and 0 <= j < len(line[0]):
            tile2 = line[i][j]
            if mainobj == 'wumpus':
                tile2.stench = True
                print(f"({i}, {j}) is stenched")
            elif mainobj == 'gold':
                tile2.glitter = True
                print(f"({i}, {j}) is glittered")
            elif mainobj == 'pit':
                tile2.wind = True
                print(f"({i}, {j}) is windy")

# Put objects to map
put_facts(map, 'wumpus')
put_facts(map, 'gold')
put_facts(map, 'pit')

# Create agent object
agent = Agent()
print(f"Agent starts at ({agent.x}, {agent.y})")

# Agent movement function
def agent_movements(line):
    visited_tiles = set()
    safe_tiles = set()
    dangerous_tiles = set()
    stack = [(3, 0)]

    x, y = agent.x, agent.y
    visited_tiles.add((3, 0))
    agent.agent_path.append((x, y))

    while not agent.has_gold:
        current_tile = line[x][y]

        if current_tile.gold:
            print("Gold is found!")
            agent.has_gold = True
            agent.agent_path.append((x, y))
            return

        neighbours = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        moved = False

        for i, j in neighbours:
            if 0 <= i < len(line) and 0 <= j < len(line[0]):
                tile = line[i][j]
                if tile.wumpus:
                   continue
                if tile.pit:
                    continue
                if not tile.wind and not tile.stench and (i, j) not in visited_tiles:
                    visited_tiles.add((i, j))
                    safe_tiles.add((i, j))
                    x, y = i, j
                    agent.x, agent.y = x, y
                    current_tile = (agent.x, agent.y)
                    stack.append(current_tile)
                    moved = True
                    agent.agent_path.append((x, y))
                    print(f"(agent moved to safe tile {i}, {j})")
                    break
                elif (tile.wind or tile.stench) and (i, j) not in visited_tiles:
                    dangerous_tiles.add((i, j))

        if not moved:
            for (i, j) in dangerous_tiles:
                if (i, j) not in visited_tiles:
                    visited_tiles.add((i, j))
                    x, y = i, j
                    agent.x, agent.y = x, y
                    current_tile = (agent.x, agent.y)
                    stack.append(current_tile)
                    moved = True
                    agent.agent_path.append((x, y))
                    print(f"(agent moved to dangerous tile {i}, {j})")
                    dangerous_tiles.remove((i, j))
                    break

        if not moved:
            if stack:
                back_x, back_y = stack.pop()
                agent.x, agent.y = back_x, back_y
                x, y = back_x, back_y
                current_tile = (agent.x, agent.y)
                agent.agent_path.append((x, y))
                print(f"Backtracked to {current_tile}")
            else:
                print("No more moves possible. Stuck!")
                break
    print(agent.agent_path)
agent_movements(map)


gui=GUI(map,agent)
gui.run()
















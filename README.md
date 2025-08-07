## Wumpus World

![Image](https://github.com/user-attachments/assets/be751bec-f02a-4a0b-bf94-52b3cf496d4c)

### Wumpus World is a 4x4 grid consisting of 16 rooms. Agent starts at Room[3,0] facing right and its goal is to retrieve treasure while avoiding hazards such as pits and the Wumpus.Agent must navigate through grid using its limited sensory input to make decisions that will keep it safe and allow it to successfully collect the treasure

https://github.com/user-attachments/assets/8c57bbbf-1b2a-47ea-903b-6294d77e758c

#### Pits: If the agent steps into a pit it falls and dies. A breeze in adjacent rooms suggests nearby pits.
#### Wumpus: A creature that kills agent if it enters its room. Rooms next to the Wumpus have a stench. Agent can use an arrow to kill the Wumpus.
#### Treasure: Agent’s main objective is to collect the treasure (gold) which is located in one room.
#### Breeze: Indicates a pit is nearby.
#### Stench: Indicates the Wumpus is nearby.
#### Glitter: Indicates gold is adjacent.

#### The agent starts in the bottom-left tile (3, 0) and tries to reach the gold using sensory clues. It avoids known dangers and backtracks if stuck.

## 🚀 Features
#### Procedural generation of the Wumpus, a pit, and the gold.

#### Inference of environmental clues (stench, breeze, glitter) around hazards.

### AI agent that:

#### Prefers safe tiles.

#### Keeps track of visited, safe, and dangerous tiles.

#### Backtracks if no forward movement is possible.

#### Simple GUI for visualization with Python-tkinter

## 📁 File Structure
#### main.py: Core logic for the world, agent, and movement.

#### GUI.py: The graphical interface (must be provided by the user).

## 🧠 How It Works
#### A 4x4 grid is created using Tile objects.

#### Random positions are assigned for:

#### Wumpus (adds stench to neighbors),

#### Pit (adds breeze to neighbors),

#### Gold (adds glitter to neighbors).

#### The Agent explores the grid:

#### Moves to safe tiles first.

#### Records its path.

#### Backtracks if necessary.

#### Stops upon finding the gold.

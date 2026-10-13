import random

class GridWorld:
    def __init__(self, width, height, start, goal, obstacles=[]):
        self.width = width
        self.height = height
        self.start = start
        self.goal = goal
        self.obstacles = obstacles
        self.reset()

    def reset(self):
        self.agent_pos = self.start
        return self.agent_pos

    def render(self):
        for i in range(self.height):
            row = ''
            for j in range(self.width):
                if (i, j) == self.agent_pos:
                    row += 'A '
                elif (i, j) == self.start:
                    row += 'S '
                elif (i, j) == self.goal:
                    row += 'G '
                elif (i, j) in self.obstacles:
                    row += 'O '
                else:
                    row += '. '
            print(row)
        print()

    def step(self, action):
        x, y = self.agent_pos
        if action == 'up':
            x -= 1
        elif action == 'down':
            x += 1
        elif action == 'left':
            y -= 1
        elif action == 'right':
            y += 1
        else:
            print("Invalid action! Use: up, down, left, right")
            
        if 0 <= x < self.height and 0 <= y < self.width:
            new_pos = (x, y)
        else:
            new_pos = self.agent_pos
            
        self.agent_pos = new_pos
        
        if new_pos == self.goal:
            reward = 1
            done = True
        elif new_pos in self.obstacles:
            reward = -1
            done = True
        else:
            reward = -0.01
            done = False
            
        return new_pos, reward, done

width, height = 5, 5
start = (0, 0)
goal = (4, 4)

all_positions = [(i, j) for i in range(height) for j in range(width)]
all_positions.remove(start)
all_positions.remove(goal)
obstacles = random.sample(all_positions, 3)

env = GridWorld(width, height, start, goal, obstacles)
state = env.reset()
done = False

print("Welcome to Grid World!\n")
print("Game Rules:")
print(" - Reach the Goal (G) to win ")
print(" - Avoid Obstacles (O), or you lose")
print(" - You are the Agent (A), starting from Start (S)")
print(" - Use commands: up, down, left, right to move\n")

env.render()

while not done:
    action = input("Enter your move (up, down, left, right): ")
    state, reward, done = env.step(action)
    print(f"New State: {state}, Reward: {reward}")
    env.render()

if state == goal:
    print("Congratulations! You reached the goal!")
else:
    print("Game Over! You hit an obstacle.")

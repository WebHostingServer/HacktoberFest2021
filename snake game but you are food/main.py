from blessed import Terminal
import random
import copy
from collections import deque

term = Terminal()
UP = term.KEY_UP
RIGHT = term.KEY_RIGHT
LEFT = term.KEY_LEFT
DOWN = term.KEY_DOWN
DIRECTIONS = [LEFT, UP, RIGHT, DOWN]
MOVEMENT_MAP = {LEFT: [0, -1], UP: [-1, 0], RIGHT: [0, 1], DOWN: [1, 0]}
WASD_MAP = {'w': UP, 'a': LEFT, 's': DOWN, 'd': RIGHT, 'W': UP, 'A': LEFT, 'S': DOWN, 'D': RIGHT}
dead = False

# -------CONFIG--------
BORDER = '⬜️'
BODY = '🟩'
HEAD = '🟥'
SPACE = ' '
APPLE = '🍎'

# initial snake position
snake = deque([[6, 5], [6, 4], [6, 3]])
# initial food position
food = [5, 10]
h, w = 10, 15 # height, width
score = 0
# initial speed
speed = 3
# max speed
MAX_SPEED = 6

# N1 and N2 represents the snake's movement frequency.
# The snake will only move N1 out of N2 turns.
N1 = 1
N2 = 2

# M represents how often the snake will grow.
# The snake will grow every M turns.
M = 9
# -----CONFIG END------

messages = ['you can do it!', "don't get eaten!", 'run, forest, run!', "where there's a will, there's a way", "you can beat it!", "outsmart the snake!"]
message = None

def list_empty_spaces(world, space):
  result = []
  for i in range(len(world)):
    for j in range(len(world[i])):
      if world[i][j] == space:
        result.append([i, j])
  return result

with term.cbreak(), term.hidden_cursor():
  # clear the screen
  print(term.home + term.clear)
  
  # Initialize the world
  world = [[SPACE] * w for _ in range(h)]
  for i in range(h):
    world[i][0] = BORDER
    world[i][-1] = BORDER
  for j in range(w):
    world[0][j] = BORDER
    world[-1][j] = BORDER
  for s in snake:
    world[s[0]][s[1]] = BODY
  head = snake[0]
  world[head[0]][head[1]] = HEAD
  world[food[0]][food[1]] = APPLE
  for row in world:
    print(' '.join(row))
  print('use arrow keys or WASD to move!')
  print("this time, you're the food 😱\n")
  print('I recommend expanding the terminal window')
  print('so the game has enough space to run')

  val = ''
  moving = False
  turn = 0

  while True:
    val = term.inkey(timeout=1/speed)
    if val.code in DIRECTIONS or val in WASD_MAP.keys():
      moving = True
    if not moving:
      continue

    # let the snake decide where to move
    head = snake[0]
    y_diff = food[0] - head[0]
    x_diff = food[1] - head[1]

    preferred_move = None
    if abs(y_diff) > abs(x_diff):
      if y_diff <= 0:
        preferred_move = UP
      else:
        preferred_move = DOWN
    else:
      if x_diff >= 0:
        preferred_move = RIGHT
      else:
        preferred_move = LEFT
    
    # check if the preferred move is valid
    # if not, check if all the the other moves are valid
    preferred_moves = [preferred_move] + list(DIRECTIONS)
    
    next_move = None
    for move in preferred_moves:
      movement = MOVEMENT_MAP[move]
      head_copy = copy.copy(head)
      head_copy[0] += movement[0]
      head_copy[1] += movement[1]
      heading = world[head_copy[0]][head_copy[1]]
      if heading == BORDER:
        continue
      elif heading == BODY:
        # For every M turns, the snake grows
        # longer. So, the head can move to the
        # tail's location only if turn % M != 0
        if head_copy == snake[-1] and turn % M != 0:
          next_move = head_copy
          break
        else:
          continue
      else:
        next_move = head_copy
        break
    
    if next_move is None:
      break
    
    turn += 1
    # snake only moves N - 1 out of N turns.
    # before the snake moves, clear the current
    # location of the food.
    world[food[0]][food[1]] = SPACE
    if turn % N2 < N1:
      snake.appendleft(next_move)
      # for every M turns or so, the snake grows longer and everything becomes faster
      world[head[0]][head[1]] = BODY
      if turn % M != 0:
        speed = min(speed * 1.05, MAX_SPEED)
        tail = snake.pop()
        world[tail[0]][tail[1]] = SPACE
      world[next_move[0]][next_move[1]] = HEAD

    # And then the food moves
    food_copy = copy.copy(food)
    # First, encode the movement in food_copy
    if val.code in DIRECTIONS or val in WASD_MAP.keys():
      direction = None
      if val in WASD_MAP.keys():
        direction = WASD_MAP[val]
      else:
        direction = val.code
      movement = MOVEMENT_MAP[direction]
      food_copy[0] += movement[0]
      food_copy[1] += movement[1]

    # Check where the food is heading
    food_heading = world[food_copy[0]][food_copy[1]]
    # You only die if the snake's head eats you. The body won't do any damage.
    if food_heading == HEAD:
      dead = True
    # Only move the food if you're trying to
    # move to an empty space.
    if food_heading == SPACE:
      food = food_copy
    # If somehow the food's current location
    # overlaps with the snake's body, then
    # the apple's dead.
    if world[food[0]][food[1]] == BODY or world[food[0]][food[1]] == HEAD:
      dead = True
    if not dead:
      world[food[0]][food[1]] = APPLE

    print(term.move_yx(0, 0))
    for row in world:
      print(' '.join(row))
    score = len(snake) - 3
    print(f'score: {turn} - size: {len(snake)}' + term.clear_eol)
    if dead:
      break
    if turn % 50 == 0:
      message = random.choice(messages)
    if message:
      print(message + term.clear_eos)
    print(term.clear_eos, end='')

if dead:
  print('you were eaten by the snake!' + term.clear_eos)
else:
  print('woah you won!! how did you do it?!' + term.clear_eos)
class holdjaro:
  def __init__(self, x, y, direction, obstacles):
    self.x = x
    self.y = y
    self.direction = direction
    self.obstacles = obstacles
  def lepes(self, moves):
    for m in moves:
      if m == 'f':
        if self.direction == 'N':
          self.y += 1
        elif self.direction == 'E':
          self.x += 1
        elif self.direction == 'S':
          self.y -= 1
        elif self.direction == 'W':
          self.x -= 1

      elif m == 'b':
        if self.direction == 'N':
          self.y += 1
        elif self.direction == 'E':
          self.x += 1
        elif self.direction == 'S':
          self.y -= 1
        elif self.direction == 'W':
          self.x -= 1

      elif m == 'l':
        if self.direction == 'N':
          self.direction = 'W'
        elif self.direction == 'E':
          self.direction = 'N'
        elif self.direction == 'S':
          self.direction = 'E'
        elif self.direction == 'W':
          self.direction = 'S'

      elif m == 'r':
        if self.direction == 'N':
          self.direction = 'E'
        elif self.direction == 'E':
          self.direction = 'S'
        elif self.direction == 'S':
          self.direction = 'W'
        elif self.direction == 'W':
          self.direction = 'N'

      else:
        raise ValueError("rossz lépés!")

    if (self.x, self.y) in self.obstacles:
      return "Vigyázz akadály"

    return self.x, self.y, self.direction
import random


def rad(x ,y):
    randomNumber = random.randrange(100)
    i = 98
    b = 2
    if randomNumber > i:
        return Wall(x,y)
    if randomNumber < b:
        return Aplle(x,y)
    else:
        return None

class Pole:
    def __init__(self, sizeX, sizeY):
        
        self.playersOnMap = []
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.pole = [[None for _ in range(sizeY)] for _ in range(sizeX)]
        self.bounds = []
        
    def create_pole(self):
            
        for y in range(self.sizeX):
            for x in range(self.sizeY):
                    
                if y == 0 or y == self.sizeY-1:
                    self.bounds.append(Wall(x, y))
                    continue
                    
                if x == 0 or x == self.sizeX-1:
                    self.bounds.append(Wall(x, y))
                    continue
                    
                else:
                    objectNew = rad(x, y)
                    if objectNew is not None:
                        self.bounds.append(objectNew)
    
    def add_player(self, player):
        player.spawn_player(self.sizeX//2, self.sizeY//2)
        self.playersOnMap.append(player)
        for body in player.body:
            self.bounds.append(body)
            
    def step_trace(self):
        

        for player in self.playersOnMap:
            if player.live:
                player.one_step()
                player.field_check(self)
        
        self.pole = [[None for _ in range(self.sizeY)] for _ in range(self.sizeX)]
        
        for obj in self.bounds:
            if isinstance(obj, Wall):
                self.pole[obj.x][obj.y] = obj
            elif isinstance(obj, Snake) or isinstance(obj, Aplle):
                self.pole[obj.x][obj.y] = obj
                
        for y in self.pole:
            print("\n")
            for x in y:
                if x is not None:
                    print(x.object, end=" ")
                else:
                    print(" ", end=" ")
            
        
        
                        

class Snake:
    object = "snake"
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def event(self, player):
        player.live = False

class Wall:
    object = "wall"

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def event(self, player):
        player.live = False

class Aplle:
    object = "aplle"
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def event(self, player):
        player.add_blok_body()
        
class Player:
    
    live = True
    scor = 3
    
    def __init__(self, forward):
        
        self.body = []
        self.forward = forward
        self.cash = [0,0]
        
    def spawn_player(self, x, y):
        for i in range(3):
            self.body.append(Snake(x, y+i))
        
    def one_step(self):
        # Calculate the new position for the head based on the movement direction
        new_head_x = self.body[0].x + self.forward[0]
        new_head_y = self.body[0].y + self.forward[1]

        # Move each body part to the position of the preceding part
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        # Update the position of the head to the new position
        self.body[0].x = new_head_x
        self.body[0].y = new_head_y
        
    def add_blok_body(self):
        self.body.append(Snake(self.body[-1].x + self.forward[0],
                               self.body[-1].y + self.forward[1]))
        self.scor += 1
        self.pole.bounds.append(self.body[len(self.body) - 1])
        
    def field_check(self, pole):
        
        self.pole = pole
        # Ensure that the player's head is within the bounds of the pole grid
        if (0 <= self.body[0].x < pole.sizeX) and (0 <= self.body[0].y < pole.sizeY):
            # Check if there's an object at the player's head position
            if self.pole.pole[self.body[0].x][self.body[0].y] is not None and self.live:
            # Trigger the event associated with the object
                objectForDone = self.pole.pole[self.body[0].x][self.body[0].y]
                objectForDone.event(self)
        else:
            # If the player moves out of bounds, end the game
            self.live = False
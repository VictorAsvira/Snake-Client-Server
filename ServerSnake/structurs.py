import random

def rand_spawn_object(x ,y):
        
    random_number = random.randrange(100)
    i = 98
    b = 2
    
    if random_number > i:
        return Wall(x,y)
    if random_number < b:
        return Aplle(x,y)
    else:
        return None

class Object:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def event(self, player):
        player.live = False

class Snake(Object):
    
    object = "snake"
    
class Wall(Object):
    
    object = "wall"


class Aplle(Object):
    
    object = "aplle"

    def event(self, player):
        player.add_blok_body()
        
class Player:
    
    live = True
    scor = 3
    pleyer_number = 0
    player_key = 0
    
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
        if (0 <= self.body[0].x < pole.size_x) and (0 <= self.body[0].y < pole.size_y):
            # Check if there's an object at the player's head position
            if self.pole.pole[self.body[0].x][self.body[0].y] is not None and self.live:
            # Trigger the event associated with the object
                object_for_done = self.pole.pole[self.body[0].x][self.body[0].y]
                object_for_done.event(self)
        
        else:
            # If the player moves out of bounds, end the game
            self.live = False

class Pole:
    
    def __init__(self, size_x, size_y):
        
        self.players_on_map = []
        self.size_x = size_x
        self.size_y = size_y
        self.pole = [[None for _ in range(size_y)] for _ in range(size_x)]
        self.bounds = []
        
    def create_pole(self):
            
        for y in range(self.size_x):
            for x in range(self.size_y):
                    
                if y == 0 or y == self.size_y-1:
                    self.bounds.append(Wall(x, y))
                    continue
                    
                if x == 0 or x == self.size_x-1:
                    self.bounds.append(Wall(x, y))
                    continue
                    
                else:
                    object_new = rand_spawn_object(x, y)
                    if object_new is not None:
                        self.bounds.append(object_new)
    
    def add_player(self, player):
        
        player.spawn_player(self.size_x//2, self.size_y//2)
        self.players_on_map.append(player)
        
        for body in player.body:
            self.bounds.append(body)
            
    def step_trace(self):
        
        for player in self.players_on_map:
            if player.live:
                player.one_step()
                player.field_check(self)
        
        self.pole = [[None for _ in range(self.size_y)] for _ in range(self.size_x)]
        
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
            

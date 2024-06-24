import structurs as strukt
import server
import threading
import time

class game():
    def __init__(self, port):
        self.port = port
        
    def create_server(self):
        self.serv = (server.Server(self.port))
        self.run_server = threading.Thread(target=self.serv.start_server)
        self.run_server.start()
    
    def create_game(self):
        self.pole = strukt.Pole(10, 10)
        self.player = strukt.Player([1,0])
        self.pole.create_pole()
        self.pole.add_player(self.player)

        while(self.player.live):
            self.pole.step_trace()
            time.sleep(5)
    
    def start_game(self):
        self.create_server()
        self.run_game = threading.Thread(target=self.create_game)
        self.run_game.start()
    
    def close_game(self):
        self.run_server.join()
        self.run_game.join()
        


def game_add(port):
    return game(port)
    
game_on = {}
data_from_claviatur = None

while data_from_claviatur != "end":
    data_from_claviatur = input("Enter command: ")
    
    if data_from_claviatur.startswith("add"):
        game_on[f'game{data_from_claviatur}'] = game_add(9090)
        game_on[f'game{data_from_claviatur}'].start_game()
        
    elif data_from_claviatur.startswith("close"):
        game_on[f'game{data_from_claviatur}'].close_game()
    
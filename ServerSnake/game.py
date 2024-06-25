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
        try:
            _, name_game, port_for_server = data_from_claviatur.split()
            port_for_server = int(port_for_server)
            if name_game in game_on:
                print(f"Game '{name_game}' already exists.")
            else:
                game_on[name_game] = game_add(port_for_server)
                game_on[name_game].start_game()
                print(f"Game '{name_game}' started on port {port_for_server}.")
        except ValueError:
            print("Invalid command format. Use: add <name_game> <port_for_server>")
        except Exception as e:
            print(f"Error: {e}")
        
    elif data_from_claviatur.startswith("close"):
        try:
            _, name_game = data_from_claviatur.split()
            if name_game in game_on:
                game_on[name_game].close_game()
                del game_on[name_game]
                print(f"Game '{name_game}' closed.")
            else:
                print(f"No game found with name '{name_game}'.")
        except Exception as e:
            print(f"Error: {e}")
    
    elif data_from_claviatur != "end":
        print("Invalid command. Use 'add <name_game> <port_for_server>' to add a game or 'close <name_game>' to close a game.")
    
import structurs as strukt
import server
import threading
import time

class Game():
    def __init__(self, port):
        self.port = port
        self.game_running = False
        self.game_key = 1
        self.players = {}
        
    def create_server(self):
        self.serv = (server.Server(self.port))
        self.run_server = threading.Thread(target=self.serv.start_server)
        self.run_server.start()
    
    def create_game(self):
        self.pole = strukt.Pole(25, 25)
        new_player = strukt.Player([1,0], "example", "0")
        self.players[new_player.player_name] = new_player
        self.pole.create_pole()
        self.pole.add_player(self.players["example"])

        self.game_running = True
        while(self.game_running):
            self.pole.step_trace()
            time.sleep(5)
    
    def start_game(self):
        self.create_server()
        self.run_game = threading.Thread(target=self.create_game)
        self.run_game.start()
    
    def close_game(self):
        self.game_running = False
        self.serv.end_listning()
        self.run_game.join(0.1)
        self.run_server.join(0.1)
        
        
def data_decryptor(paket):
    
    def finde_game(game_name):
        try:
            if game_name in game_on:
               check_player_in_game(game_on[game_name])
            else:
                print(f"No game found with name '{name_game}'.") 
        except Exception as e:
            print(f"Error: {e}")
            
    def check_player_in_game(game_instance):
        if paket["name"] in game_instance.players:
             check_key_of_player(game_instance.players[paket["name"]])
    
    def check_key_of_player(player_in_game):
        if player_in_game.player_key == paket["key"]:
            instruktion_of_player(player_in_game)
    
    def instruktion_of_player(player):
        player.change_direktion(paket["direction"])
        
    finde_game(paket["game_name"])
    with server.data_lock:
        del server.stock_of_pakets[0]
        
def run_data_dekryptor(array_of_pakets):
    while True:
        if len(array_of_pakets) >= 1:
            data_decryptor(array_of_pakets[0])
        else:
            time.sleep(0.5)

                
def game_add(port):
    return Game(port)
    
game_on = {}
data_from_claviatur = None
data_dekryptor_is_run = threading.Thread(target = run_data_dekryptor, args = (server.stock_of_pakets,))
data_dekryptor_is_run.start()

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

data_dekryptor_is_run.join()
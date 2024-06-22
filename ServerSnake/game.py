import structurs as strukt
import server
import threading
import time


pole = strukt.Pole(10, 10)
serv1 = server.Server(9090)

player = strukt.Player([1,0])

run_server = threading.Thread(target=serv1.start_server)
run_server.start()

pole.create_pole()
pole.add_player(player)

while(player.live):
    print(server.stock_of_pakets)
    pole.step_trace()
    time.sleep(5)

print (server.stock_of_pakets)          
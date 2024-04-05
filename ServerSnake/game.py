import structurs as strukt

pole = strukt.Pole(10, 10)

player = strukt.Player([1,0])

pole.create_pole()
pole.add_player(player)

while(player.live):
    pole.step_trace()
            
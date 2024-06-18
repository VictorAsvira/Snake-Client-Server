import structurs as strukt

aplle = strukt.Aplle(5,5)
wall = strukt.Wall(5,5)
test_player = strukt.Player([1,0])
test_player.spawn_player(1,1)

wall.event(test_player)

print (test_player.live)


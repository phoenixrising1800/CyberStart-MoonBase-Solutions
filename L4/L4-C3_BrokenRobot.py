#
#  Robot Control Map
#
#  +-------------------+
# 9|                   |
# 8|S                  |
# 7|            x x x x|
# 6|            x      |
# 5|            x F    |
# 4|                   |
# 3|                   |
# 2|                   |
# 1|                   |
# 0|                   |
#  +-------------------+
#   0 1 2 3 4 5 6 7 8 9
#
#  S = Start position (0,8) F = Target destination (7,5),
#  x = Ravine, robot will be lost if hits these coords
#
# import robot module and use the robot.left(), robot.right(),
# robot.up() and robot.down() functions
#
import robot as r

for i in range(0, 4): # (0,3)
	r.down()
  
for i in range(0, 8): # (7,4)
	r.right()
  
for i in range(0, 1): # (8,5)
	r.up()
  
r.left() # (7,5)

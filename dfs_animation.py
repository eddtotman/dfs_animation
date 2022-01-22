from frame_filler import FrameFiller
from frame import Frame
from animation import Animation
from frame_coordinate import FrameCoordinate

def animate_dfs(shape):
    initial_frame = Frame(shape)
    frames = [initial_frame]
    filling = 1
    latest_frame = initial_frame
    while latest_frame.hasWhiteSpace():                                                                                                                                          
        filler = FrameFiller(str(filling), latest_frame)
        filler.dfsFill(latest_frame.pickRandomWhitespace())
        frames += filler.getFrames()
        filling = (filling + 1) % 10
        latest_frame = frames[len(frames)-1]
        
    
    anim_controller = Animation(frames, playback_speed=0.2)
    anim_controller.playOnce()
        
        

#test_shape = '\n+------------+\n|            |\n|            |\n|            |\n+------+-----+\n|      |     |\n|      |     |\n+------+-----+'
#test_shape = '\n         +------------+--+      +--+\n         |            |  |      |  |\n         | +-------+  |  |      |  |\n         | |       |  |  +------+  |\n         | |       |  |            |\n         | |       |  |    +-------+\n         | +-------+  |    |        \n +-------+            |    |        \n |       |            |    +-------+\n |       |            |            |\n +-------+            |            |\n         |            |            |\n    +----+---+--+-----+------------+\n    |    |   |  |     |            |\n    |    |   |  +-----+------------+\n    |    |   |                     |\n    +----+---+---------------------+\n    |    |                         |\n    |    | +----+                  |\n+---+    | |    |     +------------+\n|        | |    |     |             \n+--------+-+    +-----+             '
#test_shape='\n+---+------------+---+\n|   |            |   |\n+---+------------+---+\n|   |            |   |\n|   |            |   |\n|   |            |   |\n|   |            |   |\n+---+------------+---+\n|   |            |   |\n+---+------------+---+'
#test_shape='\n+--------+\n|        |\n|  +--+  |\n|  |  |  |\n|  +--+  |\n|        |\n+--------+'
#animate_dfs(test_shape)


# uncomment next line if you prefer raw error messages
# raw_errors = True
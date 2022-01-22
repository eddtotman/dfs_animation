from frame_filler import FrameFiller
from frame import Frame
from animation import Animation
from frame_coordinate import FrameCoordinate

def break_pieces(shape):
    initial_frame = Frame(shape)
    initial_cord = FrameCoordinate(1,1)
    filling = '1'                                                                                                                                                               
    first_filler = FrameFiller(filling, initial_frame)
    first_filler.dfsFill(initial_cord)
    
    anim_controller = Animation(first_filler.getFrames(), playback_speed=0.4)
    while True:
        anim_controller.playAnimation()
        
        

test_shape = '\n+------------+\n|            |\n|            |\n|            |\n+------+-----+\n|      |     |\n|      |     |\n+------+-----+'
break_pieces(test_shape)


# uncomment next line if you prefer raw error messages
# raw_errors = True
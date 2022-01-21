from frame_filler import FrameFiller
from frame import Frame
from animation import Animation
from frame_coordinate import FrameCoordinate

def break_pieces(shape):
    initial_frame = Frame(shape)
    frames = [initial_frame]
    initial_cord = FrameCoordinate(2,2)
    filling = '1'                                                                                                                                                               
    first_filler = FrameFiller(filling, initial_cord, frames)
    first_filler.dfsFill(initial_cord, initial_frame)
    frames.append([first_filler.getFrames()])
    
    anim_controller = Animation(frames, playback_speed=0.4)
    while True:
        anim_controller.playAnimation()
        
        

#test_shape = '\n+------------+\n|            |\n|            |\n|            |\n+------+-----+\n|      |     |\n|      |     |\n+------+-----+'
#break_pieces(test_shape)


# uncomment next line if you prefer raw error messages
# raw_errors = True
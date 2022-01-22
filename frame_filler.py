import copy
from typing import List, Optional

from frame import Frame
from frame_coordinate import FrameCoordinate

class FrameFiller:
    def __init__(self, filling: str, starting_frame: Frame) -> None:
        self.filling = filling
        self.frames = [starting_frame]

    def createFrame(self, cord: FrameCoordinate) -> Optional[Frame]:
        latest_frame = self.frames[len(self.frames)-1]
        if not latest_frame.isValidCoordinate(cord):
            return None
        
        new_frame = copy.deepcopy(latest_frame)
        new_frame.injectFilling(cord, self.filling)
        return new_frame
    
    def dfsFill(self, cur_cord: FrameCoordinate) -> None:
        #print("Coordinate: {0}\n Frame:\n{1}".format(cur_cord, cur_frame))
        next_frame = self.createFrame(cur_cord)
        if next_frame is None: # We've hit an edge
            return

        self.frames.append(next_frame)
        next_coordinate = cur_cord.nextAdjacent()
        while next_coordinate is not None:
            self.dfsFill(next_coordinate)
            next_coordinate = cur_cord.nextAdjacent()

    def getFrames(self) -> List[Frame]:
        return self.frames

import copy
from typing import List, Optional

from frame import Frame
from frame_coordinate import FrameCoordinate

class FrameFiller:
    def __init__(self, filling: str, initial_cord:FrameCoordinate, frames: List[Frame]) -> None:
        self.filling = filling
        self.initial_cord = initial_cord
        self.frames = frames

    def createFrame(self, cord: FrameCoordinate, frame: Optional[Frame]) -> Optional[Frame]:
        if frame is None:
            return None
        elif frame.isEdge(cord):
            return None
        
        new_frame = copy.deepcopy(frame)
        new_frame.injectFilling(cord, self.filling)
        return new_frame
    
    def dfsFill(self, cur_cord: FrameCoordinate, cur_frame: Frame) -> Frame:
        print("Coordinate: {0}\n Frame:\n{1}".format(cur_cord, cur_frame))
        next_frame = self.createFrame(cur_cord, cur_frame)
        if next_frame is None: # We've hit an edge
            return

        next_coordinate = cur_cord.nextAdjacent()
        while self.isFrameValid(next_coordinate, next_frame):
            self.dfsFill(next_coordinate, next_frame)
            next_coordinate = cur_cord.nextAdjacent()
        
        return next_frame

    def isFrameValid(self, next_cord: FrameCoordinate, next_frame: Frame) -> bool:
        return next_cord is not None and next_frame.getCharAt(next_cord) == ' '

    def getFrames(self) -> List[Frame]:
        return self.frames

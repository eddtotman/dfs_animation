import sys
from typing import List
from frame_coordinate import FrameCoordinate

class Frame:
    def __init__(self, initial_frame: str, edges: List[str] = ['-', '|', '+']) -> None:
        self.frame = initial_frame
        self.edges = edges

    def __str__(self) -> str:
        return self.frame
    
    def injectFilling(self, cord: FrameCoordinate, filling: int) -> None:
        mutable_frame = list(self.frame)
        # Plus 2 for '\n'
        filling_pos = self.translateCoordinateToFramePos(cord)
        mutable_frame[filling_pos] = filling
        self.frame = ''.join([str(char) for char in mutable_frame])

    def findLineLength(self) -> int:
        # it's [1] here because the examples start with a '\n'
        # so [0] is empty
        return len(self.frame.split("\n")[1])

    def printFrame(self):
        sys.stdout.write(self.frame)
        sys.stdout.flush()

    def translateCoordinateToFramePos(self, cord: FrameCoordinate):
        # Plus 2 for '\n'
        return 1 + cord.x * (self.findLineLength() + 1) + cord.y
    
    def getCharAt(self, cord: FrameCoordinate) -> str:
        return self.frame[self.translateCoordinateToFramePos(cord)]

    def isEdge(self, cord: FrameCoordinate) -> bool:
        return self.getCharAt(cord) in self.edges

    def hasWhiteSpace(self) -> bool:
        return ' ' in self.frame
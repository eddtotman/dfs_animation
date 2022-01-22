import sys
import random
from typing import List
from frame_coordinate import FrameCoordinate

class Frame:
    def __init__(self, initial_frame: str, edges: List[str] = ['-', '|', '+']) -> None:
        self.frame = initial_frame
        if self.frame[0] == '\n':
            self.frame = self.frame[1:len(self.frame)]
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
        # Plus 1 for '\n'
        return cord.x * (self.findLineLength() + 1) + cord.y
    
    def getCharAt(self, cord: FrameCoordinate) -> str:
        pos = self.translateCoordinateToFramePos(cord)
        if pos < 0 or pos >= self.len():
            return '-'
        return self.frame[pos]

    def isEdge(self, cord: FrameCoordinate) -> bool:
        return self.getCharAt(cord) in self.edges

    def hasWhiteSpace(self) -> bool:
        return ' ' in self.frame
    
    def isValidCoordinate(self, cord: FrameCoordinate) -> bool:
        return self.getCharAt(cord) == ' '

    def len(self) -> int:
        return len(self.frame)

    def numLines(self) -> int:
        return len(self.frame.split("\n")) - 1

    def pickRandomCoordinate(self) -> FrameCoordinate:
        rand_x = random.randrange(0, self.numLines())
        rand_y = random.randrange(0, self.findLineLength())
        return FrameCoordinate(rand_x, rand_y)

    def pickRandomWhitespace(self) -> FrameCoordinate:
        choice = self.pickRandomCoordinate()
        
        while self.getCharAt(choice) != ' ':
            choice = self.pickRandomCoordinate()

        return choice
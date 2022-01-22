from typing import List, Tuple

class FrameCoordinate:
    def __init__(self, x: int, y: int, adjacency_ops: List[Tuple[int,int]] = [(1,0), (0,1), (-1,0), (0,-1)]) -> None:
        self.x = x
        self.y = y
        self.adjacency_ops = adjacency_ops
        self.cur_op = 0

    def __str__(self) -> str:
        return "(x: {0}, y: {1})".format(self.x, self.y)
    
    def nextAdjacent(self) -> 'FrameCoordinate':
        if self.cur_op >= len(self.adjacency_ops):
            return None
        next_x = self.x + self.adjacency_ops[self.cur_op][0]
        next_y = self.y + self.adjacency_ops[self.cur_op][1]
        self.cur_op += 1
        return FrameCoordinate(next_x, next_y)
from time import sleep
from frame import Frame
from typing import List
import os

class Animation:
    def __init__(self, frames: List[Frame], playback_speed: float = 0.5) -> None:
        self.frames = frames
        self.playback_speed = playback_speed

    def playAnimation(self) -> None:
        for frame in self.frames:
            frame.printFrame()
            sleep(self.playback_speed)
            os.system('clear')
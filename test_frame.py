from frame import Frame
from frame_coordinate import FrameCoordinate

test_shape = '\n+------------+\n|            |\n|            |\n|            |\n+------+-----+\n|      |     |\n|      |     |\n+------+-----+'

def test_line_length():
    test_frame = Frame(test_shape)
    lines = [
        "+------------+",
        "|            |",
        "+------+-----+"
    ]
    for line in lines:
        assert test_frame.findLineLength() == len(line)

def test_cord_translate():
    test_frame = Frame(test_shape)
    assert '+' == test_frame.getCharAt(FrameCoordinate(0,0))
    assert '|' == test_frame.getCharAt(FrameCoordinate(1,0))
    assert ' ' == test_frame.getCharAt(FrameCoordinate(1,1))
    assert '+' == test_frame.getCharAt(FrameCoordinate(7, test_frame.findLineLength()-1))
    assert '-' == test_frame.getCharAt(FrameCoordinate(7, test_frame.findLineLength()-2))
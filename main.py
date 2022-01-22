from os import listdir
import random
from dfs_animation import animate_dfs

def main():
    shape_dir = "shapes"
    shapes = listdir(shape_dir)
    random.shuffle(shapes)
    while True:
        for shape in shapes:
            with open("{0}/{1}".format(shape_dir, shape)) as shape_file:
                animate_dfs(shape_file.read())


if __name__ == "__main__":
    main()
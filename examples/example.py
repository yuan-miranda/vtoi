# examples/example.py
import sys
sys.path.append('..')

from main import to_frames

def main():
    name = "../media/brookiecookie679.mov"
    to_frames(name, name.split("/")[-1].split(".")[0])

if __name__ == "__main__":
    main()
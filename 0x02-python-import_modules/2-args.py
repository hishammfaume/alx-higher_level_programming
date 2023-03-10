#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    nums = len(args)
    if nums == 0:
        print("0 arguments.")
    elif nums == 1:
        print("1 argument:")
    else:
        print(f"{nums} arguments:")
    for i, arg in enumerate(args):
        i += 1
        print("{}: {}".format(i, arg))

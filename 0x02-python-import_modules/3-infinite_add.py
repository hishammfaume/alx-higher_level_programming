#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    nums = sys.argv[1:]
    add = sum(int(num) for num in nums)
    print(add)

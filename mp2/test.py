# This is for godot integration soon™️ experience

import sys

def test_function(test):
    print(f"Testing function: {test}")

def main():
    args = sys.argv
    test_function(args[1])
    

if __name__ == "__main__":
    main()
    
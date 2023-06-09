#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    """Print all names defined by the hidden_4 module, sorted in alphabetical order."""
    names = dir(hidden_4)
    for name in sorted(names):
        if not name.startswith("__"):
            print(name)

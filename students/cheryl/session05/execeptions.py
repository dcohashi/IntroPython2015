#!/usr/bin/env python3
def safe_input():
    try:
        input("enter some text: ")
    except (EOFError, KeyboardInterrupt):
        return None

if __name__ == '__main__':
    print(safe_input())

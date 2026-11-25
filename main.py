#!/usr/bin/env python3
"""Fortune Cookies for Machines — writes one fortune-cookie line for an AI agent."""
import os

ENTRY = "You will be asked to do the impossible by Tuesday, and you will say 'Certainly!' before checking if Tuesday exists."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()

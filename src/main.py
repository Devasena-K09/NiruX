"""
NiruX - simple starter CLI
Run: python main.py
"""

import time
from agents.example_agent import ExampleAgent

def main():
    print("Starting NiruX (placeholder)...")
    agent = ExampleAgent()
    while True:
        user = input("\nYou: ")
        if user.strip().lower() in ("exit", "quit"):
            print("NiruX: Shubh din! (Goodbye)")
            break
        response = agent.handle(user)
        print("NiruX:", response)

if __name__ == "__main__":
    main()

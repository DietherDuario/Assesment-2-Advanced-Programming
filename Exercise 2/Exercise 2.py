import random

def load_jokes(filename):
    jokes = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if "?" in line:
                setup, punch = line.split("?", 1)
                jokes.append((setup.strip() + "?", punch.strip()))
    return jokes

def tell_joke(jokes):
    setup, punch = random.choice(jokes)
    print("\n" + setup)
    input("Press Enter for the punchline...")
    print(punch, "\n")

def main():
    jokes = load_jokes("joke.txt")

    print("Say 'Alexa tell me a joke' to hear one, or type 'quit' to exit.\n")

    while True:
        cmd = input("You: ").strip().lower()
        if cmd == "alexa tell me a joke":
            tell_joke(jokes)
        elif cmd == "quit":
            print("Goodbye!")
            break
        else:
            print("Alexa: I didn’t understand that. Try again.\n")

if __name__ == "__main__":
    main()

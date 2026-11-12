"""
Project 1: "Rule-Based Chatbot"
Made by : Muhammad Mujtaba
-----------------------------
A simple chatbot that uses if-elif-else logic to respond to
predefined user inputs. It runs in a continuous loop until the
user types an exit command.
"""

from datetime import datetime


def get_response(user_input):
    """Decide how to reply based on predefined rules."""
    text = user_input.lower().strip()

    # Rule 1: Greetings
    if text in ("hi", "hello", "hey", "good morning", "good evening"):
        return "Hello! How can I help you today?"

    # Rule 2: Asking about the bot
    elif "how are you" in text:
        return "I'm just a program, but I'm running great! How about you?"

    elif "your name" in text or "who are you" in text:
        return "I'm RuleBot, a simple rule-based chatbot."

    # Rule 3: Asking what the bot can do
    elif "help" in text or "what can you do" in text:
        return ("I can: greet you, tell the time or date, "
                "tell a joke, and chat a little. Type 'bye' to exit.")

    # Rule 4: Time and date
    elif "time" in text:
        return "The current time is " + datetime.now().strftime("%I:%M %p") + "."

    elif "date" in text or "today" in text:
        return "Today's date is " + datetime.now().strftime("%A, %d %B %Y") + "."

    # Rule 5: Fun
    elif "joke" in text:
        return "Why do programmers prefer dark mode? Because light attracts bugs!"

    # Rule 6: Polite replies
    elif "thank" in text:
        return "You're welcome!"

    # Default: nothing matched
    else:
        return "Sorry, I don't understand that. Type 'help' to see what I can do."


def main():
    exit_commands = ("bye", "exit", "quit", "goodbye")

    print("RuleBot: Hi! I'm RuleBot. Type 'help' for options or 'bye' to exit.")

    # Continuous loop
    while True:
        user_input = input("You: ")

        # Exit command check
        if user_input.lower().strip() in exit_commands:
            print("RuleBot: Goodbye! Have a great day!")
            break

        # Ignore empty input
        if user_input.strip() == "":
            print("RuleBot: Please type something.")
            continue

        print("RuleBot:", get_response(user_input))


if __name__ == "__main__":
    main()

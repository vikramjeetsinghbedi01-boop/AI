import colorama
from colorama import Fore, Style
from textblob import TextBlob

# Initialize colorama
colorama.init()

# Welcome Message
print(f"{Fore.CYAN} Welcome to Sentiment Spy! {Style.RESET_ALL}")

# Get user name
user_name = input(f"{Fore.MAGENTA}Please enter your name: {Style.RESET_ALL} ").strip()
if not user_name:
    user_name = "Mystery Agent"

# Store conversation history
conversation_history = []

# Intro Instructions
print(f"\n{Fore.CYAN}Hello, Agent {user_name}!")
print(f"Type a sentence and I will analyze its sentiment using TextBlob. 🔵")
print(f"Type {Fore.YELLOW}'reset'{Fore.CYAN}, {Fore.YELLOW}'history'{Fore.CYAN}, "
      f"or {Fore.YELLOW}'exit'{Fore.CYAN} to quit.{Style.RESET_ALL}\n")

# Main Loop
while True:
    user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()

    if not user_input:
        print(f"{Fore.RED}Please enter some text or a valid command.{Style.RESET_ALL}")
        continue

    # Exit command
    if user_input.lower() == "exit":
        print(f"\n{Fore.BLUE}👋 Exiting Sentiment Spy. Farewell, Agent {user_name}!{Style.RESET_ALL}")
        break

    # Reset history command
    elif user_input.lower() == "reset":
        conversation_history.clear()
        print(f"{Fore.CYAN}🗑️ All conversation history cleared!{Style.RESET_ALL}")
        continue

    # Show history command
    elif user_input.lower() == "history":
        if not conversation_history:
            print(f"{Fore.YELLOW}No conversation history yet.{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}📜 Conversation History:{Style.RESET_ALL}")
            for idx, (text, polarity, sentiment_type) in enumerate(conversation_history, start=1):
                if sentiment_type == "Positive":
                    color = Fore.GREEN
                    emoji = "positive"
                elif sentiment_type == "Negative":
                    color = Fore.RED
                    emoji = "negative"
                else:
                    color = Fore.YELLOW
                    emoji = "neutral"
                print(f"{idx}. {color}{emoji} {text} "
                      f"(Polarity: {polarity:.2f}, {sentiment_type}){Style.RESET_ALL}")
        continue

    # Sentiment Analysis
    blob = TextBlob(user_input)
    polarity = blob.sentiment.polarity

    # Determine sentiment type
    if polarity > 0.25:
        sentiment_type = "Positive"
        color = Fore.GREEN
        emoji = "positive"
    elif polarity < -0.25:
        sentiment_type = "Negative"
        color = Fore.RED
        emoji = "negative"
    else:
        sentiment_type = "Neutral"
        color = Fore.YELLOW
        emoji = "neutral"

    # Save to history
    conversation_history.append((user_input, polarity, sentiment_type))

    # Show result
    print(f"{color}{emoji} {sentiment_type} sentiment detected! "
          f"(Polarity: {polarity:.2f}){Style.RESET_ALL}")

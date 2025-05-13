import colorama
from colorama import Fore, Style
from textblob import TextBlob

colorama.init()

print(f"{Fore.CYAN}Welcome to the Sentiment Analysis Spy {Style.RESET_ALL}")


user_name = input(f"{Fore.YELLOW}Enter your name: {Style.RESET_ALL}")

if not user_name:
   user_name = "Mystery Agent" 

conversation_history = []

print(f"{Fore.GREEN}Hello, {user_name}!")
print(f"Type a sentence and I will analyze your sentence with Textblob and show you the sentiment")
print(f"{Fore.YELLOW}'reset' {Fore.CYAN} to quit.{Style.RESET_ALL}\n")

while True:
   user_input = input (f"{Fore.GREEN} >> {Style.RESET_ALL}").strip()

   if not user_input:
      print(f"{Fore.RED}Please enter some text or a valid command.{Style.RESET_ALL}")
      continue
   
   elif user_input.lower() == "reset":  
      conversation_history.clear()
      print(f"{Fore.CYAN}All Conversation History Cleared!{Style.RESET_ALL}")
      continue
   
   elif user_input.lower() == "history":
      if not conversation_history:
         print(f"{Fore.RED}No conversation history available.{Style.RESET_ALL}")    
      else:
            print(f"{Fore.CYAN}Conversation History:{Style.RESET_ALL}")
            for idx, (text,polarity,sentiment_type) in enumerate(conversation_history, 1):
               if sentiment_type == "positive":
                  color = Fore.GREEN
                  emoji = "😊"
               elif sentiment_type == "negative":
                  color = Fore.RED
                  emoji = "😞"
               else:
                  color = Fore.YELLOW
                  emoji = "😐"
                  
               print(f"{color}{idx}. {text} - Polarity: {polarity} {emoji}{Style.RESET_ALL}")          
      continue
   
   polarity = TextBlob(user_input).sentiment.polarity
   if polarity > 0.25:
        sentiment_type = "positive"
        color = Fore.GREENP
        emoji = "😊"
   elif polarity < -0.25:  
        sentiment_type = "negative"
        color = Fore.RED
        emoji = "😞"
   else:
        sentiment_type = "neutral"
        color = Fore.YELLOW
        emoji = "😐"

   conversation_history.append((user_input, polarity, sentiment_type))
 
   print(f"{color}Sentiment: {sentiment_type.capitalize()} - Polarity: {polarity} {emoji}{Style.RESET_ALL}")
   print(f"{Fore.CYAN}Conversation History:{Style.RESET_ALL}",conversation_history)


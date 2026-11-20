import colorama
from colorama import Fore,Style
from textblob import TextBlob # to find polarity
colorama.init()
print(f"{Fore.CYAN} Wellcome to Sentiment Spy{Style.RESET_ALL}")
name = input(f"{Fore.MAGENTA} Please enter your name: {Style.RESET_ALL}").strip()
if not name:
    name="Mystery Agent"
conversationhistory = [] 
print(f"{Fore.CYAN} Hello, agent {name}")
print(f"Type a sentence and i will analyse your sentence with textblob libray and show you the sentiment")
print(f"Type {Fore.YELLOW} reset{Fore.CYAN} ,{Fore.YELLOW} History{Fore.CYAN},or{Fore.YELLOW} Exit{Fore.CYAN} To Quit {Style.RESET_ALL}")
while True:
    userinput = input(f"{Fore.GREEN} >> {Style.RESET_ALL}").strip()
    if not userinput:
        print(f"{Fore.RED} Please Enter a text or a  valid command{Style.RESET_ALL}")
        continue
    if userinput.lower()=="exit":
        print(f"{Fore.BLUE} exiting sentiment spy. Good Bye agent {name}") 
        break
    elif userinput.lower()=="reset":
        conversationhistory.clear()
        print(f"{Fore.CYAN} All conservation history is cleared{Style.RESET_ALL}")
        continue
    elif userinput.lower() == "histoy":
        if not conversationhistory:
            print(f"{Fore.YELLOW} No conservation history yet{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN} conservation histoy:{Style.RESET_ALL}")
            for i,(text,polarity,sentimenttype) in enumerate(conversationhistory,start = 1):
                if sentimenttype == "Positive":
                    color = Fore.GREEN
                    emoji = "😊"
                elif sentimenttype == "Negative":
                    color = Fore.RED
                    emoji  = "😔"
                else:
                    color=Fore.YELLOW
                    emoji = "😐"
                print(f"{i}.{color}{emoji}{text} polarity:{polarity:.2f},{sentimenttype} {Style.RESET_ALL}")
        continue

    polarity = TextBlob(userinput).sentiment.polarity
    if polarity > 0.25:
        sentimenttype = "Positive"
        color = Fore.GREEN
        emoji = "😊"
    elif polarity < -0.25:
        sentimenttype = "Negative"
        color = Fore.RED
        emoji = "😔"
    else:
        sentimenttype = "Neutral" 
        color = Fore.YELLOW
        emoji = "😐"
    conversationhistory.append((input,polarity,sentimenttype))
    print(f"{color}{emoji}{sentimenttype} sentiment detected. polarity: {polarity:.2f}")
            
                

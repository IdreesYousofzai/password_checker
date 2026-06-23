import re
from colorama import Fore, Style, init

init(autoreset=True)

def check_password_strength(password):
    score = 0
    feedback = []

    # length rule
    if len(password) >= 8: 
        score += 1
    else: 
        feedback.append("Make it at least 8 characters long.")

    # check lower/upper case
    if re.search(r"[a-z]", password): 
        score += 1
    else: 
        feedback.append("Add a lowercase letter.")

    if re.search(r"[A-Z]", password): 
        score += 1
    else: 
        feedback.append("Add an uppercase letter.")

    # check numbers
    if re.search(r"\d", password): 
        score += 1
    else: 
        feedback.append("Add a number.")

    # check special chars
    if re.search(r"[ !@#$%^&*(),.?\":{}|<>]", password): 
        score += 1
    else: 
        feedback.append("Add a special character (e.g., !, @, #).")

    # score grading setup
    if score <= 2:
        rating = f"{Fore.RED}Weak \U0001F534"
    elif score <= 4:
        rating = f"{Fore.YELLOW}Medium \U0001F533"
    else:
        rating = f"{Fore.GREEN}Strong \U0001F532"

    return rating, score, feedback

if __name__ == "__main__":
    user_password = input("Enter a password to test: ")
    rating, score, tips = check_password_strength(user_password)
    
    print(f"\nStrength: {rating} ({score}/5)")
    
    # print hints if score is under 5
    if tips:
        print(f"\n{Fore.CYAN}Suggestions to improve:")
        for tip in tips:
            print(f"- {tip}")


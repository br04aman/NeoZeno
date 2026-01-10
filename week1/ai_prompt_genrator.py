from datetime import datetime

def ai_prompt_logger():
    prompt = input("Enter an AI prompt: ").strip()
    if not prompt:
        print("No prompt entered.")
        
        return

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {prompt}\n"

    with open("prompt_history.txt", "a", encoding="utf-8") as file:
        file.write(line)

    print("Prompt saved to prompt_history.txt")

ai_prompt_logger()

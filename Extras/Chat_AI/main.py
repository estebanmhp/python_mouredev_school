import openai
import config
import typer
from rich import print
from rich.table import Table

def main():

    openai.api_key = config.api_key

    print("💬 [bold green]ChatGTP API + Python[/bold green]")

    table = Table("Command", "Description")
    table.add_row("new", "Start a new chat")
    table.add_row("exit", "Finish the chat")
    table.add_row("command", "Remember commands")

    print(table)

    # Assistant context (it can be as specific as you would like)

    context = {"role": "system", "content": "You are an highly efficient asistant with focus in progrmmaing"}
    messages = [context]

    while True:

        content = __prompt()
        
        if content == "new":
            messages = [context]
            new = typer.confirm("✋\nAre you sure?\nI'm going to forget all about the previous chat.\nJust in case that you don't know")
            if new:
                content = input("🆕 Hello again.\nWhat would you like to chat about? ")
        elif content == "command":
            print("Here are all the commands that you can use")
            print(table)

        messages.append({"role": "user", "content": content})

        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )
        
        response_content = response.choices[0].message.content
        messages.append({"role": "assistant", "content": response_content})

        print(f"[bold green]> [/bold green] [green]{response_content}[/green]")

        
def __prompt() -> str:
    prompt = typer.prompt("What would you like to chat about? ")

    if prompt == "exit":
        exit = typer.confirm("✋\nAre you sure?\nI'm going to forget all about this chat.\nJust in case that you don't know")
        if exit:
            print("It was a pleasure chatting with you!!!\n👋")
            raise typer.Abort()
        
        return __prompt()

    return prompt

if __name__ == "__main__":
    typer.run(main)
from dotenv import load_dotenv
from rich.console import Console
from rich import print
import requests
import os

load_dotenv()

console = Console()

secret = os.getenv("SECRET_VALUE")

console.print(f"[bold green]Loaded secret:[/bold green] {secret}")

response = requests.get("https://jsonplaceholder.typicode.com/posts")
response.raise_for_status()

posts = response.json()

console.print("\n[bold cyan]First 3 Post Titles[/bold cyan]")

for i, post in enumerate(posts[:3], start=1):
    console.print(f"[yellow]{i}.[/yellow] [bold]{post['title']}[/bold]")
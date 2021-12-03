import speedtest
import socket
from rich.console import Console # type: ignore
from time import sleep

#Main App
internet  = speedtest.Speedtest()
server = internet.get_best_server()

IP = socket.gethostbyname(socket.gethostname())
Download = internet.download()
Upload = internet.upload()
Ping = internet.results.ping

console = Console()

works = ["Get list of servers", "Finding optimal server", "Downloading Speed", "Uploading Speed", "Logging Information"]
i = 0

with console.status("[bold green]Preparing...") as status:
    while i < len(works):
        work = works[i]
        sleep(2)
        console.log(f"{work} [green]: Completed")
        i += 1
    console.log(f"""[bold cyan]ID:[/bold cyan] [blue]{server['id']}
[bold cyan]HOST:[/bold cyan] [blue]{server['host']}
[bold cyan]SERVER:[/bold cyan] [blue]{server['cc']}

[bold cyan]IP:[/bold cyan] [white]{IP}
[bold cyan]Ping:[/bold cyan] [white]{Ping:.2f} ms
[bold cyan]Download:[/bold cyan] [white]{Download / 1024 / 1024:.2f} Mbit/s
[bold cyan]Upload:[/bold cyan] [white]{Upload / 1024 / 1024:.2f} Mbit/s
""")

# file for loging and testing function and code
# for seperation of code only
# i don't want to messed up the main code 
# so I do little function here and finalize in main

import speedtest
from rich.console import Console # type: ignore
import socket

console = Console()
wifi  = speedtest.Speedtest()
server = wifi.get_best_server()

IP = socket.gethostbyname(socket.gethostname())

console.log(f"""[bold white]ID:[/bold white] [blue]{server['id']}
[bold white]HOST:[/bold white] [blue]{server['host']}
[bold white]SERVER:[/bold white] [blue]{server['cc']}

[bold cyan]IP:[/bold cyan] [white]{IP}
[bold cyan]Ping:[/bold cyan] [white]{IP}
[bold cyan]Download:[/bold cyan] [white]{IP}
[bold cyan]Upload:[/bold cyan] [white]{IP}
""")
import nmap
import os
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table

scanner = nmap.PortScanner()

# Define network to scan
network = '172.20.10.0/24'


def scanNetwork(network):
    # Print scan results for all hosts
    print(f"Scanning network {network}...")
    scanner.scan(hosts=network, arguments="-sn")

    for host in scanner.all_hosts():
        print(f"\nFound Host {host}:")
        for key in scanner[host]["vendor"]:
            print(f'mac: {scanner[host]["addresses"]["mac"]} ({scanner[host]["vendor"][key]}')
            print(f'{scanner[host]["hostnames"][0]["name"]}')
        

def scan_host(network, ports):
    print(f"Scanning network {network}...")
    scanner.scan(hosts=network, arguments=f"-p {ports}")
    for host in scanner.all_hosts():
        print(f"\nScan results for {host}:")
        for proto in scanner[host].all_protocols():
            print('Protocol : %s' % proto)
            lport = scanner[host][proto].keys()
            lport = sorted(lport)
            for port in lport:
                print('port: %s (%s)  -  state: %s' % (port, scanner[host][proto][port]['name'], scanner[host][proto][port]['state']))


console = Console()

def main_screen():
    while True:
        console.clear()
        console.print(Panel("Welcome to the Main Screen", title="Main Menu", style="bold green"))
        choice = Prompt.ask("Please choose an option:\n1.Scan Current Network\n2.Scan Host\nQ/q. Quit\n", choices=["1", "2", "Q", "q"])
        if choice == "1":
            option1_screen()
        elif choice == "2":
            option2_screen()
        elif choice in ["Q","q"]:
            break

def option1_screen():
    while True:
        console.clear()
        console.print(Panel("Network Scan Screen", title="Scanning Network", style="bold blue"))
        choice = Prompt.ask("Digite o ip da sua rede (para voltar digite 'Back')")
        if choice == "Back":
            break
        else:
            scanNetwork(choice)
            Prompt.ask("[bold red]aperte 'ENTER' para continuar[/bold red]")
            break

def option2_screen():
    while True:
        console.clear()
        console.print(Panel("Scan Host Screen", title="Scanning Host", style="bold blue"))
        choice = Prompt.ask("Digite o IP do Host (para voltar digite 'Back')")
        if choice == "Back":
            break
        else:
            ports = Prompt.ask("Agora digite o intervalo de portas dado esse formato:\n    [italic white]<menor porta>-<maior porta>[/italic white]", default="1-1000")
            scan_host(choice, ports)
            Prompt.ask("[bold red]aperte 'ENTER' para continuar[/bold red]")
            break
            

if __name__ == "__main__":
    # main_screen()
    main_screen()
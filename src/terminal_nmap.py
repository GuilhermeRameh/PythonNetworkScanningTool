""" main script for terminal nmap """

import nmap
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

scanner = nmap.PortScanner()

# Define network to scan
NETWORK = "172.20.10.0/24"


def scan_network(network):
    """Print scan results for all hosts"""
    print(f"Scanning network {network}...")
    scanner.scan(hosts=network, arguments="-sn")

    for host in scanner.all_hosts():
        print(f"\nFound Host {host}:")
        for key in scanner[host]["vendor"]:
            print(
                f'mac: {scanner[host]["addresses"]["mac"]} ({scanner[host]["vendor"][key]}'
            )
            print(f'{scanner[host]["hostnames"][0]["name"]}')


def scan_host(network, ports):
    """Print scan results for a single host"""
    print(f"Scanning network {network}...")
    scanner.scan(hosts=network, arguments=f"-p {ports}")
    for host in scanner.all_hosts():
        print(f"\nScan results for {host}:")
        for proto in scanner[host].all_protocols():
            print(f"Protocol : {proto}")
            lport = scanner[host][proto].keys()
            lport = sorted(lport)
            for port in lport:
                print(f"port: {port} ({scanner[host][proto][port]['name']})")
                print(f"state: {scanner[host][proto][port]['state']}")


console = Console()


def main_screen():
    """Main screen for terminal nmap"""
    while True:
        console.clear()
        console.print(
            Panel("Welcome to the Main Screen", title="Main Menu", style="bold green")
        )
        choice = Prompt.ask(
            "Please choose an option:\n1.Scan Current Network\n2.Scan Host\nQ/q. Quit\n",
            choices=["1", "2", "Q", "q"],
        )
        if choice == "1":
            option1_screen()
        elif choice == "2":
            option2_screen()
        elif choice in ["Q", "q"]:
            break


def option1_screen():
    """Screen for option 1"""
    while True:
        console.clear()
        console.print(
            Panel("Network Scan Screen", title="Scanning Network", style="bold blue")
        )
        choice = Prompt.ask("Digite o ip da sua rede (para voltar digite 'Back')")
        if choice == "Back":
            break
        else:
            scan_network(choice)
            Prompt.ask("[bold red]aperte 'ENTER' para continuar[/bold red]")
            break


def option2_screen():
    """Screen for option 2"""
    while True:
        console.clear()
        console.print(
            Panel("Scan Host Screen", title="Scanning Host", style="bold blue")
        )
        choice = Prompt.ask("Digite o IP do Host (para voltar digite 'Back')")
        if choice == "Back":
            break
        else:
            ports = Prompt.ask(
                "Agora digite o intervalo de portas dado esse formato:\n"
                "    [italic white]<menor porta>-<maior porta>[/italic white]",
                default="1-1000",
            )

            scan_host(choice, ports)
            Prompt.ask("[bold red]aperte 'ENTER' para continuar[/bold red]")
            break


if __name__ == "__main__":
    # main_screen()
    main_screen()

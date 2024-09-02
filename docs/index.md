# Bem vindo a Documentação de Nmap Python Tool

## Layout do Projeto

    README.md
    requirements.txt        # Arquivo com as dependências
    mkdocs.yml              # Configuração do mkdocs
    docs/
        index.md            # Página inicial mkdocs
    src/
        terminal_nmap.py    # Arquivo principal python

## Requirements e Primeiros passos

O projeto funciona usando python, em conjunto com as bibliotecas:
nmap, os e rich-console.

Instale as bibliotecas necessárias com o comando:
> pip install -r requirements.txt

Além disso, verifique que possui a ferramenta NMAP instalada. Senão, para distribuições linux Ubuntu, rode:

> sudo apt-get update
>
> sudo apt-get install nmap

## Primeira Execução
Execute o comando para iniciar o programa python:

> python terminal_nmap.py

## Uso

Na tela principal, o usuário é apresentado com um painel que exibe o texto "Welcome to the Main Screen". O usuário é então solicitado a escolher uma das seguintes opções:

<b>
1: Scan Current Network - Para escanear uma rede inteira.

2: Scan Host - Para escanear portas específicas de um host.

Q/q: Quit - Para sair do programa.
</b>

### Opção 1
Nesta tela, o usuário deve digitar o endereço IP da rede que deseja escanear, no formato CIDR (por exemplo, 192.168.0.0/24).
O script então executa um escaneamento utilizando o nmap com o comando -sn, que é um "ping scan", buscando identificar quais hosts estão ativos na rede especificada.
Os resultados do escaneamento são exibidos no terminal, mostrando cada host encontrado, seu endereço MAC e o nome do host, se disponível.
Após o escaneamento, o usuário pode pressionar "ENTER" para retornar à tela principal.

### Opção 2
Se o usuário escolher a opção "2", ele será direcionado para a tela de escaneamento de host (option2_screen):

Nesta tela, o usuário deve digitar o endereço IP do host que deseja escanear.
Em seguida, o usuário é solicitado a inserir um intervalo de portas para escanear (por exemplo, 1-1000).
O script então executa um escaneamento utilizando o nmap, especificando as portas a serem verificadas no host selecionado.
Os resultados do escaneamento são exibidos no terminal, mostrando as portas abertas, o nome do serviço associado a cada porta e o estado de cada porta (aberta ou fechada).
Após o escaneamento, o usuário pode pressionar "ENTER" para retornar à tela principal.

### Saindo do programa
Em qualquer ponto no menu principal, se o usuário escolher "Q" ou "q", o programa termina a execução e o terminal volta ao prompt de comando padrão.

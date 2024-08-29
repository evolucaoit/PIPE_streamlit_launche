import os
import subprocess
from InquirerPy import inquirer
from colorama import init, Fore, Style

# Inicializar Colorama
init(autoreset=True)

# Função para exibir o logo em ASCII
def display_logo():
    logo = """
██████╗ ██╗██████╗ ███████╗
██╔══██╗██║██╔══██╗██╔════╝
██████╔╝██║██████╔╝█████╗  
██╔═══╝ ██║██╔═══╝ ██╔══╝   
██║     ██║██║     ███████╗
╚═╝     ╚═╝╚═╝     ╚══════╝
    """
    print(Fore.RED + Style.BRIGHT + logo)

# Função para listar arquivos .py na raiz
def list_python_files():
    return [f for f in os.listdir('.') if f.endswith('.py')]

# Função para executar um comando de sistema
def run_command(command):
    subprocess.run(command, shell=True)

# Função principal
def main():
    # Exibe o logo
    display_logo()

    # Lista os arquivos .py
    py_files = list_python_files()
    if not py_files:
        print(Fore.RED + "Nenhum arquivo .py encontrado na raiz.")
        return

    # Pergunta ao usuário qual arquivo deseja lançar
    file_to_run = inquirer.select(
        message="Selecione um arquivo para lançar com Streamlit:",
        choices=py_files,
        instruction="Use as setas para navegar e Enter para selecionar"
    ).execute()

    # Comando para lançar o arquivo com Streamlit
    command = f"py -m streamlit run {file_to_run}"
    print(Fore.RED + f"Lançando: {command}")
    run_command(command)

if __name__ == "__main__":
    main()

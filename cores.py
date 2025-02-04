from colorama import Fore, Back, Style, init

# Inicializa o colorama (necessário no Windows)
init()

print(Fore.RED + "Isso é vermelho")
print(Fore.GREEN + "Isso é verde")
print(Fore.BLUE + "Isso é azul")
print(Fore.YELLOW + "Isso é azul")
print(Style.RESET_ALL)  # Reseta as cores
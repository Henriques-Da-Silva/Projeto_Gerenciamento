'''Restrições: o estoque deve ser maior que dez para permitir a venda, garanta que se for 
digitado número no nome da fruta, o prgrama não adicione a fruta e o nome deve ter pelo 
menos 3 letras, o preço não pode ser negativo e deve estar em KZ, não pode ser adicionado 
um número negativo ao estoque, o programa só pára se o usuário quiser, trata todo tipo de 
Exceções se houverem, não pode haver duas frutas iguais na lista. '''

import time
import os

frutas = {
            "Maçã": {"preço": 300, "quantidade": 15, "Total Vendido": 0},
            "Banana": {"preço": 200, "quantidade": 13, "Total Vendido": 0},
            "Laranja": {"preço": 100, "quantidade": 10, "Total Vendido": 0},
            "Uva": {"preço": 500, "quantidade": 15, "Total Vendido": 0},
            "Pera": {"preço": 250, "quantidade": 10, "Total Vendido": 0},
            "Manga": {"preço": 100, "quantidade": 10, "Total Vendido": 0},
            "Melancia": {"preço": 600, "quantidade": 15, "Total Vendido": 0},
            "Abacaxi": {"preço": 300, "quantidade": 10, "Total Vendido": 0},
            "Morango": {"preço": 700, "quantidade": 11, "Total Vendido": 0},
            "Kiwi": {"preço": 400, "quantidade": 14, "Total Vendido": 0},
        }

opcao = 0

class BarracaDeFrutas():
    
    def __init__(self):
        self.main()
    
    def main(self):
        global opcao
        while opcao != 8:
            print('='*50)
            print('         GERENCIAMENTO DA LOJA DE FRUTAS')
            print('='*50)
            print('1- Vender \n2- Remover Fruta. \n3- Adicionar Qtd em estoque de uma fruta. \n4- Adicionar Fruta. \n5- Buscar Fruta. \n6- Exibir Dados das Frutas. \n7- Relatórios. \n8- Sair.')
            print('='*50)
            opcao = int(input('Opção: '))
            print('='*50)
            match opcao:
                case 1:
                    self.vender()
                case 2:
                    self.remover_fruta()
                case 3:
                    self.adicionar_quantidade_de_uma_fruta()
                case 4:
                    self.adicionar_fruta()
                case 5:
                    self.buscar_frutas_por_nome()
                case 6:
                    self.relatorios(opcao)
                case 7:
                    self.relatorios(opcao)
                case 8:
                    print('SAINDO.', end='')
                    time.sleep(1)
                    print('.', end='')
                    time.sleep(1)
                    print('.')
                    time.sleep(1)
                    os.system('cls')
                    print('SAIU.')
                    break
                case __:
                    print('OPÇÃO INVÁLIDA!')
                    time.sleep(3)
                    os.system('cls')

    def adicionar_fruta(self):
        
        print
        
    def remover_fruta(self):
        encontrada = False
        os.system('cls')
        print('='*46)
        nome = input('Digite o nome da fruta: ')
        print('='*46)
        for fruta, dados in frutas.items():
            if fruta.lower() == nome.lower():
                encontrada = True
                del frutas[fruta]
                print('FRUTA REMOVIDA COM SUCESSO!')
                print('='*46)
                op = 4
                while op != 1:
                    op = int(input('1- Voltar.\nOpção: '))
                    if op == 1:
                        os.system('cls')
                        self.main()
                    else:
                        print('OPÇÃO INVÁLIDA!')
                        time.sleep(3)
        if encontrada == False:
            print(f'A fruta "{nome}" não está na sua lista de frutas.')
            print('='*46)
            time.sleep(5)
            os.system('cls')
            self.main()
            
    def adicionar_quantidade_de_uma_fruta(self):
        encontrada = False
        os.system('cls')
        print('='*46)
        print('     ADICIONAR QUANTIDADE DE UMA FRUTA')
        print('='*46)
        nome = input('Insira o Nome da Fruta: ')
        print('='*46)
        for fruta, dados in frutas.items():
            if fruta.lower() == nome.lower():
                encontrada = True
                try:
                    qtd = int(input('Insira a Quantidade a Adicionar: '))
                    if qtd > 0:
                        dados['quantidade'] += qtd
                        print('='*46)
                        print('QUANTIDADE ADICIONADA COM SUCESSO!')
                        print('='*46)
                        time.sleep(3)
                        os.system('cls')
                        self.main()
                    else:
                        print('='*46)
                        print('IMPOSSÍVEL adicionar valor negativo!')
                        time.sleep(5)
                        self.adicionar_quantidade_de_uma_fruta()
                except ValueError:
                    print('='*46)
                    print('Insira somente valor inteiro pra quantidade.')
                    time.sleep(5)
                    self.adicionar_quantidade_de_uma_fruta()
                    
        if encontrada == False:
            print(f'A fruta "{nome}" não está na sua lista de frutas.')
            print('='*46)
            time.sleep(5)
            os.system('cls')
            self.main() 
        
    def vender(self):
        print
        
    def buscar_frutas_por_nome(self):
        encontrada = False
        os.system('cls')
        print('='*46)
        nome = input('Digite o nome da fruta: ')
        print('='*46)
        for fruta, dados in frutas.items():
            if fruta.lower() == nome.lower():
                encontrada = True
                print('              DADOS DA FRUTA')
                print('='*46)
                print('|___Nome___|_Preço(kzs)_|Quantidade|_Vendido_|')
                print(f'|{fruta:^10}|{dados['preço']:^12}|{dados['quantidade']:^10}|{dados['Total Vendido']:^9}|')
                print('='*46)
                op = 4
                while op != 1:
                    op = int(input('1- Voltar.\n2- Buscar outra fruta. \nOpção: '))
                    if op == 1:
                        os.system('cls')
                        self.main()
                    elif op == 2:
                        self.buscar_frutas_por_nome()
                    else:
                        print('OPÇÃO INVÁLIDA!')
                        time.sleep(3)
        if encontrada == False:
            print(f'A fruta "{nome}" não está na sua lista de frutas.')
            print('='*46)
            time.sleep(5)
            os.system('cls')
            self.main()
            
    def relatorios(self, op):
        global frutas
        # Listar os dados de todas as frutas
        if op == 6:
            os.system('cls')
            print('='*46)
            print('               _ESTOQUE_ATUAL_')
            print('='*46)
            print('|___Nome___|_Preço(kzs)_|Quantidade|_Vendido_|')
            for fruta, dados in frutas.items():
                print(f'|{fruta:^10}|{dados['preço']:^12}|{dados['quantidade']:^10}|{dados['Total Vendido']:^9}|')
            print('='*46)
            while op != 1:
                op = int(input('1- Voltar.\nOpção: '))
                if op == 1:
                    os.system('cls')
                    self.main()
                else:
                    print('OPÇÃO INVÁLIDA!')
                    time.sleep(3)
                    
        # Total Pressuposto com as vendas
        else:
            os.system('cls')
            total = 0
            for fruta, dados in frutas.items():
                total_fruta = float(dados['preço']) * int(dados['quantidade'])
                total += total_fruta
            print('='*50)
            print('Total Pressuposto com as Vendas: ', total, ' kzs')
            
        # Total adquirido até agora
            total_adquirido = 0
            for fruta, dados in frutas.items():
                total_fruta = float(dados['preço']) * int(dados['Total Vendido'])
                total_adquirido += total_fruta
            print('='*50)
            print('Total Adquirido até Agora: ', total_adquirido, ' kzs')
            print('='*50)
            op = 4
            while op != 1:
                op = int(input('1- Voltar.\nOpção: '))
                if op == 1:
                    os.system('cls')
                    self.main()
                else:
                    print('OPÇÃO INVÁLIDA!')
                    time.sleep(3)
    
BarracaDeFrutas()
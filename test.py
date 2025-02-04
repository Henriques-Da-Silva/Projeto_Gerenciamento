class BarracaDeFrutas:
    def _init_(self):
        self.frutas = {
            "Maçã": {"preço": 2.5, "quantidade": 10, "vendido": 0},
            "Banana": {"preço": 1.2, "quantidade": 10, "vendido": 0},
            "Laranja": {"preço": 1.8, "quantidade": 10, "vendido": 0},
            "Uva": {"preço": 3.5, "quantidade": 10, "vendido": 0},
            "Pera": {"preço": 2.2, "quantidade": 10, "vendido": 0},
            "Manga": {"preço": 4.0, "quantidade": 10, "vendido": 0},
            "Melancia": {"preço": 6.0, "quantidade": 10, "vendido": 0},
            "Abacaxi": {"preço": 5.5, "quantidade": 10, "vendido": 0},
            "Morango": {"preço": 7.0, "quantidade": 10, "vendido": 0},
            "Kiwi": {"preço": 3.8, "quantidade": 10, "vendido": 0},
        }
        self.total_vendas = 0

    def estoque(self):
        print("\nEstoque Atual:")
        for fruta, dados in self.frutas.items():
            print(f"{fruta}: {dados['quantidade']} unidades - R${dados['preço']:.2f} cada")

    def vender_fruta(self, nome, quantidade):
        if nome in self.frutas:
            if self.frutas[nome]["quantidade"] >= quantidade:
                self.frutas[nome]["quantidade"] -= quantidade
                valor_venda = self.frutas[nome]["preço"] * quantidade
                self.frutas[nome]["vendido"] += valor_venda
                self.total_vendas += valor_venda
                print(f"Venda realizada! {quantidade} {nome}(s) por R${valor_venda:.2f}")
            else:
                print("Estoque insuficiente!")
        else:
            print("Fruta não encontrada!")

    def total_vendas(self):
        print(f"\nTotal vendido: R${self.total_vendas:.2f}")


barraca = BarracaDeFrutas()

while True:
    print("\n1. Exibir Estoque")
    print("2. Vender Fruta")
    print("3. Exibir Total Vendido")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        barraca.exibir_estoque()
    elif opcao == "2":
        fruta = input("Digite o nome da fruta: ")
        qtd = int(input("Quantidade a vender: "))
        barraca.vender_fruta(fruta, qtd)
    elif opcao == "3":
        barraca.exibir_total_vendas()
    elif opcao == "4":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida! Tente novamente.")
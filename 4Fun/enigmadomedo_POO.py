# Feito por Cacatua - 22/10/2020
# Baseado no seguinte projeto: https://gabrielf9.github.io/enigma_do_medo/
# Caso não tenha requests instalado, utilize: pip install requests

import requests

class Itens:
    def __init__(self, id, titulo, preco, pago, pendente, total_pago, total_pendente, total):
        self._id = id
        self._titulo = titulo
        self._pago = pago
        self._preco = preco
        self._pendente = pendente
        self._total_pago = total_pago
        self._total_pendente = total_pendente
        self._total = total

    # Getters
    @property
    def id(self):
        return self._id
    
    @property
    def titulo(self):
        return self._titulo
    
    @property
    def preco(self):
        return self._preco

    @property
    def pago(self):
        return self._pago

    @property
    def pendente(self):
        return self._pendente
    
    @property
    def total_pago(self):
        return self._total_pago

    @property
    def total_pendente(self):
        return self._total_pendente

    @property
    def total(self):
        return self._total

# Função para mostrar as operações requisitadas
def mostraOperacoes(lista, recompensas):
    total = 0
    pendente = 0
    for elem in recompensas:
        for i in lista:
            if i == '1':
                print(f'Título: {elem.titulo}')
            elif i == '2':
                print(f'Preço: R${int(elem.preco)}')
            elif i == '3':
                print(f'Pago: {elem.pago} unidades')
            elif i == '4':
                print(f'Total pago: R${int(elem.total_pago)}')
            elif i == '5':
                print(f'Pendente: {elem.pendente} unidades')
            elif i == '6':
                print(f'Total pendente: R${int(elem.total_pendente)},00')
            elif i == '7':
                print(f'Total: R${int(elem.total)}')
            elif i == '8':
                total += int(elem.total_pago)
                pendente += int(elem.total_pendente)
        print()

    if '8' in lista:
        print(f"O total arrecadado é: R${total}")
        print(f"O total pendente é: R${pendente}")
        print(f"Se todos os pendentes forem pagos, totalizará: R${total + pendente}")
        print()

def main():
    i = 0
    recompensas = []

    site = requests.get('https://api.catarse.me/reward_details?project_id=eq.122021')
    novo_site = site.json()

    for item in novo_site:
        recompensa = Itens(i, item['title'], item['minimum_value'], item['paid_count'], item['waiting_payment_count'], (float(item['minimum_value']) * float(item['paid_count'])), (float(item['minimum_value']) * float(item['waiting_payment_count'])), (int(item['paid_count']) * int(item['minimum_value']) + int(item['waiting_payment_count']) * int(item['minimum_value'])))
        recompensas.append(recompensa)
        i += 1

    while True:
        print("=" * 35)
        print("Menu de Operações")
        print("1 - Ver o título")
        print("2 - Ver o preço")
        print("3 - Ver a quantidade paga")
        print("4 - Ver o total pago")
        print("5 - Ver a quantidade pendente")
        print("6 - Ver o total pendente")
        print("7 - Ver o total pago e pendente")
        print("8 - Ver o total arrecadado")
        print("9 - Sair do programa")
        opcoes = input("Selecione quais opções deseja ver colocando o dígito da operação separando por espaços: ") 

        if opcoes == '9':
            print("Você decidiu sair, até mais!")
            break

        else:
            print()
            mostraOperacoes(opcoes.split(), recompensas)

if __name__ == "__main__":
    main()
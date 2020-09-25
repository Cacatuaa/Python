def main():
    qtd = int(input("Quantidade de jogos grátis: "))
    if qtd == 1:
        nome = input("Digite o nome do jogo: ")
        link = input("Digite o link do jogo: ")
        data = input("Digite a data que expira a promoção: ")
        print("="*25)
        print(f'**{nome}** está gratuito na **Epic Games**. A promoção termina **{data}** às **12:00**.')
        print("@LOOTS")
        print(link)
        print("="*25)

    elif qtd == 2:
        nome = input("Digite o nome do primeiro jogo: ")
        link = input("Digite o link do primeiro jogo: ")
        nome2 = input("Digite o nome do segundo jogo: ")
        link2 = input("Digite o link do segundo jogo: ")
        data = input("Digite a data que expira a promoção: ")
        print("="*25)
        print(f'**{nome}** e **{nome2}** estão gratuitos na **Epic Games**. A promoção termina **{data}** às **12:00**.')
        print("@LOOTS")
        print(link)
        print(link2)
        print("="*25)

if __name__ == "__main__":
    main()
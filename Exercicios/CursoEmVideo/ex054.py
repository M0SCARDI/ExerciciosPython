from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior = totmaior + 1
    else:
        totmenor= totmenor + 1
print('Ao todo tivemos {} pessoas maiores de idade '.format(totmaior))
print('Ao todo tivemos {} pessoas menores de idade '.format(totmenor))

from time import sleep
import random
sleep(1)

print('''É um prazer ter você no Pizza But!!!
Para melhor agilidade,faça aqui seu pedido.''')
o1 = str(input('Digite S para continuar: ')).strip().upper()
while o1 != 'S':
    o1 = str(input('Ops, não entendi! Digite S para fazer seu pedido: ')).strip().upper()

nome = input('Informe seu nome e sobrenome: ')

print(f'''Olá {nome[0:20]}. Essas são nossas opções de sabores:
[1] Calabresa
[2] Peperoni
[3] Portuguesa
[4] Bacon
[5] Mussarela
[6] Frango com Catupiry''')
opcao1 = str(input('Qual sabor você vai querer? (escolha o nº da sua opção): '))

while opcao1 not in '123456':
    opcao1 = str(input('Opção invalida, digite novamente, inserindo o nº da sua opção: '))

sleep(0.5)
print()
adc = str(input('''Temos alguns ingrendientes caso você queria adicionais:
[1] Tomate
[2] Azeitona
[3] Ovos
[4] Bacalhau
[5] Azeitona preta
[6] Cebola
[7] Bacon
[8] Não quero adicionais: '''))
while adc not in '12345678':
    adc = str(input('Opção invalida, digite novamente, inserindo o nº da sua opção: '))

sleep(0.5)

print(f'Pedido realizado!!! Aguarde 3 segundos que já ficará pronto')
sleep(1)
print('...')
sleep(1)
print('...')
sleep(1)
print('...')
sleep(1)


list = [1,2,3,4,5]
esco = random.choice(list)

print(f'Tudo pronto {nome[0:20]}, dirija-se ao balcão {esco} para pegar seu pedido!')

# listas_vazia = []

# listas_vazia.append("Olá")
# listas_vazia.append("Mundo")

# print(listas_vazia)

# ////////////////////////////////

# pessoa = {
#     "nome":"Lucas Silva",
#     "idade":27,
#     "peso":70.9
# }

# print(pessoa['nome'])
# print(pessoa['idade'])
# print(pessoa['peso'])

# ////////////////////////////////

# import os

# mensagens = []

# nome = input("Digite seu nome: ")

# while True:

#     #limpa o terminal
#     os.system('cls')

#     if len(mensagens)>0:
#         for m in mensagens:
#             print(m['nome'], "-", m['texto'])

#     print("__________________________________")

#     texto = input("mensagem: ")
#     if texto == "fim":
#         break

#     #adiciona mensagem na lista
#     mensagens.append({
#         "nome":nome,
#         "texto":texto
#     })


# ////////////////////////////////

# def minha_funcao(valor1, valor2):
#     return valor1+valor2


# while True:
#     valor1 = int(input("Digite um valor"))
#     valor2 = int(input("Digite outro valor"))

#     resposta = minha_funcao(valor1, valor2)
#     print(valor1, "+", valor2, "=", resposta)


# ////////////////////////////////

fluxo_caixa = []

print("__________________")
print("@ Fluxo de caixa")
print("__________________")
print("1 - Adicionar receita")
print("2 - Adicionar despesa")
print("\n# Digite outro numero para encerrar #\n")


def adicionar_transacao_lucro():
    nome = input("Nome: ")
    valor = float(input("Valor ganho: "))
    fluxo_caixa.append({
        "nome": nome,
        "valor": valor
    })

def adicionar_transacao_despesa():
    nome = input("Nome: ")
    valor = float(input("Valor gasto: "))
    fluxo_caixa.append({
        "nome": nome,
        "valor": -valor
    })


while True:

    opcao = int(input("Digite a opção"))

    if opcao == 1:
        adicionar_transacao_lucro()
    elif opcao == 2:
        adicionar_transacao_despesa()
    else:
        break

total = 0
for fc in fluxo_caixa:
    print("Nome", fc['nome'], ", Valor: R$", fc['valor'])
    total = total+fc['valor']

print("Saldo atual: R$", total)

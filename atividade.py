clientes = [
    ["Wanderson", 50, 3200.00, "bom"],
    ["Priscila", 45, 5300.00, "bom"],
    ["Bianca", 25, 1200.00, "ruim"],
]

def validar_credito(cliente):
    idade = cliente[1]
    renda = cliente[2]
    historico = cliente[3]

    if idade >= 50 and renda <= 1000 and historico == "ruim":
        return "ALTO RISCO"
    elif idade >= 50 and renda >= 1000 and historico == "bom":
        return "MÉDIO RISCO"
    elif idade >= 20 and renda >= 3000 and historico == "bom":
        return "BAIXO RISCO"
    elif historico == "ruim":
        return "ALTO RISCO"
    else:
        return "SEM RESPOSTA"


for cliente in clientes:
    nome = cliente[0]
    print(f"{nome}: {validar_credito(cliente)}")
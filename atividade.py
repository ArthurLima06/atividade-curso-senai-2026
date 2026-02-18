clientes = {["Wanderson", 50, 3200.00, "bom"],
            ["Priscila", 45, 5300.00, "bom"],
            ["Bianca", 25, 1200.00, "ruim"]}

def validar_credito():
    if clientes[i,1] >= 50 and clientes[i,2] <= 1000 and clientes[i,3] == "ruim":
        print ("ALTO RISCO")
    elif clientes[i,1] >= 50 and clientes[i,2] >= 1000 and clientes[i,3] == "bom":
        print ("MÉDIO RISCO")
    elif clientes[i,1] >= 20 and clientes [i,2] >= 3000 and clientes[i,3] == "bom":
        print ("BAICO RISCO")
    else:
        print ("SEM RESPOSTA")


   print (validar_credito()) 
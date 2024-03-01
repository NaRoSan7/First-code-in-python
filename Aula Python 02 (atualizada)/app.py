produto = float(input("Digite o valor do produto R$: "))
desconto = float(input("Qual o desconto pro camarada?: "))

desconto = float(desconto/100);
vf = float(produto-produto*desconto);

print("O valor Final do produto:" + str(vf))

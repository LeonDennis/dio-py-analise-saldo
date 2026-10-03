entrada = input().strip()

saldo = 0.0

lancamentos = entrada.split(',')

for lancamento in lancamentos:
    tipo, valor = lancamento.strip().split()
    valor = float(valor)
    if tipo == 'R':
        saldo += valor
        
    elif tipo == 'D':
        saldo -= valor 
    

print(f"{saldo:.2f}")

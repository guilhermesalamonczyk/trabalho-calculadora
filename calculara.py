#calculadora de aprovação escolar

nome = input ("Digite o nome do estudante:")

soma_notas = 0
quantidade_trimestre = 3
meta_aprovacao = 180

#Coleta notas dos 3
for i range(1, quantidade_trimestre +1):
    nota = float(input("informe a nota {i}º periodo:"))
soma_notas += notas

print ("-" * 30)
print(f "Esudante: {nome}")
print(f"Pontuação Total: {soma_notas}")

#Verificar o Status de aprovação
if soma_notas >= meta_aprovacao:
    print(Status: " APROVADÃO! Parabens!! Finalmente!!")
else:
    pontos_faltantes = 
    meta aprovacao - soma_notas
    print("Status: TENTE OUTRA VEZ! ")
    print(f"faltaram {pontos_faltantes}pontos para atingir o minimo de aprovação")
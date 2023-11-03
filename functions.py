# variáveis: número em binário, decimal, potência, binário em str, i
# 1.  número em binário:                             1  0  1  0  (int) 
# 2.  inverter:                                      0  1  0  1  (str)
# 3.  iterar cada item, cada item se multiplica por 2 (int)
# 4.  se item==0: ignorar iteração (continue)
# 5.1 elevar a potência 0 até a última contagem:     0⁰ [2¹] 0² [2³] (int)
# 5.2 após o cálculo do item na sua potência, somá-lo junto a variável "decimal" (int)

binario = 1010
decimal = p = 0
binStr = str(binario)[::-1]

for i in binStr:
    i = int(i) * 2
    if i == 0:
        p += 1
        continue
    decimal += i ** p
    p += 1

print(decimal)

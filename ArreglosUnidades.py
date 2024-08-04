tprt = int(input("Ingrese la cantidad de Temperatura que desea ingresar: "))
temperaturas = []


for i in range(tprt):
    temp = float(input(f"Ingrese la temperatura #{i+1}: "))
    temperaturas.append(temp)
    
if tprt > 0: 
    media = sum(temperaturas) / tprt 
else: 
    media = 0 

    
count_superiores_o_iguales = sum(1 for temp in temperaturas if temp >= media)


print(f"La media de temperaturas es: {media:.2f}")
print(f"Cantidad de temperaturas superiores o iguales a la media: {count_superiores_o_iguales}")  

if __name__ == "__main__":
    main()  
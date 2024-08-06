def convertir_fecha(texto_fecha):
    
    meses = {
        'Enero': 1, 'Febrero': 2, 'Marzo': 3, 'Abril': 4, 'Mayo': 5, 'Junio': 6,
        'Julio': 7, 'Agosto': 8, 'Septiembre': 9, 'Octubre': 10, 'Noviembre': 11, 'Diciembre': 12
    }
    
    try:
       
        partes = texto_fecha.split(',')
        dia = int(partes[0].strip())
        mes_y_anio = partes[1].strip().split()
        mes = mes_y_anio[0]
        anio = int(mes_y_anio[1])
        
        
        mes_numero = meses.get(mes)
        if mes_numero is None:
            raise ValueError("Nombre del mes no válido.")
        
        return f"{dia}/{mes_numero}/{anio}"
    except (IndexError, ValueError) as e:
        return f"Error: {e}. Asegúrarel ingreso de la fecha en el formato 'DD, Mes AAAA'."


fecha_u = input("Ingrasa una fecha (DD, Mes AAAA): ")
resultado = convertir_fecha(fecha_u)


print("Fecha en formato numérico:", resultado)

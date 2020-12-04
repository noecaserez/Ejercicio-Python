id_clientes = {
    10 : 'Roxana',
    11 : 'Francisco',
    12 : 'Jose',
    13 : 'Natalia',
    14 : 'Nadia',
}

valor_clientes = {
    10 : {'Nombre' : 'Roxana Rodriguez', 'Direccion' : 'Berazategui', 'Telefono' : 1543432020, 'Correo' : 'roxanarodriguez@gmail.com', 'Preferente' : True},
    11 : {'Nombre' : 'Francisco Roldán', 'Direccion' : 'Luis Guillón', 'Telefono' : 1522221111, 'Correo' : 'fran_roldan@gmail.com', 'Preferente' : True},
    12 : {'Nombre' : 'José Fernandez', 'Direccion' : 'Martinez', 'Telefono' : 1500001111, 'Correo' : 'sin e-mail confirmado', 'Preferente' : False},
    13 : {'Nombre' : 'Natalia Lopez', 'Direccion' : 'Morón', 'Telefono' : 114444444, 'Correo' : 'natalia_correo@gmail.com', 'Preferente' : True},
    14 : {'Nombre' : 'Nadia Castro', 'Direccion' : 'Berazategui', 'Telefono' : 1543432020, 'Correo' : 'roxanarodriguez@gmail.com', 'Preferente' : True}
}


opciones = """
INGRESE UNA OPCION:
 
1) Añadir cliente 
2) Eliminar cliente 
3) Mostrar cliente 
4) Listar todos los clientes ID / Nombre
5) Listar clientes preferentes 
6) Terminar
 
SU OPCION: """
 
def main():
    datos_clientes = 0
    while datos_clientes <= 6:
        if datos_clientes == 0:
            datos_clientes = mostrar_opciones() #Opciones
 
        elif datos_clientes == 1: # 1 - Añadir cliente  
            id_cliente = max_id()

            Nombre = str(input("ingrese Nombre de nuevo Cliente: "))
            Direccion = str(input("Ingrese Direccion de nuevo cliente: "))
            Telefono = input("Ingrese Telefono del nuevo cliente: ")
            Correo = input("Ingrese correo electronico de Nuevo cliente: ")
            Preferente = input("¿Es usuario Preferente?. Ingresar Si/(No):  ") or "No"
            a = ['si', 's', "true"]
            if Preferente.lower() in a: #buscar un valor en una lista hay que usar el IN
                Preferente = True
            else:
                Preferente = False
                
            

            valor_clientes[id_cliente] = (dict(Nombre=Nombre, Direccion=Direccion, Telefono=Telefono, Correo=Correo, Preferente=Preferente))
            id_clientes[id_cliente] = Nombre #se agrega al diccionario id_clientes
            
            print(f"Nuevo Cliente ingresado.\nDatos:\n {list(valor_clientes.keys())[-1]}: {list(valor_clientes.values())[-1]}")

            datos_clientes = 0
 
        elif datos_clientes == 2: # 2 - Eliminar cliente
            eliminar_cliente()

            datos_clientes = 0
 
        elif datos_clientes == 3: #3 - Mostrar cliente Preguntar por el ID del cliente y mostrar sus datos
            mostrar_cliente_porID()

            datos_clientes = 0
 
        elif datos_clientes == 4: #Mostrar lista de todos los clientes de la base datos con su ID y nombre.
            mostrar_clientes()
 
            datos_clientes = 0
 
        elif datos_clientes == 5: #Mostrar la lisa de clientes preferentes de la base de datos con su ID y nombre.
            cliente_preferente()

            datos_clientes = 0
 
        elif datos_clientes == 6:
            print("\nAdios!")
            break
 
        else:
            print("No ha elegido ninguna opcion correcta")
            datos_clientes = 0
 
#Opciones
def mostrar_opciones():
    datos = int(input(opciones))
    return datos
 
# 1 - Añadir Cliente
def max_id():
    if len(id_clientes) == 0:
        return 1
    else: 
        return len(id_clientes) + 1 #al ultimo valor de id_cliente le agrega el siguiente 1, 2, 3, 4, etc

# prueba de preferente para true
"""
def Preferente():
    a = ['True', 'true', "True"]
    b = ['False', 'false', "False"]
    for preferente in Preferente:
        if preferente in Preferente == a:
            return True
        if Preferente in Preferente == b:
            return False  
"""              


#2 - Eliminar Cliente - Preguntar por el ID del cliente y eliminar sus datos de la base de datos.
def eliminar_cliente():
    ingresar = int(input("Ingrese el ID del Cliente que desea eliminar: "))
    id_clientes.pop(ingresar)
    valor_clientes.pop(ingresar)
    print(f"Los ID ingresado ha sido eliminado.\nLista Clientes actualizada\n \nID Clientes: \n \n{id_clientes}\n \nValor Clientes\n \n {valor_clientes}")

# 3 - Mostrar clientes - Preguntar por el ID del cliente y mostrar sus datos
def mostrar_clientes():
    for k, v in id_clientes.items():
        print(f'{k}: {v}')

# 4 - Listar todos los clientes ID / Nombre
def mostrar_cliente_porID():
    consulta = valor_clientes.get(int(input("Ingrese ID de usuario a consultar: ")))
    print(consulta)

# 5 - Clientes Preferentes  #Mostrar la lista de clientes preferentes de la base de datos con su ID y nombre.
def cliente_preferente():
    for n, p in valor_clientes.items():
        if valor_clientes[n]['Preferente'] == True or str == 'True':
            print("Clientes PREFERENTES:\n")
            print(f"\nID Cliente:  {n} \nDatos: {p}")
    
    




# esto lo que hace es decirle a python que ejecute este codigo primero al iniciar el script.
# aca lo digo que primero ejecute la funcion main().
if __name__ == "__main__":
    main()
def dcto_inacap(precio, descuento):
    return precio * descuento

# ####### # FIX A ESTO URGENTE (diccionario no validaba correctamente)
#debe recibir para chequeos:
#la lista de asientos que hay, el que eligieron, todos los asientos, los 3 registros, y los datos ingresados por el cliente

def comprar_pasaje(asientos_disp, asiento_cliente, asientos_gral, regis_nombres, regis_rut, regis_tlf, nomclte, rutclte, telclte,):
    precio = 0
    if asiento_cliente < 31:
        precio = 78900
        print(f"El asiento seleccionado tiene un valor de ${precio}")
    elif asiento_cliente > 31:
        precio = 240000
        print(f"El asiento seleccionado es VIP, y tiene un valor de ${precio}")
    convenio_cliente = input("Pertenece a BancoInacap? (SI / NO): ")
    if convenio_cliente.upper() == "SI":
        total = dcto_inacap(precio, 0.85)
        print(f"Total de compra (incluido descuento BancoInacap): ${total}")
    elif convenio_cliente.upper() == "NO":
        print(f"Total de compra ${precio}")

    cliente_confirma = input("Desea confirmar su compra del vuelo?: (SI / NO)")
    if cliente_confirma.upper() == "SI":
        if str(asiento_cliente) not in asientos_disp:
            for x in range(7):
                for y in range(6):
                    if str(asiento_cliente) == asientos_gral[x][y]:
                        asientos_disp[x,y] = asientos_gral[x,y]
                        asientos_gral[x][y] = "X"
                        regis_nombres.insert(asiento_cliente, nomclte)
                        regis_rut.insert(asiento_cliente, rutclte)
                        regis_tlf.insert(asiento_cliente, telclte)
                        return print("Ha reservado su pasaje exitosamente.")
        elif str(asiento_cliente) in asientos_disp:
            print("Este asiento ya se encuenta reservado. Elija uno que esté libre.")
    else:
        print("Gracias por preferir VuelosInacap.")


def edicion_datos(asiento_cliente, asientos_disp, rutclte, regis_rut, regis_nombres, regis_tlf):
    if str(asiento_cliente) in asientos_disp and rutclte in regis_rut:
        nuevo_nom = input("Ingrese el nuevo nombre a registrar: ")
        regis_nombres[asiento_cliente] = nuevo_nom
        nuevo_telefono = input("Ingrese el nuevo número de teléfono a registrar: ")
        regis_tlf[asiento_cliente] = nuevo_telefono
        print("Sus datos han sido modificados con éxito.")
    else:
        print("""Este asiento aún no ha sido comprado en nuestros registros.
        Por favor, verifique sus datos ingresados.""")


def anulacion(asiento_cliente, asientos_disp, asientos_gral, regis_nom, regis_rut, regis_tlf):
    if str(asiento_cliente)  in asientos_disp:
        for x in range(7):
            for y in range(6):
                if str(asiento_cliente) == asientos_disp[x, y]:
                    asientos_gral[x, y] = asientos_disp[x, y]
                    regis_nom.pop(asiento_cliente)
                    regis_rut.pop(asiento_cliente)
                    regis_tlf.pop(asiento_cliente)
                    print("Datos eliminados con éxito.")
    else:
        print("""ERROR: El pasaje comprado no existe en los registros.
        Favor de verificar los datos ingresados.""")


def muestra_asientos(asientos):
    print("""- Asientos Disponibles -""")
    print(f"""
    |  {asientos[0,0]}   {asientos[0,1]}   {asientos[0,2]}       {asientos[0,3]}   {asientos[0,4]}   {asientos[0,5]}  |
    |			          |
    |  {asientos[1,0]}   {asientos[1,1]}   {asientos[1,2]}      {asientos[1,3]}  {asientos[1,4]}  {asientos[1,5]}  |
    |			          |
    |  {asientos[2,0]}  {asientos[2,1]}  {asientos[2,2]}     {asientos[2,3]}  {asientos[2,4]}  {asientos[2,5]}  |
    |			          |
    |  {asientos[3,0]}  {asientos[3,1]}  {asientos[3,2]}     {asientos[3,3]}  {asientos[3,4]}  {asientos[3,5]}  |
    |			          |
    |  {asientos[4,0]}  {asientos[4,1]}  {asientos[4,2]}     {asientos[4,3]}  {asientos[4,4]}  {asientos[4,5]}  |
    |____________      ___________|		
    |____________      ___________|
    |  {asientos[5,0]}  {asientos[5,1]}  {asientos[5,2]}     {asientos[5,3]}  {asientos[5,4]}  {asientos[5,5]}  |
    |			          |
    |		                  |
    |  {asientos[6,0]}  {asientos[6,1]}  {asientos[6,2]}     {asientos[6,3]}  {asientos[6,4]}  {asientos[6,5]}  |
    """)
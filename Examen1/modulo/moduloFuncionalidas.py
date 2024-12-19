import json
import modulo.menus as menus
import utils.Accion as ctrl
import modulo.funsiones as fdir
import modulo.moduloMesajes as msg


def nuevoCliente ():
    ctrl.borrar_pantalla()
    print('Favor ingresar los siguientes datos: ')
    nombre = input ('Nombres: ')
    apellidos = input('Apellidos: ')
    identificacio = input('Numero de indentificacion: ')
    direccion = input('Direccion : ')
    Telefono = input('Telefono: ')
    ##servicio = input()
    cliente = {
        "nombre" : nombre,
        "apellidos": apellidos,
        "identificacio" : identificacio,
        "direccion": direccion,
        "Telefono": Telefono,
        "servicio": "Sin asignar"


    }
    print = ('Usted a sido registrado correctamente en unos momentos uno de nustros asesores se comunicara con usted')
    numeroUser = fdir.contarUser
    nombreUser = "usuario" + str(numeroUser)

    with open ('./datos.json', 'r+') as abrir:
        baseDatos = json.load(abrir)
        baseDatos['Usuarios'][nombreUser] = cliente
        abrir.seek(0)
        json.dump(baseDatos, abrir, indent=4)
    print(msg.mensajeNuevoUsuario)
    ctrl.borrar_pantalla()

def agregarServicio():
    ctrl.borrar_pantalla()
    print('Favor ingresar el numero de identificacion del usuario que desea agregarle un servicio: ')
    numero = input('-----)   ')
    baseDatos = fdir.abriBase()
    for datoUsuario, Usuarios in baseDatos ['Usuarios'].items():
        if Usuarios['identificacio'] == numero:
            print(menus.menuContra)
            opc = int(input('----)  '))
            match opc:
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    pass
                case 6:
                    pass
                case 7:
                    pass
                case _:
                    break

def validarServicio(id):
    base = fdir.abriBase()
    for datoUsuario, usuario in base["Usuarios"].items():
        if usuario["identificacio"] == id:
            return(usuario["servicio"])

def cambiarEstado (id, nuevoServicio):
    base = fdir.abriBase()
    nuevoServicio = validarServicio(id)
    match nuevoServicio:
        case 'Sin servicios':
            for datoUsuario, usuario in base['Usuarios'].items():
                if usuario['identificacio'] == id:
                    usuario['servicio'] = nuevoServicio
                    fdir.guardarBase(base)
                    break

            


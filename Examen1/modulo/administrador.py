import utils.Accion as ctrl
import modulo.menus as menu
import modulo.moduloFuncionalidas as fdir

def admin ():
    ctrl.borrar_pantalla
    print(menu.menuAdmin)
    opc = int(input('-----)    '))
    while (True):
        match opc:
            case 1:
                fdir.nuevoCliente()
                ctrl.pausar_pantalla()
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
                break
            case _:
                pass

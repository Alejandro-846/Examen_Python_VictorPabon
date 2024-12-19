import modulo.menus as menus
import utils.Accion as ctrl
import modulo.moduloFuncionalidas as fdir
import modulo.administrador as admin
if __name__ == '__main__':

    print(menus.Bienvenida)
    print(menus.menuInicial)

    while (True):
        opc = int(input('--- )  '))
        match opc:
            case 1:
                fdir.nuevoCliente()
                ctrl.pausar_pantalla()
            case 2:
                ctrl.pausar_pantalla()
                pass
            case 3:
                pass
            case 4:
                admin.admin()
            case 5:
                break
            case _:
                break
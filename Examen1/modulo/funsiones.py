import json

def abriBase():
    with open('./datos.json', 'r') as abrir:
        baseDatos = json.load(abrir)
    return (baseDatos)

def guardarBase (base):
    with open('./datos.json', 'w') as abrir:
        json.dump(base, abrir, indent=4)


def contarUser ():
    base = abriBase()
    cantidad = len(base['usuario'])
    return (cantidad)
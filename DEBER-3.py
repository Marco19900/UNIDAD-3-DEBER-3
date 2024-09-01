
# DEBER SISTEMA AVANZADO DE GESTION DE INVENTARIOS
import os
import json

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio:.2f}"

class Inventario:
    def __init__(self, archivo='inventario.json'):
        self.archivo = archivo
        self.productos = {}  # Diccionario para almacenar productos con ID como clave
        self.cargar_inventario()

    def añadir_producto(self, producto):
        if producto.id in self.productos:
            print("Error: El ID del producto ya existe.")
        else:
            self.productos[producto.id] = producto
            print("Producto añadido exitosamente.")
            self.guardar_inventario()

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            print("Producto eliminado exitosamente.")
            self.guardar_inventario()
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            producto = self.productos[id]
            if cantidad is not None:
                producto.cantidad = cantidad
            if precio is not None:
                producto.precio = precio
            print("Producto actualizado exitosamente.")
            self.guardar_inventario()
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto_por_nombre(self, nombre):
        resultados = [producto for producto in self.productos.values() if nombre.lower() in producto.nombre.lower()]
        return resultados

    def mostrar_productos(self):
        if not self.productos:
            print("No hay productos en el inventario.")
        else:
            for producto in self.productos.values():
                print(producto)

    def guardar_inventario(self):
        try:
            with open(self.archivo, 'w') as f:
                productos_dict = {id: vars(producto) for id, producto in self.productos.items()}
                json.dump(productos_dict, f, indent=4)
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error al guardar el inventario: {e}")

    def cargar_inventario(self):
        if not os.path.exists(self.archivo):
            print("Archivo de inventario no encontrado, se creará uno nuevo.")
            return
        try:
            with open(self.archivo, 'r') as f:
                productos_dict = json.load(f)
                self.productos = {id: Producto(**datos) for id, datos in productos_dict.items()}
        except (FileNotFoundError, PermissionError) as e:
            print(f"Error al cargar el inventario: {e}")
        except json.JSONDecodeError as e:
            print(f"Error al procesar el archivo de inventario: {e}")

def menu():
    inventario = Inventario()

    while True:
        print("\n--- Sistema Avanzado de Gestión de Inventario ---")
        print("1. Añadir nuevo producto")
        print("2. Eliminar producto por ID")
        print("3. Actualizar cantidad o precio de un producto")
        print("4. Buscar producto(s) por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == '2':
            id = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == '3':
            id = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad (deje en blanco si no desea cambiarla): ")
            precio = input("Ingrese el nuevo precio (deje en blanco si no desea cambiarlo): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)

        elif opcion == '4':
            nombre = input("Ingrese el nombre del producto a buscar: ")
            resultados = inventario.buscar_producto_por_nombre(nombre)
            if resultados:
                for producto in resultados:
                    print(producto)
            else:
                print("No se encontraron productos con ese nombre.")

        elif opcion == '5':
            inventario.mostrar_productos()

        elif opcion == '6':
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida, por favor seleccione otra opción.")

if __name__ == "__main__":
    menu()
from prettytable import PrettyTable 
#Importamos la libreria para se formen tablas de forma más clara y organizada

class VentasDepartamentos:
    def __init__(self):
        """Inicializa la clase con los datos necesarios."""
        self.meses = 12
        self.departamentos = 3
        self.ventas = [[0] * self.meses for _ in range(self.departamentos)]
        self.nombres_departamentos = ["Ropa", "Deportes", "Juguetería"]
        self.nombres_meses = [
            "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
            "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
        ]

    def ingresar_ventas(self):
        """Permite al usuario ingresar las ventas para cada departamento y mes."""
        for i in range(self.departamentos):
            print(f"Ingresando ventas para el departamento de {self.nombres_departamentos[i]}:")
            for j in range(self.meses):
                self.ventas[i][j] = float(input(f"Ingrese las ventas de {self.nombres_meses[j]}: "))

    def buscar_venta(self, departamento, mes):
        """Busca una venta específica y la devuelve."""
        if 0 <= departamento < self.departamentos and 0 <= mes < self.meses:
            return self.ventas[departamento][mes]
        else:
            print("Error: Departamento o mes no válido.")
            return None

    def eliminar_venta(self, departamento, mes):
        """Elimina una venta específica."""
        if 0 <= departamento < self.departamentos and 0 <= mes < self.meses:
            self.ventas[departamento][mes] = 0
            print("Venta eliminada correctamente.")
            self.mostrar_ventas()  # Muestra las ventas actualizadas después de eliminar
        else:
            print("Error: Departamento o mes no válido.")

    def mostrar_ventas(self):
        """Muestra todas las ventas en una tabla formateada."""
        table = PrettyTable() # Esta línea crea un objeto de tipo PrettyTable para generar tablas de forma fácil y personalizada en la terminal.
        table.field_names = ["Mes"] + self.nombres_departamentos # Esta línea establece los nombres de las columnas de la tabla

        for i, mes in enumerate(self.nombres_meses):
            row = [mes]
            for j in range(self.departamentos):
                row.append(f"${self.ventas[j][i]:.2f}")
            table.add_row(row)

        print(table)

    def obtener_datos_usuario(self, mensaje):
        """Obtiene un número entero positivo del usuario."""
        while True:
            try:
                valor = int(input(mensaje))
                if valor >= 0:
                    return valor
                else:
                    print("Ingrese un valor positivo.")
            except ValueError:
                print("Ingrese un número válido.")

# Ejemplo de uso
ventas = VentasDepartamentos()
ventas.ingresar_ventas()
ventas.mostrar_ventas()

# Buscar una venta
departamento = ventas.obtener_datos_usuario("Ingrese el departamento para buscar(0 = Ropa, 1 = Deportes, 2 = Juguetería): ")
mes = ventas.obtener_datos_usuario("Ingrese el mes (1-12): ") 
venta_encontrada = ventas.buscar_venta(departamento, mes)
if venta_encontrada is not None: # Esta línea de código es una condicional. Lo que hace es verificar si la variable venta_encontrada tiene un valor asignado
    print(f"Venta encontrada: ${venta_encontrada:.2f}")

# Eliminar una venta
departamento = int(input("Eliminar venta (0 = Ropa, 1 = Deportes, 2 = Juguetería): "))
mes = int(input("Ingrese el mes (1-12): ")) 
ventas.eliminar_venta(departamento, mes)
# Al restar 1 al valor ingresado por el usuario, estamos ajustando el valor coincida con el índice de la lista de meses, que comienza en 0
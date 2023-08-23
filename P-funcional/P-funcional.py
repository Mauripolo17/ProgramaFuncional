# Define una clase inmutable para representar empleados
class Empleado:
    def __init__(self, nombre, salario, departamento):
        self.nombre = nombre
        self.salario = salario
        self.departamento = departamento

    def __str__(self):
        return f"{self.nombre}, ${self.salario}, {self.departamento}"

# Lista de empleados
empleados = [
    Empleado("Alice", 50000, "Ventas"),
    Empleado("Bob", 60000, "Desarrollo"),
    Empleado("Carol", 55000, "Desarrollo"),
    Empleado("David", 75000, "Gerencia"),
]

# Función pura para filtrar empleados por salario
def filtrar_por_salario(empleados, salario_minimo):
    return list(filter(lambda emp: emp.salario >= salario_minimo, empleados))


# Filtrar empleados con salario mínimo de $55,000
empleados_filtrados = filtrar_por_salario(empleados, 55000)
print("Empleados con salario mayor o igual a $55,000:")
print("\n".join(map(str, empleados_filtrados)))


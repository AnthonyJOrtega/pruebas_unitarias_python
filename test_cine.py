import pytest
from cine import Pelicula
# Compra de entradas con asientos suficientes.

def test_compra_exitosa():
    pelicula = Pelicula("Peli prueba", 10, 8)
    resultado = pelicula.vender_entradas(5)
    assert resultado == "Has comprado 5 entradas para Peli prueba. Total: $40"

# Compra de entradas con asientos insuficientes.

def test_compra_asientos_insuficientes():
    pelicula = Pelicula("Peli prueba", 3, 8)
    resultado = pelicula.vender_entradas(5)
    assert resultado == "No hay suficientes asientos disponibles. Solo quedan 3 asientos."

# Compra de cero entradas.

def test_compra_cero_entradas():
    pelicula = Pelicula("Peli prueba", 10, 8)
    resultado = pelicula.vender_entradas(0)
    assert resultado == "Has comprado 0 entradas para Peli prueba. Total: $0"



if __name__ == "__main__":
    pytest.main()

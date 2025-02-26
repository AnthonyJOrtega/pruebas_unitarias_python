import pytest
from biblioteca import Libro, Biblioteca

# Prueba Libro
def test_libro_atributos():
    libro = Libro("DI", "Anthony", 1999)
    assert libro.titulo == "DI"
    assert libro.autor == "Anthony"
    assert libro.anio == 1999
    assert libro.prestado == False

def test_libro_estado():
    libro = Libro("DI", "Anthony", 1999)
    assert str(libro) == "DI de Anthony (1999) - disponible"
    libro.prestado = True
    assert str(libro) == "DI de Anthony (1999) - prestado"

# Prueba Biblioteca
def test_agregar_libro():
    biblioteca = Biblioteca()
    libro = Libro("DI", "Anthony", 1999)
    biblioteca.agregar_libro(libro)
    assert len(biblioteca.libros) == 1
    assert biblioteca.libros[0].titulo == "DI"

def test_eliminar_libro():
    biblioteca = Biblioteca()
    libro = Libro("DI", "Anthony", 1999)
    biblioteca.agregar_libro(libro)
    biblioteca.eliminar_libro("DI")
    assert len(biblioteca.libros) == 0

def test_eliminar_libro_no_existente():
    biblioteca = Biblioteca()
    libro = Libro("DI", "Anthony", 1999)
    biblioteca.agregar_libro(libro)
    biblioteca.eliminar_libro("libro_pruebae")
    assert len(biblioteca.libros) == 1

def test_buscar_libro():
    biblioteca = Biblioteca()
    libro = Libro("DI", "Anthony", 1999)
    biblioteca.agregar_libro(libro)
    assert biblioteca.buscar_libro("DI") == libro

def test_buscar_libro_no_existente():
    biblioteca = Biblioteca()
    assert biblioteca.buscar_libro("libro_pruebae") is None

def test_listar_libros():
    biblioteca = Biblioteca()
    libro = Libro("DI", "Anthony", 1999)
    biblioteca.agregar_libro(libro)
    assert biblioteca.listar_libros() == ["DI de Anthony (1999) - disponible"]

def test_prestar_libro():
    biblioteca = Biblioteca()
    libro = Libro("DI", "Anthony", 1999)
    biblioteca.agregar_libro(libro)
    assert biblioteca.prestar_libro("DI") == "Has pedido prestado el libro 'DI'."

def test_prestar_libro_ya_prestado():
    biblioteca = Biblioteca()
    libro = Libro("DI", "Anthony", 1999)
    biblioteca.agregar_libro(libro)
    biblioteca.prestar_libro("DI")
    assert biblioteca.prestar_libro("DI") == "El libro 'DI' ya está prestado."

def test_prestar_libro_no_existente():
    biblioteca = Biblioteca()
    assert biblioteca.prestar_libro("libro_pruebae") == "El libro 'libro_pruebae' no se encuentra en la biblioteca."

def test_devolver_libro():
    biblioteca = Biblioteca()
    libro = Libro("DI", "Anthony", 1999)
    biblioteca.agregar_libro(libro)
    biblioteca.prestar_libro("DI")
    assert biblioteca.devolver_libro("DI") == "Has devuelto el libro 'DI'."

def test_devolver_libro_no_prestado():
    biblioteca = Biblioteca()
    libro = Libro("DI", "Anthony", 1999)
    biblioteca.agregar_libro(libro)
    assert biblioteca.devolver_libro("DI") == "El libro 'DI' no estaba prestado."

def test_devolver_libro_no_existente():
    biblioteca = Biblioteca()
    assert biblioteca.devolver_libro("libro_pruebae") == "El libro 'libro_pruebae' no se encuentra en la biblioteca."

if __name__ == "__main__":
    pytest.main()

# IMPORTANT: The length of the lists has to be the same

# List of lists, where each of the inner lists has all the inputs for a single test
input_values = [
    # Test case 1
    (
    ["3","gato", "perro", "jabali", "ardilla", "perro", "oso"],
    ["Cuántas palabras por lista:",">>> ", ">>> ", ">>> ", "['gato', 'perro', 'jabali']",
    ">>> ", ">>> ", ">>> ", "['ardilla', 'perro', 'oso']", "['perro']"],
    ["La salida no cumple con el caso de prueba."]
    ),
    # Test case 2
    (
     ["2","gato", "perro", "jabali", "ardilla"],
    ["Cuántas palabras por lista:",">>> ", ">>> ", "['gato', 'perro']",
    ">>> ", ">>> ", "['jabali','ardilla']", "[]"],
    ["La salida no cumple con el caso de prueba."]
    )
    ]

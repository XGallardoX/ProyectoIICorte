import sys  
from lexer import lex  

# Función para escribir los tokens generados en un archivo de salida.
def write_tokens_to_file(tokens, output_file):
    # Abrimos el archivo de salida en modo escritura ('w'), que sobreescribe el archivo si ya existe.
    with open(output_file, 'w') as f:
        # Recorremos la lista de tokens generados.
        for token in tokens:
            # Si el token tiene 3 elementos (tipo, lexema, número de línea), escribimos el token en el archivo.
            if len(token) == 3:
                f.write(f'<{token[0]},{token[1]},{token[2]}>\n')
            # Si el token tiene 4 elementos (tipo, lexema, número de línea, número de columna), también lo escribimos.
            else:
                f.write(f'<{token[0]},{token[1]},{token[2]},{token[3]}>\n')

# Función principal del programa, encargada de orquestar la ejecución.
def main():
    # Comprobamos si el número de argumentos recibidos es diferente de 3 
    if len(sys.argv) != 3:
        # Si no hay 3 argumentos, mostramos un mensaje de uso correcto y salimos del programa.
        print("Uso: python main.py <archivo_entrada> <archivo_salida>")
        sys.exit(1)  # Terminamos la ejecución con un código de error.

    # Asignamos el primer argumento como el archivo de entrada.
    input_file = sys.argv[1]
    # Asignamos el segundo argumento como el archivo de salida.
    output_file = sys.argv[2]

    # Llamamos a la función 'lex' para realizar el análisis léxico del archivo de entrada y obtener los tokens.
    tokens = lex(input_file)

    # Abrimos el archivo de salida en modo escritura ('w').
    with open(output_file, 'w') as f:
        # Si la lista de tokens no está vacía, escribimos los tokens en el archivo de salida.
        if tokens:
            write_tokens_to_file(tokens, output_file)
        # Si la lista está vacía (por ejemplo, el archivo de entrada solo tiene comentarios), no hacemos nada (pasamos).
        else:
            pass  # No hacemos nada si no hay tokens para escribir.

# Verificamos si el archivo se está ejecutando directamente como un script principal.
if __name__ == "__main__":
    main()  

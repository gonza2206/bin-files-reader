# Name of the binary file to read
binary_file = 'C:\\Users\\Urano\\Documents\\GitHub\\bin-files-reader\\RFGW_1.0.3.bin'

# Function to convert a value to hexadecimal format with '0x'
def to_hex(value):
    return f'0x{value:02X}'

# Read the binary file and convert the bytes to hexadecimal format
with open(binary_file, 'rb') as file:
    binary_bytes = file.read()
    hex_values = [to_hex(byte) for byte in binary_bytes]

    # Track the current reading pointer position
    current_position = file.tell()

    # Get the total length of the file
    file_length = len(binary_bytes)

    # Check if we are at the last position of the file
    is_last_position = current_position == file_length

    # Format the hexadecimal array
    if is_last_position:
        result = ', '.join(hex_values)
    else:
        result = '};'.join(hex_values)

# Guardar el resultado en un archivo C++
output_file = 'C:\\Users\\Urano\\Documents\\GitHub\\bin-files-reader\\UpgradeRFProgram.h'  # Reemplaza 'ruta_a_tu_archivo.cpp' con la ruta de tu archivo C++

# Lee el contenido actual del archivo .h
with open(output_file, 'r') as cpp_file:
    existing_lines = cpp_file.readlines()

# Abre el archivo en modo escritura para reemplazar su contenido
with open(output_file, 'w') as cpp_file:
    updated_lines = []

    for line in existing_lines:
        if "static constexpr const uint8_t code[] = {0};" in line:
            updated_lines.append(f'  static constexpr const uint8_t code[] = {{{result}}};\n')
        else:    
            updated_lines.append(line)

    cpp_file.writelines(updated_lines)
    
print(f'El valor de la variable "result" se ha guardado en {output_file}')
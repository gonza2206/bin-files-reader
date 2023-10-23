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
template_file = 'C:\\Users\\Urano\\Documents\\GitHub\\bin-files-reader\\UpgradeRFProgram.h'  # Reemplaza 'ruta_a_tu_archivo.cpp' con la ruta de tu archivo C++

# Nombre del archivo de destino
new_file = 'C:\\Users\\Urano\\Documents\\GitHub\\bin-files-reader\\UpdateProgram.h'

# Copiar el contenido de la plantilla a un nuevo archivo y reemplazar el valor de 'result'
with open(template_file, 'r') as template, open(new_file, 'w') as new:
    template_content = template.read()
    new_content = template_content.replace('static constexpr const uint8_t code[] = {0};', f'static constexpr const uint8_t code[] = {{{result}}};')
    new.write(new_content)

print(f'Se ha creado un nuevo archivo en {new_file} con el valor reemplazado.')
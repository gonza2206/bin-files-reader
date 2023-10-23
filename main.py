# Name of the binary file to read
binary_file = 'C:\\Users\\Urano\\Documents\\GitHub\\bin-files-reader\\RFGW_1.0.3.bin'

# Save the result to a C++ file
template_file = 'C:\\Users\\Urano\\Documents\\GitHub\\bin-files-reader\\UpgradeRFProgram.h'

# Name of the destination file
new_file = 'C:\\Users\\Urano\\Documents\\GitHub\\bin-files-reader\\UpdateProgram.h'

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

# Check if the new file exists and delete it.
if os.path.exists(new_file):
    os.remove(new_file)

# Copy the content from the template file to a new file and replace the value of 'result'
with open(template_file, 'r') as template, open(new_file, 'w') as new:
    template_content = template.read()
    new_content = template_content.replace('static constexpr const uint8_t code[] = {0};', f'static constexpr const uint8_t code[] = {{{result}}};')
    new.write(new_content)

print(f'A new file has been created at {new_file} with the replaced value.')

# Automatize RF Update program. in CMAKE
################################################################################

# add_custom_target(RF_UPDATE
#         COMMAND ${Python3_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/RFUpgrade.py
#         WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
#         COMMENT "Running RF Upgrade Script"
# )
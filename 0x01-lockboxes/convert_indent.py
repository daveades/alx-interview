import sys

def convert_indent(file_path, old_spaces=8, new_spaces=4):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Replace all leading multiples of old_spaces with new_spaces
        updated_lines = []
        for line in lines:
            leading_space_count = len(line) - len(line.lstrip())  # Count leading spaces
            if leading_space_count > 0:
                # Calculate the number of new spaces
                new_indent_level = (leading_space_count // old_spaces) * new_spaces
                new_indent = ' ' * new_indent_level
                updated_lines.append(new_indent + line.lstrip())
            else:
                updated_lines.append(line)  # No changes for lines with no leading spaces

        # Write the changes back to the file
        with open(file_path, 'w') as file:
            file.writelines(updated_lines)

        print(f"Indentation converted from {old_spaces} spaces to {new_spaces} spaces in {file_path}.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 convert_indent.py <file_path>")
    else:
        file_path = sys.argv[1]
        convert_indent(file_path)


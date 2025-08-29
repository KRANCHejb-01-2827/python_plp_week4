def read_and_modify_file(input_file, output_file):
    try:
        # Open the input file for reading
        with open(input_file, "r") as file:
            content = file.read()

        # Modify the content (convert to uppercase)
        modified_content = content.upper()

        # Write the modified content to a new file
        with open(output_file, "w") as file:
            file.write(modified_content)

        print(f"✅ File processed successfully! Output saved in '{output_file}'")

    except FileNotFoundError:
        print(f"❌ Error: The file '{input_file}' does not exist.")
    except PermissionError:
        print(f"❌ Error: You don’t have permission to read/write the file.")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")


# Main program
if __name__ == "__main__":
    # Ask user for input filename
    filename = input("Enter the filename to read: ")

    # Call function with error handling
    read_and_modify_file(filename, "output.txt")

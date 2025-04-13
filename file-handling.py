def modify_content(content):
    """
    Modify the file content.
    In this demo, the content is simply converted to uppercase.
    Customize this function as per the assignment requirements.
    """
    return content.upper()  # Modify as needed

def main():
    # Ask the user for the filename to be processed.
    file_name = input("Enter the filename to read: ")

    # Attempt to open and read the file.
    try:
        with open(file_name, 'r') as infile:
            data = infile.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist. Please check the filename and try again.")
        return  # Stop further processing since the file wasn't found.
    except IOError:
        print(f"Error: Could not read the file '{file_name}'. Ensure it is accessible and try again.")
        return

    # Process the file content.
    modified_data = modify_content(data)

    # Define a new filename for the modified content.
    output_file = "modified_" + file_name

    # Attempt to write the modified content to the new file.
    try:
        with open(output_file, 'w') as outfile:
            outfile.write(modified_data)
        print(f"Success: Modified content written to '{output_file}'.")
    except IOError:
        print(f"Error: Could not write to the file '{output_file}'. Please try again with a different name or check your permissions.")
        return

if __name__ == '__main__':
    main()

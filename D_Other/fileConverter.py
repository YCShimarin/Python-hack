import os
import shutil

def convert_extension(input_dir, input_ext, output_ext):
    # Create output directory if it doesn't exist
    output_dir = os.path.join(input_dir, output_ext.lstrip('.'))
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    # List all files in the input directory with the input extension
    for filename in os.listdir(input_dir):
        if filename.endswith(input_ext):
            # Get basename and directory name
            basename = os.path.splitext(filename)[0]
            dirname = os.path.dirname(os.path.abspath(os.path.join(input_dir, filename)))
            
            # Move the file to the output directory with the new extension
            shutil.move(os.path.join(dirname, filename), os.path.join(output_dir, basename + output_ext))

# Get user input for the input directory, input file extension, and output file extension
input_dir = input("Enter the input directory: ")
input_ext = input("Enter the input file extension (with the dot): ")
output_ext = input("Enter the output file extension (with the dot): ")

# Call the convert_extension function with the user input
convert_extension(input_dir, input_ext, output_ext)

print("Done!")

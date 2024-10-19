import os
import math
import argparse

def split_text_file(input_file, num_parts):
    # Read the entire file
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Calculate the size of each part
    total_size = len(content)
    part_size = math.ceil(total_size / num_parts)

    # Split the content and write to separate files
    for i in range(num_parts):
        start = i * part_size
        end = min((i + 1) * part_size, total_size)
        part_content = content[start:end]

        # Create output filename
        base_name, ext = os.path.splitext(input_file)
        output_file = f"{base_name}_part{i+1}{ext}"

        # Write the part to a new file
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(part_content)

    print(f"Split {input_file} into {num_parts} parts.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split a text file into n parts.")
    parser.add_argument("input_file", help="Path to the input text file")
    parser.add_argument("num_parts", type=int, help="Number of parts to split the file into")
    
    args = parser.parse_args()
    
    split_text_file(args.input_file, args.num_parts)


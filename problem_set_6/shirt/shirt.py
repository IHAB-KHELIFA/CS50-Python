import sys
import os
from PIL import Image, ImageOps

def main():
    # Check command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python shirt.py input_file output_file")

    # Get input and output filenames
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Check file extensions
    input_ext = os.path.splitext(input_file)[1].lower()
    output_ext = os.path.splitext(output_file)[1].lower()

    # Validate extensions
    valid_extensions = {".jpg", ".jpeg", ".png"}
    if input_ext not in valid_extensions:
        sys.exit("Input file must be .jpg, .jpeg, or .png")
    if output_ext not in valid_extensions:
        sys.exit("Output file must be .jpg, .jpeg, or .png")
    if input_ext != output_ext:
        sys.exit("Input and output must have the same extension")

    try:
        # Open the input image
        input_image = Image.open(input_file)
    except FileNotFoundError:
        sys.exit(f"Input file {input_file} does not exist")

    # Open the shirt image
    shirt = Image.open("shirt.png")
    size = shirt.size

    # Resize and crop input image to match shirt size
    output = ImageOps.fit(input_image, size)

    # Paste the shirt onto the processed input image
    output.paste(shirt, shirt)

    # Save the result
    output.save(output_file)

if __name__ == "__main__":
    main()

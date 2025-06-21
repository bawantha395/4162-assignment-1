import cv2
import numpy as np
import matplotlib.pyplot as plt

def reduce_intensity_levels(image_path, k):
    """
    Reduces the number of intensity levels in a grayscale image
    """
    image_path= 'orginal_dog.png'
    # Load the image in grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"Error: Could not load image from {image_path}")
        return

    # Validate 
    if not (k > 0 and (k & (k - 1) == 0)):
        print(f"Error: Desired number of intensity levels ({k}) must be a positive integer power of 2.")
        return

    # Calculate the factor to quantize the intensity levels
    levels_factor = 256 // k
    
    # Apply the reduction:
    img_reduced = (img // levels_factor) * levels_factor

    # Display original and reduced images 
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Original Image (256 Levels)')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(img_reduced, cmap='gray')
    plt.title(f'Reduced to {k} Levels')
    plt.axis('off')

    plt.show()

    # Save the processed image
    output_filename = f"output_intensity_reduced_to_{k}_levels.jpg"
    cv2.imwrite(output_filename, img_reduced)
    print(f"Processed image saved as {output_filename}")


if __name__ == "__main__":
    image_path_input = 'orginal_dog.png' 

    print("Q1: Reduce Number of Intensity Levels ---")
    try:
        num_levels_input = int(input("Enter the desired number of intensity levels (integer power of 2): "))
        reduce_intensity_levels(image_path_input, num_levels_input)
    except ValueError:
        print("Invalid input. Please enter an integer.")
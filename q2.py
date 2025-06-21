import cv2
import numpy as np
import matplotlib.pyplot as plt

def spatial_average_filter(image_path, kernel_sizes):
    """
    Applies spatial average filter with different kernel sizes.
    """
    image_path='orginal_dog.png'
    # Load the image in grayscale 
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"Error: Could not load image from {image_path}")
        return

    #  display original and processed images
    plt.figure(figsize=(15, 5))
    plt.subplot(1, len(kernel_sizes) + 1, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')

    # Apply average filter for each specified kernel size
    for i, kernel_size in enumerate(kernel_sizes):
        # cv2.blur performs a normalized box filter 
        img_blurred = cv2.blur(img, kernel_size)

        plt.subplot(1, len(kernel_sizes) + 1, i + 2)
        plt.imshow(img_blurred, cmap='gray')
        plt.title(f'Blurred with {kernel_size[0]}x{kernel_size[1]} Kernel')
        plt.axis('off')
        
        # Save the processed image
        output_filename = f"output_blurred_{kernel_size[0]}x{kernel_size[1]}.jpg"
        cv2.imwrite(output_filename, img_blurred)
        print(f"Processed image saved as {output_filename}")

    plt.tight_layout() # Adjust layout to prevent overlap
    plt.show()


if __name__ == "__main__":
    image_path_input = 'orginal_dog.png' 

    print("\n--- Problem 2: Spatial Average Filtering ---")
    # Define the kernel sizes as requested
    kernel_sizes_to_apply = [(3, 3), (10, 10), (20, 20)] # 
    spatial_average_filter(image_path_input, kernel_sizes_to_apply)
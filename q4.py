import cv2
import numpy as np
import matplotlib.pyplot as plt

def reduce_spatial_resolution(image_path, block_sizes):
    """
    Reduces the spatial resolution of an image by replacing non-overlapping
    blocks of pixels with their average value.
    """
    image_path = 'orginal_dog.png'  

    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"Error: Could not load image from {image_path}")
        return

    plt.figure(figsize=(15, 7))
    plt.subplot(1, len(block_sizes) + 1, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')

    h, w = img.shape # Get image height and width

    for i, block_size in enumerate(block_sizes):
        # Create a copy of the image to modify, and convert to float for accurate averaging
        img_reduced_res = np.copy(img).astype(np.float32) 
        
      
        for y in range(0, h, block_size):
            for x in range(0, w, block_size):
                current_block = img_reduced_res[y : min(y + block_size, h), 
                                                x : min(x + block_size, w)]
                
                # Calculate the average of pixels in the current block
                average_value = np.mean(current_block)
                
                # Replace all pixels in the block with the calculated average value
                img_reduced_res[y : min(y + block_size, h), 
                                 x : min(x + block_size, w)] = average_value
        
        img_reduced_res = img_reduced_res.astype(np.uint8)

        plt.subplot(1, len(block_sizes) + 1, i + 2)
        plt.imshow(img_reduced_res, cmap='gray')
        plt.title(f'Resolution Reduced with {block_size}x{block_size} Blocks')
        plt.axis('off')
        
        # Save the processed image
        output_filename = f"output_res_reduced_{block_size}x{block_size}.jpg"
        cv2.imwrite(output_filename, img_reduced_res)
        print(f"Processed image saved as {output_filename}")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    image_path_input = 'orginal_dog.png' 

    print("\n--- Problem 4: Reduce Image Spatial Resolution ---")
    block_sizes_to_apply = [3, 5, 7] # 
    reduce_spatial_resolution(image_path_input, block_sizes_to_apply)
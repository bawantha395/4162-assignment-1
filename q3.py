import cv2
import numpy as np
import matplotlib.pyplot as plt

def rotate_image(image_path, angles):
    """
    Rotates an image by specified angles.
    """
    image_path = 'orginal_dog.png' 
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Could not load image from {image_path}")
        return

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    plt.figure(figsize=(15, 7))
    plt.subplot(1, len(angles) + 1, 1)
    plt.imshow(img_rgb)
    plt.title('Original Image')
    plt.axis('off')

    h, w = img.shape[:2] # Get image height and width

    for i, angle in enumerate(angles):
        img_rotated = None

        if angle == 90:
            # For 90 degrees, cv2.
            img_rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
            print(f"Rotated by {angle} degrees using cv2.rotate.")
        elif angle == 45:
            
            center = (w / 2, h / 2) # Rotation center
            
            # Get the 2x3 rotation matrix. 1.0 is the scale factor.
            M = cv2.getRotationMatrix2D(center, angle, 1.0)

            cos = np.abs(M[0, 0])
            sin = np.abs(M[0, 1])
            nW = int((h * sin) + (w * cos)) # New width
            nH = int((h * cos) + (w * sin)) # New height

            # Adjust the rotation matrix to translate the image so it fits in the new dimensions
            M[0, 2] += (nW / 2) - center[0]
            M[1, 2] += (nH / 2) - center[1]

            img_rotated = cv2.warpAffine(img, M, (nW, nH))
            print(f"Rotated by {angle} degrees using warpAffine.")
        else:
            print(f"Rotation for {angle} degrees not specifically implemented in this example. Skipping.")
            continue # Skip to the next angle

        if img_rotated is not None:
            # Convert to RGB for matplotlib display
            img_rotated_rgb = cv2.cvtColor(img_rotated, cv2.COLOR_BGR2RGB)
            
            plt.subplot(1, len(angles) + 1, i + 2)
            plt.imshow(img_rotated_rgb)
            plt.title(f'Rotated by {angle} Degrees')
            plt.axis('off')
            
            # Save the processed image
            output_filename = f"output_rotated_{angle}_degrees.jpg"
            cv2.imwrite(output_filename, img_rotated)
            print(f"Processed image saved as {output_filename}")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    image_path_input = 'orginal_dog.png' 

    print("\n--- Problem 3: Image Rotation ---")
    rotate_image(image_path_input, [45, 90]) 
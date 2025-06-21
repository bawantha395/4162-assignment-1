# EC7212 – Computer Vision and Image Processing

## Take Home Assignment 1 Scripts

This repository contains Python scripts for basic image processing operations:

- `q1.py`: Reduce the number of intensity levels in an image.
- `q2.py`: Apply mean (average) filtering with different neighborhood sizes.
- `q3.py`: Rotate an image by 45 and 90 degrees.
- `q4.py`: Block-wise averaging to simulate spatial resolution reduction.

## Requirements

- Python 3.x
- OpenCV (`opencv-python`)
- NumPy
- Matplotlib

### Recommended: Use a Python Virtual Environment
To avoid system conflicts, create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
pip install opencv-python numpy matplotlib
```

## Usage

### 1. Reduce Intensity Levels

```bash
python3 q1.py orginal_dog.png 2
```
- `<image_path>`: Path to the input image (e.g., `orginal_dog.png`).
- `<num_levels>`: Desired number of intensity levels (must be a power of 2, e.g., 2, 4, 8, ..., 256).
- **Output:** `output_intensity_reduced_to_4_levels.png` (or similar, depending on the number of levels)

### 2. Mean Filtering

```bash
python3 q2.py orginal_dog.png
```
- Applies 3x3, 10x10, and 20x20 mean filters to the image.
- **Output:**
  - `output_blurred_3x3.jpg`
  - `output_blurred_10x10.jpg`
  - `output_blurred_20x20.jpg`

### 3. Rotate Image

```bash
python3 q3.py orginal_dog.png
```
- Rotates the image by 45 and 90 degrees.
- **Output:**
  - `output_rotated_45_degrees.jpg`
  - `output_rotated_90_degrees.jpg`

### 4. Block-wise Averaging

```bash
python3 q4.py orginal_dog.png
```
- For every non-overlapping 3x3, 5x5, and 7x7 block, replaces all pixels in the block with their average.
- **Output:**
  - `output_res_reduced_3x3.jpg`
  - `output_res_reduced_5x5.jpg`
  - `output_res_reduced_7x7.jpg`

## Notes
- The scripts require a valid image file as input. The image `orginal_dog.png` was used for testing and demonstration.
- All output images will be saved in the current directory.

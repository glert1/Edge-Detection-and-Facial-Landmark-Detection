# Edge Detection and Facial Landmark Detection

This repository contains two Python scripts for computer vision tasks:

1. **Edge Detection (`edge_detection.py`)**: Implements various edge detection techniques using OpenCV.
2. **Facial Landmark Detection (`lanmarkdlib.py`)**: Uses dlib's facial landmark detector to identify facial features.

## Requirements

Before running the scripts, install the required dependencies:

```bash
pip install numpy opencv-python matplotlib dlib
```

Additionally, download the dlib face landmark model:

- [shape_predictor_68_face_landmarks.dat](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2) (Extract the file in the same directory as the script.)

## Usage

### Edge Detection

This script reads an image and applies different edge detection techniques:
- Canny Edge Detection
- Laplacian Edge Detection
- Sobel Edge Detection

#### Run the script:
```bash
python edge_detection.py
```

Modify the image path in the script before running:
```python
img = cv.imread('/your image path', cv.IMREAD_GRAYSCALE)
```

### Facial Landmark Detection

This script detects facial landmarks on an image using dlib's 68-point facial landmark predictor.

#### Run the script:
```bash
python lanmarkdlib.py
```

Modify the image path in the script before running:
```python
image = cv2.imread('/your image path')
```

## Output
- `edge_detection.py` displays the original image alongside its edge-detected versions.
- `lanmarkdlib.py` marks facial landmarks on a given image and displays it.

## License
This project is licensed under the MIT License.


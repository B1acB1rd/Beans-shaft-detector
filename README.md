# Beans Shaft Detector

This project uses a YOLO-based deep learning model to detect defects or features in beans shafts from images. It leverages the [Ultralytics YOLO](https://github.com/ultralytics/ultralytics) library for object detection.

## Project Structure

- Beans_detector.pt — Trained YOLO model weights.
- test.py — Script to run inference on sample images.
- TestImg.jpg — Example input image for testing.
- RESULTS — Contains evaluation metrics, plots, and results:
  - Precision, Recall, F1 curves (`BoxP_curve.png`, `BoxR_curve.png`, `BoxF1_curve.png`, `BoxPR_curve.png`)
  - Confusion matrices (`confusion_matrix.png`, `confusion_matrix_normalized.png`)
  - Label visualizations (`labels.jpg`, `labels_correlogram.jpg`)
  - `results.csv` — Detailed results and metrics.
  - `results.png` — Summary plot.

## Getting Started

### Requirements

- Python 3.8+
- [Ultralytics YOLO](https://docs.ultralytics.com/)
- Other dependencies as required by YOLO (see [Ultralytics installation guide](https://docs.ultralytics.com/quickstart/))

### Installation

1. Install Python and pip.
2. Install Ultralytics YOLO:
   ```powershell
   pip install ultralytics
   ```

### Usage

1. Place your test image in the project directory (e.g., TestImg.jpg).
2. Run the inference script:
   ```powershell
   python test.py
   ```
   This will load the model, run detection on the image, and display results.

### Training

If you wish to retrain the model, use the TRAIN.PY script. Make sure to prepare your dataset according to YOLO format.

## Results

Evaluation metrics and visualizations are available in the RESULTS folder. These include precision-recall curves, confusion matrices, and label distributions.


## Acknowledgments

- [Ultralytics YOLO](https://github.com/ultralytics/ultralytics)
  @misc{
    beans-dirt-detector-tpv8v_dataset,
    title = { Beans Dirt Detector Dataset },
    type = { Open Source Dataset },
    author = { B1acB1rd },
    howpublished = { \url{ https://universe.roboflow.com/b1acb1rd/beans-dirt-detector-tpv8v } },
    url = { https://universe.roboflow.com/b1acb1rd/beans-dirt-detector-tpv8v },
    journal = { Roboflow Universe },
    publisher = { Roboflow },
    year = { 2025 },
    month = { sep },
    note = { visited on 2025-09-18 },
  }

---



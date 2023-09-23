# Train object segmentation with Yolov8

<img src="yolo.png">

## Introduction

YOLOv8 is a state-of-the-art object detection algorithm known for its high accuracy and real-time performance. It's particularly effective when it comes to instance segmentation, which involves identifying and delineating individual objects within an image. YOLOv8 provides precise bounding boxes and accurate masks, making it an excellent choice for tasks that require pixel-level analysis.

## Get started

In this project, we use [COCO dataset](http://deltalab.iitk.ac.in/index.php?n=Main.MSCOCO2014Dataset) to train object segmentation for only person class.

## Installation

1. Clone repo

   ```bash
   https://github.com/shoxa0707/Object-Segmentation.git
   cd Object-Segmentation
   ```

2. Install dependent packages

   ```bash
   pip install -r requirements.txt
   ```

After installation done. The project is ready to launch:

```bash
python test.py
```

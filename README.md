# Counts & Detection Cars In Road

## Project Overview

The "Counts & Detection Cars In Roada" project is designed to detect, track, and count cars in a video stream using the YOLOv8 object detection model and OpenCV. The system processes the video in real-time, detecting vehicles as they appear, tracking their movement across the frame, and counting them when they pass specific lines on the road. This tool is particularly useful for traffic management systems and smart city applications.

## Key Features

- **YOLOv8 Object Detection:** Uses the YOLOv8 model to accurately detect cars in the video feed.
- **Real-Time Vehicle Tracking:** Implements a custom tracking mechanism to follow vehicles as they move through the frame.
- **Vehicle Counting:** Tracks and counts vehicles as they cross predefined red and blue lines, indicating their direction of movement (up or down).

## How It Works

1. **Video Input:** The system reads a video file and processes it frame by frame.
2. **Object Detection:** YOLOv8 is used to detect cars in each frame.
3. **Vehicle Tracking:** A tracking algorithm ensures that detected vehicles are consistently identified as they move through the frame.
4. **Counting Vehicles:** The system counts vehicles as they cross a red or blue line drawn across the video. The direction of the vehicle (up or down) is determined by which line is crossed.

## Code Description

### Libraries Used

- **OpenCV:** For video capture, image processing, and drawing on the frames.
- **Pandas:** For handling the output data from YOLOv8.
- **YOLOv8:** A state-of-the-art object detection model used to detect vehicles.
- **tracker.py:** A custom tracking script that ensures vehicles are accurately tracked across frames.

### Main Code

The project involves:
- Initializing the YOLOv8 model and reading the video feed.
- Detecting cars in each frame using YOLOv8.
- Tracking the detected vehicles to maintain their identity across frames.
- Counting vehicles as they cross predefined red and blue lines, which represent the boundaries for counting vehicles moving up or down.

### Installation

To run this project, ensure you have the following dependencies installed:
```bash
pip install opencv-python pandas ultralytics
```

### Usage

1. Clone the repository to your local machine.
2. Ensure the video path is correctly set in the script.
3. Run the script using Python:

```bash
python detect_track_count.py
```

### Results

The system displays the processed video feed with detected vehicles marked by bounding boxes and their unique IDs. The total count of vehicles going up and down is shown in real-time.

## Conclusion

The "Counts & Detection Cars In Road" project demonstrates the effectiveness of combining cutting-edge object detection models like YOLOv8 with custom tracking and counting logic. This system is a valuable tool for traffic management and monitoring applications, offering real-time insights into vehicle movement and counts.
---

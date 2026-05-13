# 안면인식 도어락

# Face Recognition Door Lock System

## Overview
This project is a prototype door lock system using face recognition.  
It uses OpenCV to detect and recognize faces from a camera, then triggers a solenoid lock when the recognition confidence meets the configured threshold.

## Features
- Camera connection test
- Face detection using OpenCV
- Face image dataset collection by user ID
- Face recognition model training
- Real-time face recognition
- Solenoid door lock control
- Event-based action support

## Tech Stack
- Python
- OpenCV
- Pillow
- Raspberry Pi 3B+
- ASUS Tinker Board
- Jetson Nano

## Project Structure

```text
FacialRecognitionProject/
├── dataset/      # Stores captured face images by user ID
├── trainer/      # Stores trained recognition model data
├── cam_test_webcam.py
├── face_filter.py
├── ID_face_pic.py
├── train_img.py
├── OPR_faceid.py
└── testfaceAD.py


| File                 | Description                                                               |
| -------------------- | ------------------------------------------------------------------------- |
| `cam_test_webcam.py` | Tests whether the camera is connected and working properly                |
| `face_filter.py`     | Detects faces from camera input                                           |
| `ID_face_pic.py`     | Captures face images with a user ID and stores them in the dataset folder |
| `train_img.py`       | Trains the face recognition model using collected face images             |
| `OPR_faceid.py`      | Performs real-time face recognition and controls the solenoid door lock   |
| `testfaceAD.py`      | Alternative version for triggering a custom event after recognition       |


pip install opencv-python
pip install pillow

How to Use
1. Test the camera
python cam_test_webcam.py
2. Check face detection
python face_filter.py
3. Capture face images
python ID_face_pic.py
4. Train the recognition model
python train_img.py
5. Run the face recognition door lock system
python OPR_faceid.py
Recognition Threshold

The recognition condition can be adjusted in OPR_faceid.py.

if (100 - confidence) > 40:

In the current setting, the system triggers the door lock control when the recognition score is over 40 percent.
This threshold can be modified depending on the required security level and recognition accuracy.

Supported Environment
Raspberry Pi 3B+
ASUS Tinker Board
Jetson Nano

Note: Jetson Nano may require additional environment configuration.

Project Purpose

This project was created to understand how computer vision can be applied to embedded systems.
Through this project, I practiced camera control, face recognition, dataset collection, model training, and hardware control using Python and OpenCV.

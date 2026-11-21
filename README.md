# Construction-PPE-Detection.
example project
# 🦺 Smart Construction PPE Detection

A computer vision project that uses **YOLOv8** to detect Personal Protective Equipment (PPE) on construction sites. The system identifies workers, helmets, safety vests, and potential PPE violations through an interactive Streamlit web application.

## 🚀 Live Application

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](YOUR_STREAMLIT_APP_LINK)

**Live Demo:** [Click here to open the application](YOUR_STREAMLIT_APP_LINK)

## 📌 Project Overview

Construction-site safety is essential for protecting workers from workplace hazards. This project uses a trained YOLOv8 object detection model to identify PPE-related objects in uploaded images.

Users can upload a construction-site image and view detected objects, bounding boxes, confidence scores, and potential PPE violations.

## 🎯 Detection Classes

The model detects five classes:

| Class ID | Class Name |
|---|---|
| 0 | Helmet |
| 1 | No-Helmet |
| 2 | No-Vest |
| 3 | Person |
| 4 | Vest |

## 🛠️ Technologies Used

- Python
- YOLOv8 (Ultralytics)
- Streamlit
- OpenCV
- NumPy
- Pandas
- Pillow
- Google Colab

## 📊 Dataset Information

The project uses a construction safety dataset from Roboflow Universe.

**Dataset:** [Construction Safety Dataset](https://universe.roboflow.com/ppe-sy76h/construction-safety-gsnvb-mu4sy)

| Dataset Split | Images |
|---|---:|
| Training | 997 |
| Validation | 119 |
| Testing | 90 |
| **Total** | **1,206** |

## ⚙️ Features

- Upload construction-site images.
- Detect helmets, safety vests, workers, and PPE violations.
- Display original and annotated images side by side.
- Adjust the detection confidence threshold.
- Display detected object names and confidence scores.
- Show a detection summary.
- Highlight potential missing-helmet and missing-vest detections.

## 💻 Run Locally

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

### 2. Open the project folder

```bash
cd Construction-PPE-Detection
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
python -m streamlit run app.py
```

The application will open at:

`http://localhost:8501`

## 📁 Project Structure

```text
Construction-PPE-Detection/
│
├── app.py
├── best.pt
├── requirements.txt
└── README.md
```

## 📸 Application Screenshots

Add screenshots of your working Streamlit application here after deployment.

## ⚠️ Disclaimer

This project is developed for educational and demonstration purposes. Detection results depend on image quality, model performance, and confidence thresholds. The system should not be considered a replacement for professional construction-site safety inspections.

## 👩‍💻 Author

**Eeman Fatima**

Bachelor of Science in Artificial Intelligence

## ⭐ Acknowledgment

- Ultralytics YOLO
- Roboflow Universe
- Streamlit
- Google Colab

# 🤟 Real-Time ASL Alphabet Detection System

## 📌 Project Overview

The Real-Time ASL Alphabet Detection System is a Deep Learning and Computer Vision project designed to recognize American Sign Language (ASL) alphabets using a webcam.

The system uses a Convolutional Neural Network (CNN) model to classify hand gestures and display the corresponding alphabet in real time. It helps bridge communication gaps between sign language users and non-sign language users.

---

## 🎯 Objectives

- Build a real-time ASL alphabet recognition system.
- Apply Deep Learning and Computer Vision techniques.
- Convert hand gestures into readable text.
- Improve accessibility through AI-based solutions.

---

## 🚀 Features

✅ Real-time webcam-based gesture recognition

✅ CNN-based alphabet classification

✅ Grayscale image processing

✅ Noise reduction using Gaussian Blur

✅ ROI (Region of Interest) based detection

✅ Stable prediction mechanism

✅ Word formation from detected alphabets

✅ Lightweight and easy to deploy

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| TensorFlow | Deep Learning Framework |
| Keras | Neural Network API |
| OpenCV | Computer Vision |
| NumPy | Numerical Computation |
| Matplotlib | Visualization |

---

## 📂 Project Structure

```text
ASL-Alphabet-Detection/
│
├── train_model.py
├── realtime_detection.py
├── requirements.txt
├── README.md
├── asl_model.h5
│
├── dataset/
│   ├── train/
│   └── test/
│
├── screenshots/
│   ├── training_accuracy.png
│   ├── prediction_output.png
│   └── threshold_output.png
│
└── results/
    └── output_images
```

---

## 📊 Dataset Information

The dataset consists of labeled images representing American Sign Language (ASL) alphabets (A-Z).

Dataset Source:

https://www.kaggle.com/datasets/grassknoted/asl-alphabet

### Dataset Structure

```text
dataset/
│
├── train/
│   ├── A/
│   ├── B/
│   ├── C/
│   └── ...
│
└── test/
    ├── A/
    ├── B/
    ├── C/
    └── ...
```

---

## 🔄 System Workflow

1. Load ASL dataset
2. Preprocess images
3. Resize images to 64x64
4. Convert images to grayscale
5. Normalize pixel values
6. Train CNN model
7. Save trained model
8. Open webcam
9. Detect hand gesture
10. Predict alphabet
11. Display prediction
12. Form words using detected alphabets

---

# 🧠 Model Architecture

CNN Architecture:

```text
Input Layer (64x64x1)
        ↓
Conv2D (32 Filters)
        ↓
MaxPooling
        ↓
Conv2D (64 Filters)
        ↓
MaxPooling
        ↓
Flatten
        ↓
Dense (128)
        ↓
Output Layer (26 Classes)
```

---

# 📈 Training Results

## Training Accuracy

> Add training accuracy graph here

![Training Accuracy](screenshots/training_accuracy.png)

---

## Training Loss

> Add training loss graph here

![Training Loss](screenshots/training_loss.png)

---

# 🖼️ Project Screenshots

## Home Screen


<img width="1057" height="554" alt="image" src="https://github.com/user-attachments/assets/b0bee282-e707-42e0-94ec-5d93bf77d63b" />


---

## Real-Time Detection


<img width="1088" height="549" alt="image" src="https://github.com/user-attachments/assets/8af789db-7fa3-45a4-a21a-9d350f74e651" />


---

## Threshold Output

<img width="338" height="335" alt="image" src="https://github.com/user-attachments/assets/54df062e-25f7-4ae7-9490-5fb1945eb1fb" />


---

## ROI Detection

<img width="516" height="307" alt="image" src="https://github.com/user-attachments/assets/fc928628-132f-4ea3-a46d-e3d64fa894a3" />


---

# 📋 Output Results

### Sample Prediction

```text
Prediction: A
Word: A
```

### Sample Prediction

```text
Prediction: B
Word: AB
```

### Sample Prediction

```text
Prediction: C
Word: ABC
```

---

# 📸 Output Images

## Output 1

<img width="579" height="457" alt="Code_Generated_Image" src="https://github.com/user-attachments/assets/16b7ad2c-ef5a-4039-b38b-b34b2aed2297" />


---

## Output 2

<img width="785" height="704" alt="Code_Generated_Image (1)" src="https://github.com/user-attachments/assets/7ed8715e-4539-406d-86c7-3be1be613f6f" />


---

## Output 3

<img width="855" height="704" alt="Code_Generated_Image (2)" src="https://github.com/user-attachments/assets/13c5c73d-cf97-4f20-addb-8a1a11dbd465" />


---

# ⚙️ Installation

Clone Repository

```bash
git clone https://github.com/yourusername/ASL-Alphabet-Detection.git
```

Move into Project Folder

```bash
cd ASL-Alphabet-Detection
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Project

### Train Model

```bash
python train_model.py
```

### Run Real-Time Detection

```bash
python realtime_detection.py
```

Press **Q** to quit the webcam.

---

# 🎯 Applications

- Assistive Communication Systems
- Healthcare Sector
- Educational Institutions
- Smart Classrooms
- AI-based Translation Systems
- Human Computer Interaction
- Accessibility Technologies

---

# 🔮 Future Enhancements

- Dynamic Gesture Recognition
- Sentence Formation
- Text-to-Speech Conversion
- Mobile Application Deployment
- Web Application Deployment
- MediaPipe Integration
- YOLO-based Hand Detection

---

# 👨‍💻 Author

**Rama Devi**

Data Science Graduate

Python | Machine Learning | Deep Learning | Computer Vision

---

# ⭐ If you found this project useful, consider giving it a star.

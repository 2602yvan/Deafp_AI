import os
import numpy as np
import csv
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from tensorflow.keras import models, layers
from sklearn.metrics import classification_report

# === CONFIG ===
NpyFolder = "Hand_LandMark"
LabelsFile = "labels.csv"
NUM_AUGMENTATIONS = 5

# === LOAD DATA + AUGMENT ===
X = []
y = []

def augment_landmarks(landmarks):
    # Small Gaussian noise
    noise = np.random.normal(0, 0.01, size=landmarks.shape)
    augmented = landmarks + noise
    return augmented

with open(LabelsFile, mode="r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    for row in reader:
        npy_filename, label = row
        npy_path = os.path.join(NpyFolder, npy_filename)

        if not os.path.exists(npy_path):
            continue

        landmarks = np.load(npy_path)  # shape: (frames,126)

        # Process original
        mean_features = np.mean(landmarks, axis=0)
        std_features = np.std(landmarks, axis=0)
        min_features = np.min(landmarks, axis=0)
        max_features = np.max(landmarks, axis=0)
        all_features = np.concatenate([mean_features, std_features, min_features, max_features])

        X.append(all_features)
        y.append(label)

        # Generate augmented samples
        for i in range(NUM_AUGMENTATIONS):
            aug_landmarks = augment_landmarks(landmarks)
            mean_features = np.mean(aug_landmarks, axis=0)
            std_features = np.std(aug_landmarks, axis=0)
            min_features = np.min(aug_landmarks, axis=0)
            max_features = np.max(aug_landmarks, axis=0)
            all_features = np.concatenate([mean_features, std_features, min_features, max_features])

            X.append(all_features)
            y.append(label)

print("✅ Loaded original + augmented samples:", len(X))
print("Labels distribution:", Counter(y))

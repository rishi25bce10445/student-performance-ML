# Student Performance Prediction using Machine Learning

## Overview

This project focuses on predicting student academic performance based on various lifestyle and academic factors. Many students are unsure whether their daily habits are actually helping them improve or not. This project uses Machine Learning to analyze those habits and predict performance.

The model classifies whether a student is likely to perform well or poorly.


## Problem Statement

The goal of this project is to build a Machine Learning model that can predict student performance using features such as:

* Study hours
* Attendance
* Sleep hours
* Screen time
* Previous marks
* Assignment completion
* Stress level

### Output:

* **1 → Good Performance**
* **0 → Poor Performance**

## Motivation

This problem is very relevant in real life. Students often focus only on studying more but ignore other important factors like sleep, stress, and distractions.

With the help of this model:

* Students can understand their performance trends
* Weak areas can be identified early
* Better habits can be developed


## Dataset

The dataset used in this project is manually created based on realistic student behavior.

Each row represents a student and includes:

* `study_hours` → daily study time
* `attendance` → class attendance (%)
* `sleep_hours` → average sleep
* `screen_time` → non-study screen usage
* `prev_marks` → previous performance
* `assignments` → completion percentage
* `stress` → stress level (1–10)

### Target:

* `result` → 0 (Poor), 1 (Good)


## Technologies Used

* Python
* Pandas
* Scikit-learn


## Model Used

**Logistic Regression**

Reason:

* Suitable for binary classification
* Simple and easy to understand
* Works well with small datasets


## How to Run the Project

### Step 1: Install dependencies

```bash
pip install pandas scikit-learn
```

### Step 2: Run the model

```bash
python model.py
```

## Output

The model:

* Prints accuracy score
* Displays confusion matrix
* Predicts performance for sample student inputs


## Example

Input:

```text
study_hours = 4
attendance = 65
sleep = 5
screen_time = 6
```

Output:

```text
Predicted Result: 0 (Poor Performance)
```

## Limitations

* Dataset is manually created
* Small dataset size
* Limited features
* Does not include emotional or environmental factors


## Learning Outcomes

Through this project, I learned:

* Data preprocessing using pandas
* Training a Machine Learning model
* Evaluating performance using accuracy and confusion matrix
* Applying ML concepts to a real-world problem


## Author

**Rishi Kumar**
B.Tech CSE (Core)
First Year Student
VIT Bhopal University

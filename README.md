# ft_linear_regression

A from-scratch implementation of univariate linear regression using gradient descent, applied to predicting car prices from mileage.

---

## Overview

This project trains a simple linear regression model on a dataset of car mileage vs. price. The model learns the relationship between kilometers driven and market price by minimizing a cost function through gradient descent — without using any machine learning libraries.

**Prediction formula:**

$$\hat{y}(x) = \theta_0 + \theta_1 \cdot x$$

Where:
- $x$ — mileage (km)
- $\hat{y}$ — predicted price
- $\theta_0$ — bias (y-intercept)
- $\theta_1$ — weight (slope)

---

## Project Structure

```
ft_linear_regression/
├── data.csv              # Training dataset (km, price)
├── train_model.py        # Trains the model and saves parameters
├── predict_price.py      # Loads parameters and predicts car price
├── bonus_plot.py         # Visualizes data and regression line
├── model_parameters      # Generated after training (theta0 theta1)
└── docs/
    └── theory.md         # Theory notes on linear regression
```

---

## How It Works

### 1. Training (`train_model.py`)

- Loads `data.csv`
- Applies **Z-score standardization** to both features and labels for stable convergence
- Runs **gradient descent** for up to 10,000 iterations to minimize the cost function
- Denormalizes the learned parameters back to the original data scale
- Saves `theta0` and `theta1` to `model_parameters`

**Cost function (MSE):**

$$J(\theta_0, \theta_1) = \frac{1}{2m} \sum_{i=1}^{m} \left( \hat{y}^{(i)} - y^{(i)} \right)^2$$

**Gradient descent update rules:**

$$\theta_0 := \theta_0 - \alpha \cdot \frac{1}{m} \sum_{i=1}^{m} (\hat{y}^{(i)} - y^{(i)})$$

$$\theta_1 := \theta_1 - \alpha \cdot \frac{1}{m} \sum_{i=1}^{m} (\hat{y}^{(i)} - y^{(i)}) \cdot x^{(i)}$$

### 2. Predicting (`predict_price.py`)

- Reads `model_parameters`
- Accepts mileage input in a loop
- Returns the predicted price, clipped to the range $[1000, 1{,}000{,}000]$

### 3. Visualization (`bonus_plot.py`)

- Plots the training data as a scatter chart
- Overlays the learned regression line using matplotlib

---

## Usage

### Install dependencies

```bash
pip install numpy pandas matplotlib
```

### Train the model

```bash
python train_model.py
```

This generates a `model_parameters` file containing `theta0` and `theta1`.

### Predict a price

```bash
python predict_price.py
```

```
Enter the mileage of the car: 100000
the price of the car is: 6500.0
```

### Plot the regression line

```bash
python bonus_plot.py
```

---

## Dataset

`data.csv` contains 24 samples with two columns:

| Column  | Description              |
|---------|--------------------------|
| `km`    | Mileage of the car (km)  |
| `price` | Sale price of the car (€)|

---

## Key Concepts

| Concept | Description |
|---|---|
| **Linear Regression** | Models the relationship between one feature and a continuous output |
| **Gradient Descent** | Iterative optimization algorithm to minimize the cost function |
| **Z-score Standardization** | Scales features to mean=0, std=1 to speed up convergence |
| **Denormalization** | Converts learned parameters back to the original data scale |
| **Prediction Clipping** | Constrains output to a valid price range |

For detailed theory, see [docs/theory.md](docs/theory.md).

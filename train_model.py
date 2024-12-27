import numpy as np
import pandas as pd

def cost_function(data: pd.DataFrame, theta0: float, theta1: float) -> float:
    m = data.shape[0]
    x = data['km'].values
    y = data['price'].values
    predection = theta1 * x + theta0
    
    return sum((predection - y) ** 2) / (2 * m)

def compute_gradient(data: pd.DataFrame, theta0: float, theta1: float):
    m = data.shape[0]
    sum_theta0 = 0.0
    sum_theta1 = 0.0
    for row in data.values:
        x = float(row[0])
        y = float(row[1])
        error = (theta1 * x + theta0) - y
        sum_theta0 += error
        sum_theta1 += error * x
    dj_dtheta0 = sum_theta0 / m
    dj_dtheta1 = sum_theta1 / m
    return dj_dtheta0, dj_dtheta1

def gradient_descent(data: pd.DataFrame, theta0: float, theta1: float, learning_rate: float, iterations: int = 1*10**4):
    best_theta0 = theta0
    best_theta1 = theta1
    lowest_cost = float('inf')

    for _ in range(iterations):
        dj_dtheta0, dj_dtheta1 = compute_gradient(data, theta0, theta1)
        theta0 -= learning_rate * dj_dtheta0
        theta1 -= learning_rate * dj_dtheta1

        cost_value = cost_function(data, theta0, theta1)
        if cost_value < lowest_cost:
            lowest_cost = cost_value
            best_theta0 = theta0
            best_theta1 = theta1

    return best_theta0, best_theta1

def normalize_data(data: pd.DataFrame):
    feature_mean = data['km'].mean()
    feature_std = data['km'].std()
    label_mean = data['price'].mean()
    label_std = data['price'].std()

    data['km'] = (data['km'] - feature_mean) / feature_std
    data['price'] = (data['price'] - label_mean) / label_std

    return data, feature_mean, feature_std, label_mean, label_std

def denormalize_theta(theta0, theta1, feature_mean, feature_std, label_mean, label_std):
    theta1_original = theta1 * (label_std / feature_std)
    theta0_original = label_mean + label_std * theta0 - theta1_original * feature_mean
    return theta0_original, theta1_original

def main():
    try:
        theta0 = 0.0
        theta1 = 0.0
        data = pd.read_csv('data.csv')

        data, feature_mean, feature_std, label_mean, label_std = normalize_data(data)
        learning_rate = 0.001
        theta0, theta1 = gradient_descent(data, theta0, theta1, learning_rate)

        theta0, theta1 = denormalize_theta(theta0, theta1, feature_mean, feature_std, label_mean, label_std)

        with open("model_parameters", 'w') as file:
            file.write(f"{theta0} {theta1}")

    except FileNotFoundError as err:
        print("Error:", err)
        return

if __name__ == "__main__":
    main()

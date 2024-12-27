import pandas as pd
import matplotlib.pyplot as plt

def main():
    try:
        with open("model_parameters", 'r') as file:
            model_parameters = file.read().strip()
        
        if not model_parameters:
            theta0, theta1 = 0.0, 0.0
        else:
            theta0, theta1 = map(float, model_parameters.split())

        data = pd.read_csv('data.csv')
        x = [row[0] for row in data.values]
        y = [row[1] for row in data.values]

        plt.xlabel('Kilometers')
        plt.ylabel('Price')
        plt.scatter(x, y, label='Data Points', color='blue')

        predicted_y = [theta0 + theta1 * xi for xi in x]
        plt.plot(x, predicted_y, color='red', label='Regression Line')

        plt.title('Linear Regression Model')
        plt.legend()
        plt.show()

    except FileNotFoundError as err:
        print("Error:", err)
    except Exception as e:
        print("An unexpected error occurred:", e)

if __name__ == "__main__":
    main()

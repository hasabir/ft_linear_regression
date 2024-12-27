
import numpy as np


def main():
	with open("model_parameters", 'r') as file:
		model_parameters = file.read()
	if not model_parameters:
		theta0 = 0.0
		theta1 = 0.0
	else:
		theta0, theta1 = map(float, model_parameters.split())
	
	while True:
		try:
			mileage = input("Enter the mileage of the car: ")
			predection = theta0 + theta1 * float(mileage)
			postprocessed_predection = np.clip(predection, 1*10**3, 1*10**6)
			print("the price of the car is:", postprocessed_predection)
		except KeyboardInterrupt:
			print("\nexiting ...")
			break
		except ValueError as e:
			print("Syntaxe error")


if __name__ == "__main__":
	main()
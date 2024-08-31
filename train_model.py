import pandas


def cost_function(data: pandas.DataFrame, theta0, theta1):
	m = data.shape[0]
	sum : float = 0.0
	for row in data.values:
		x = float(row[0])
		y = float(row[1])
		sum += ((theta1 * x + theta0) - y)**2
	return 1/(2 * m) * sum


def compute_gradient(data: pandas.DataFrame, theta0, theta1):
	m = data.shape[0]
	sum_theta1 = 0
	sum_theta0 = 0
	for row in data.values:
		x = float(row[0])
		y = float(row[1])
		sum_theta0 += ((theta1 * x + theta0) - y) 
		sum_theta1 += ((theta1 * x + theta0) - y) * x
	dj_dtheta0 = sum_theta0 / m
	dj_dtheta1 = sum_theta1 / m
	return dj_dtheta0, dj_dtheta1


def gradien_descent(data: pandas.DataFrame, theta0, theta1, learning_rate):

	stock_theta0 = theta0
	stock_theta1 = theta1
	stock_cost_value = float('inf')

	for i in range (0, 20):
		dj_dtheta0, dj_dtheta1 = compute_gradient(data, theta0, theta1)
		tmp_theta0  = theta0 - learning_rate * dj_dtheta0
		tmp_theta1 = theta1 - learning_rate * dj_dtheta1
		theta0 = tmp_theta0
		theta1 = tmp_theta1
		cost_value = cost_function(data, tmp_theta0, tmp_theta1)
		if cost_value < stock_cost_value:
			stock_cost_value = cost_value
			stock_theta0 = theta0
			stock_theta1 = theta1
	return stock_theta0, stock_theta1


def main():
	try:
		theta0 = 0
		theta1 = 0
		data = pandas.read_csv('data.csv')
		theta0, theta1 = gradien_descent(data, theta0, theta1, 0.0000001)
		with open("model_parameters", 'w') as file:
			file.write(f"{theta0} {theta1}")
		
	except FileNotFoundError as err:
		print("Error:", err)
		return



if __name__ == "__main__":
	main()
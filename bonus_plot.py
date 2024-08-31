import pandas
import matplotlib.pyplot as plt


def main():
	with open("model_parameters", 'r') as file:
		model_parameters = file.read()
	if not model_parameters:
		theta0 = 0.0
		theta1 = 0.0
	else:
		theta0, theta1 = map(float, model_parameters.split())
	




	data = pandas.read_csv('data.csv')
	x = [row[0]  for row in data.values]
	y = [row[1]  for row in data.values]

	y_hat = []
	for row in data.values:
		y_hat.append(theta0 + theta1 * float(row[0]))
	fig = plt.figure()
	ax = fig.add_subplot()
	plt.plot(x, y_hat)
	
	# x_ticks = [year for i, year in enumerate(x) if i % 40 == 0]
	# ax.set_xticks(x_ticks)
	plt.xlabel('km')
	plt.ylabel('price')
	plt.scatter(x, y)

	plt.title('data')
	
	plt.show()



if __name__ == "__main__":
	main()
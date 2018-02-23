import numpy as np

num_interations = 10000000

def main():
	x_count = 0
	y_count = 0

	x_prob = 2/3
	y_prob = 1/3

	for i in range(num_interations):
		x = 1
		y = 2
		while (x > 0 and y > 0):
			val = np.random.rand()
			if val > x_prob:
				x = x - 1
				y = y + 1
			else:
				x = x + 1
				y = y - 1

		if x == 0:
			y_count = y_count + 1
		else:
			x_count = x_count + 1


	print("I won {} %% of the time".format(x_count/num_interations*100))

if __name__ == "__main__":
	main()
import numpy as np


num_each = 30
n_iter = 100000


def main():
	total_preferred_vitamins_count = 0
	for i in range(n_iter):
		vitamins_in_bottle = np.append(np.zeros(num_each), np.ones(num_each))
		np.random.shuffle(vitamins_in_bottle)
		preferred_vitamins_count = 0
		while vitamins_in_bottle.size > 0:
			day_vitamins = vitamins_in_bottle[range(4)]
			vitamins_in_bottle = np.delete(vitamins_in_bottle, [0, 1, 2, 3])
			preferred_vitamins_today = np.sum(day_vitamins, dtype=np.int32)
			if preferred_vitamins_today > 2:
				preferred_vitamins_today = 2
			preferred_vitamins_count += preferred_vitamins_today

		total_preferred_vitamins_count += preferred_vitamins_count

	print(total_preferred_vitamins_count/n_iter/num_each)

if __name__ == "__main__":
	main()
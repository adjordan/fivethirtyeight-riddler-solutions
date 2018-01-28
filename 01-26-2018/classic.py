import numpy as np
import itertools

# Manually insert the coordinates of the shapes
def get_coordinates_of_shapes():
	shape_coordinates = {}
	shape_coordinates['s1'] = [[0,0,2], [0,12,10]]
	shape_coordinates['s2'] = [[0,2,4], [0,10,8]]
	shape_coordinates['s3'] = [[0,2,3], [0,4,0]]
	shape_coordinates['s4'] = [[2,3,3], [4,6,0]]
	shape_coordinates['s5'] = [[0,4,6], [12,8,12]]
	shape_coordinates['s6'] = [[3,3,4,6,6], [0,6,8,6,0]]
	shape_coordinates['s7'] = [[4,6,6], [8,12,6]]
	shape_coordinates['s8'] = [[6,8,12], [0,4,0]]
	shape_coordinates['s9'] = [[6,6,9,8], [6,12,6,4]]
	shape_coordinates['s10'] = [[8,9,12], [4,6,0]]
	shape_coordinates['s11'] = [[6,6,8], [0,6,4]]
	shape_coordinates['s12'] = [[6,12,12,9], [12,12,8,6]]
	shape_coordinates['s13'] = [[9,12,12], [6,8,6]]
	shape_coordinates['s14'] = [[9,12,12], [6,6,0]]

	return shape_coordinates


# Simple implementation of the shoelace formula to calculate area based on x-y coordinates
def calculate_area_of_shape(x, y):
	return 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))


# Calculate areas of all shapes
def calculate_area_of_shapes():
	shape_coordinates = get_coordinates_of_shapes()
	shape_areas = []
	for key, coords in shape_coordinates.items():
		shape_areas.append(calculate_area_of_shape(coords[0], coords[1]))

	return shape_areas


def partition_by_sum(input_list, target):
	output_list = []

	# Get all possible combinations of numbers that sum to the target
	sum_sets = [list(seq) for i in range(len(input_list), 0, -1) for seq in itertools.combinations(input_list, i) if sum(seq) == target]

	# Sort every set of numbers
	for i in range(len(sum_sets)):
		sum_sets[i].sort()

	# Create a new list that has no duplicates; will account for permutations
	# at the end
	sum_sets_unique = []
	for x in sum_sets:
		if x not in sum_sets_unique:
			sum_sets_unique.append(x)

	# Find all of the pairs that combine to make the original list
	for i, set1 in enumerate(sum_sets_unique):
		for j, set2 in enumerate(sum_sets_unique):
			comb = set1 + set2
			comb.sort()
			if set1 != set2 and comb == input_list:# and [set1, set2] not in output_list and [set2, set1] not in output_list:
				output_list.append([set1, set2])

	return output_list


def main():
	# Load in the areas of each shape
	shape_areas = [int(x) for x in calculate_area_of_shapes()]

	# Sort shape areas
	shape_areas.sort()

	# Get sum of all areas and the target area for each color
	array = np.asarray(shape_areas, dtype=np.int)
	total_area = array.sum()
	quadrant_area = total_area / 4

	# Split the shapes as if there are only 2 colors, target area of half the total area
	# for each color; does not include permutation of shapes with same area across sets
	two_color_partition_sets = partition_by_sum(shape_areas, quadrant_area*2)

	# For each pair of sets that results from the first partition, partition each set in
	# each pair again to get 4 colors
	four_color_partition_sets = []
	for pair_set in two_color_partition_sets:
		partition_set1 = partition_by_sum(pair_set[0], quadrant_area)
		partition_set2 = partition_by_sum(pair_set[1], quadrant_area)
		four_color_partition_sets.append([partition_set1, partition_set2])
		print([partition_set1, partition_set2])

	print(len(four_color_partition_sets))


if __name__ == "__main__":
	main()
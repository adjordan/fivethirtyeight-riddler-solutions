"""
Intuition:

If there are x <= 18 senators present, then a palindrome can be formed by an even split in the vote:

	18 senators: 9-9 is a palindrome

If there are x > 18 senators present, then palindromes can only be found if x is divisible by 11. For
a valid number of senators x, the number of possible palindromes p is given by:

	p = x / 11 - 1

If we sum values of p across all valid values of x there are 45 total palindromes that can be formed.

If we include leading zeros on single digit numbers, then we add an additional 18 possibilities, two
to each x that is divisible by 11:

	for x = 22, palindromes include 20-02 and 02-20,
	for x = 33, palindromes include 30-03 and 03-30,
	etc.

This would give us a total of 63 possibile palindromes.

The python script below provides the same answer via brute force.

"""

def main():
	palindrome_count = 0
	for i in range(1,101):
		for j in range(i+1):
			yea_count = j
			nay_count = i - j

			if str(yea_count) == str(nay_count)[::-1]:
				print("If there are {} senators present, a vote of {}-{} is a palindrome!".format(i, yea_count, nay_count))
				palindrome_count +=1

	print("\nTotal number of possible palindromes: {}".format(palindrome_count))


if __name__ == "__main__":
	main()
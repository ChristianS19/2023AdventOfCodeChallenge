"""
Update to the day 01. Some of the numbers were actually spelt out in letters! Rather than just the first and last digit, 
it is actually the first and last number, whether digit or word. Find the real first and last number for each line.

For example:
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen

Here, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

"""

def mixed_calibration_values(input):
    """
    Takes in a text file, and returns the sum of the combined first and last number (digit or word) of each line in the file.
    input: str, the location of the input file.

    Returns the sum of all calibration values as an integer.
    """

    number_words = {
        'twone': 2, 'eightwo': 8, 'eighthree': 8,                   # higher overlapping numbers
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
        }

    calibration_sum = 0
    with open(input, 'r') as file:
        for line in file:
            for key in number_words:
                if key in line:
                    line = line.replace(key, str(number_words[key]))
            digits = [s for s in line if s.isdigit()]
            first_num = digits[0]
            second_num = digits[-1]
            print(first_num + second_num)
            calibration_sum += int(first_num + second_num)
            print(f"Sum is: {calibration_sum}")
    file.close()
    return calibration_sum




if __name__ == '__main__':
    main()


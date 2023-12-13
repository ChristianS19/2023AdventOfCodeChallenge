"""
D02_NumericalWords Test
Test taken from "https://adventofcode.com/2023/day/2/
Numbers are only from one to nine. Numbers such as sixteen are not valid, and taken as six.

Lines:
two1nine            # Test Case 1: Word first, Word Last
eightwothree        # Test Case 2: All words
abcone2threexyz     # Test Case 3: Word first, Word l
xtwone3four         
4nineeightseven2     
zoneight234         # Test Case 4: Word first with extra letter, digit last
7pqrstsixteen       # Test Case 5: Digit first, Word last

Here, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

For the total calibration file, the correct answer is .

"""

from Day02_NumericalWords import mixed_calibration_values

test_cases = [
    ("Day02_NumericalWords_InputData_Test.txt", 281),
    ("Trebuchet_InputData.txt", 54500)
]

# print(mixed_calibration_values("Trebuchet_InputData.txt"))
# print(mixed_calibration_values("Day02_NumericalWords_InputData_Test.txt"))

for idx, (input_data, expected_output) in enumerate(test_cases, start=1):
    output = mixed_calibration_values(input_data)
    assert (output == expected_output, 
            f"""Test {idx:02d} Failed,
            Input: {input_data},
            Expected Output: {expected_output},
            Actual Output: {output}"""
            )
    print(f"Test {idx:02d} Passed")



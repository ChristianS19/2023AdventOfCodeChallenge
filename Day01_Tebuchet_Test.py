"""
D01_Trebuchet Test
Test taken from "https://adventofcode.com/2023/day/1/
Lines:

1abc2           # Test Case 1: Two digits.
pqr3stu8vwx     # Test Case 2: Two digits mixed
a1b2c3d4e5f     # Test Case 3: Three digits mixed
treb7uchet      # Test Case 4: Single digit
bdbr23skd4n     # Test Case 5: Double digit and single digit

In this example, the calibration values of these four lines are 12, 38, 15, 77, 24. Adding these together produces 166.

For the total calibration file, the correct answer is 55816.

"""

from Day01_Trebuchet import calibration_values

test_cases = [
    ("Day01_Trebuchet_InputData_Test.txt", 166),
    ("Trebuchet_InputData.txt", 55816)
]

for idx, (input_data, expected_output) in enumerate(test_cases, start=1):
    output = calibration_values(input_data)
    assert (output == expected_output, 
            f"""Test {idx:02d} Failed,
            Input: {input_data},
            Expected Output: {expected_output},
            Actual Output: {output}"""
            )
    print(f"Test {idx:02d} Passed")
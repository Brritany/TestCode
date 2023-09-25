
# Unit Testing for Student Code

## Description

This repository contains a unit test script (`test_code.py`) designed to validate student code in a Data Science project. The project involves data manipulation and analysis using Python, Pandas, and other relevant libraries.

## How to Use

### Clone the Repository
Clone this repository into your Google Colab environment:

```python
!git clone https://github.com/Brritany/TestCode.git
```

### Import and Run the Unit Tests
After cloning, import the `TestCode` class from `test_code.py` and run the unit tests as follows:

```python
from TestCode.test_code import TestCode
import unittest

suite = unittest.TestLoader().loadTestsFromTestCase(TestCode)
unittest.TextTestRunner().run(suite)
```

## Test Cases

The unit tests include the following:

1. `test_discharge_summary`: Validates that the DataFrame contains 'Discharge summary' records.
2. `test_merged_data`: Checks if the DataFrame contains the columns 'SUBJECT_ID' and 'HADM_ID'.
3. `test_final_admission`: Ensures that each 'SUBJECT_ID' appears only once in the DataFrame.

## Requirements

- Python 3.x
- Pandas

## Author

Yong Zhen Huang

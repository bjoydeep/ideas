```python
# Importing required libraries
from typing import List

def calculate_moving_average(data: List[float], window: int) -> List[float]:
    """
    Function to calculate moving average

    :param data: List of float numbers
    :param window: Integer representing the window for moving average
    :return: List of float numbers representing the moving average
    """
    # Input validation
    if not isinstance(data, list) or not all(isinstance(i, (int, float)) for i in data):
        raise ValueError("data must be a list of numbers.")
    if not isinstance(window, int) or window <= 0:
        raise ValueError("window must be a positive integer.")

    # Variable to store moving averages
    moving_averages = []

    # Loop through data
    for i in range(len(data) - window + 1):
        # Calculate moving average and append to list
        moving_averages.append(sum(data[i:i+window]) / window)

    return moving_averages


def test_calculate_moving_average():
    """Test function for calculate_moving_average"""
    assert calculate_moving_average([10.0, 20.0, 30.0, 40.0, 50.0], 2) == [15.0, 25.0, 35.0, 45.0], "Invalid result for calculate_moving_average"
    assert calculate_moving_average([1.0, 2.0, 3.0, 4.0, 5.0], 3) == [2.0, 3.0, 4.0], "Invalid result for calculate_moving_average"
    try:
        calculate_moving_average([10.0, "b", 30.0], 2)
    except ValueError:
        pass
    else:
        raise AssertionError("Expected a ValueError for invalid input data in calculate_moving_average")

    try:
        calculate_moving_average([10.0, 20.0, 30.0], 0)
    except ValueError:
        pass
    else:
        raise AssertionError("Expected a ValueError for invalid window in calculate_moving_average")


# Run the test
test_calculate_moving_average()
```
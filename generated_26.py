Sure, based on the requirements, here is the Python code you need.

Please save it in a Python file.

```python
from typing import List
import unittest

def calculate_moving_average(data: List[float], window: int) -> List[float]:
    # Basic input validation
    if not isinstance(data, list) or not all(isinstance(i, (float, int)) for i in data):
        raise ValueError("data: List must contain only integers or floats")
    
    if not isinstance(window, int) or window < 1:
        raise ValueError("window: integer value must be greater than 0")

    if window > len(data):
        raise ValueError("window: integer value cannot be greater than the length of data List")

    #Your logic for moving average goes here
    result = []
    
    for i in range(len(data) - window + 1):
        result.append(sum(data[i:i+window]) / window)

    return result

class TestMovingAverage(unittest.TestCase):
  
    def test_calculate_moving_average(self):
        self.assertEqual(calculate_moving_average([4.0, 3.0, 5.0, 6.0, 8.0], 3), [4.0, 4.666666666666667, 6.333333333333333])
        self.assertEqual(calculate_moving_average([1.0, 2.0, 3.0, 4.0, 5.0], 2), [1.5, 2.5, 3.5, 4.5])
        self.assertRaises(ValueError, calculate_moving_average, [1.0, 2.0, 'a', 4.0], 2)
        self.assertRaises(ValueError, calculate_moving_average, [1.0, 2.0, 3.0, 4.0], 0)
        self.assertRaises(ValueError, calculate_moving_average, [1.0, 2.0, 3.0, 4.0], 5)


if __name__ == '__main__':
    unittest.main()
```

Please take note that you can run the test cases by simply running the python file.
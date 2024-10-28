# PyProgress

Library for simple and pretty progress bars in Python.

## Example

Ever wanted to use a progress bar like this?

```[22.00%] [####\---------------] (11/50)```

Say no more!

### Running the demo

```python demo.py```

### Minimal example

```python
from pyprogress.ProgressBar import ProgressBar

# create a bar for 100 processing units with default width
bar = ProgressBar(100.0)

# set to unit 75/100
bar.update(75)

# print
bar.print()
```

## Requirements

- Python (duh?)


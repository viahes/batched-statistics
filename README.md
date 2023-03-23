# Incremental-Statistics Python library

It computes several statistical measures in an incremental way and without keeping the original data in memory, reducing substantially the amount of memory needed to extract statistics in a huge amount of data situation.

## 1. Metrics

The following metrics can be obtained from the observations:
  - `count`: number of samples
  - `mean`: average
  - `std`: standard deviation
  - `var`: variance
  - `quantile`: any quantile from 0 to 1
  - `min`: min value
  - `max`: max value

## Usage

``` python
from incremental_statistics import Statistics

stats = Statistics()

stats.add(1)
stats.add([2,5])

print(stats.report())

>>> {'count': 3, 'mean': 2.6666666666666665, 'std': 1.699673171197595, 'var': 2.8888888888888893, 'median': 2.0, 'q1': 1.5, 'q3': 3.5, 'min': 1, 'max': 5
```

# Incremental-Statistics Python library

It computes several statistical measures incrementally and without keeping the original data in memory, substantially reducing the amount of memory needed to extract statistics in a massive data situation.

## 1. Metrics

The following metrics can be obtained from the observations:
  - `count`: number of samples
  - `mean`: average
  - `std`: standard deviation
  - `var`: variance
  - `quantile`: any quantile from 0 to 1
  - `min`: min value
  - `max`: max value

## 2. Basic usage

The method `add` of the Statistics class appends samples to the population.
You can add them sample by sample or by providing a list of samples.

``` python
from incremental_statistics import Statistics

stats = Statistics()

# Adding a single sample
stats.add(1)
# Adding an array of samples
stats.add([2,5])

print(stats.report())

>>> {'count': 3, 'mean': 2.6666666666666665, 'std': 1.699673171197595, 'var': 2.8888888888888893, 'median': 2.0, 'q1': 1.5, 'q3': 3.5, 'min': 1, 'max': 5
```

## 3. Batched calculation

With Statistics, you can calculate splits of the population separately and then merge them into a single Statistics object. The following example assumes that the `stats_batch1` and `stats_batch2` are calculated in different processes.

``` python
from incremental_statistics import Statistics

stats = Statistics()
stats_batch1 = Statistics()
stats_batch2 = Statistics()

# Samples of the first batch
stats_batch1.add([2,5])
# Samples of the second batch
stats_batch2.add([1])

# Merging statistics
stats.update(stats_batch1)
stats.update(stats_batch2)

print(stats.report())

>>> {'count': 3, 'mean': 2.6666666666666665, 'std': 1.699673171197595, 'var': 2.8888888888888893, 'median': 2.0, 'q1': 1.5, 'q3': 3.5, 'min': 1, 'max': 5
```

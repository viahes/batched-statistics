# Incremental-Statistics Python library

It computes several statistical measures incrementally and without keeping the original data in memory, substantially reducing the amount of memory needed to extract statistics in a massive data situation.

## 1. Metrics

The following metrics can be obtained from the observations:
  - `count`: number of samples
  - `mean`: average
  - `std`: standard deviation
  - `var`: variance
  - `median`: median
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

stats.report(round_to=1, prefix="-")

>>> - Number of samples: 3
>>> - Mean: 2.7
>>> - Standard deviation: 1.7
>>> - Variance: 2.9
>>> - Median: 2.0
>>> - 1rs quantile: 1.5
>>> - 3rd quantile: 3.5
>>> - Min value: 1
>>> - Max value: 5
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

stats.report(round_to=1, prefix="-")

>>> - Number of samples: 3
>>> - Mean: 2.7
>>> - Standard deviation: 1.7
>>> - Variance: 2.9
>>> - Median: 2.0
>>> - 1rs quantile: 1.5
>>> - 3rd quantile: 3.5
>>> - Min value: 1
>>> - Max value: 5
```

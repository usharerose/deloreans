# DeLoreans
![licience](https://img.shields.io/github/license/usharerose/deloreans)
![badge](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/usharerose/2c9c2c824a9b4150718e84579abbe456/raw/badge.json)

**DeLoreans** is a simple library, providing compared date range according to your scenario

```python
>>> import datetime
>>> import deloreans
>>>
>>> kwargs = dict()
>>> kwargs["start_date"] = datetime.date(2024, 6, 1)
>>> kwargs["end_date"] = datetime.date(2024, 6, 30)
>>> kwargs["date_granularity"] = deloreans.DateGranularity.MONTHLY
>>> kwargs["offset"] = -1
>>> kwargs["offset_granularity"] = deloreans.OffsetGranularity.YEARLY
>>>
>>> compared_start_date, compared_end_date = deloreans.get(**kwargs)
>>> compared_start_date
datetime.date(2023, 6, 1)
>>> compared_end_date
datetime.date(2023, 6, 30)
```

Above example stands for the scenario that year-over-year comparison on June 2024, which the compared date range is June 2023.

DeLoreans abstracts the process of date range offset to the above parameters.

You can construct the parameters according to the unified pattern with any conditions, then get the corresponding detailed date range instead of manual works.

## Installing DeLoreans
DeLoreans is available on PyPI:

```console
$ python -m pip install deloreans
```

## Theory
### Abstraction
A classic scenario of date comparison is year-over-year on financial performance, which compares the performance (e.g. revenue) in a date period with its numbers for the same period one year earlier.

For example, compare June 2024's revenue with the same period (or the same Nth month) of last year.

There are several key parameters which can be abstracted from above description:
* Given date range (June 2024)
* Rougher background date period, which given date range is allocated to (Year 2024)
* Index of given date range in located date period (6th month in 2024)
* Offset away from the located period (-1 since what you want is the previous year of 2024)

Then you can get the same 6th month in 2023 which is the previous year of 2024, and it is called June 2023, comparing with June 2024.

This is the process of getting the compared date range. DeLoreans abtracts the key parameters from it, making you construct multiple scenarios with various combinations.

### Parameters
#### Given Date Range
Given date range which is one of comparing objects, is defined by the following three parameters:
* `start_date`: Start date of the date range
* `end_date`: End date of the date range
* `date_granularity`: Granularity of the given date range, supported options are
  * `daily`
  * `weekly`
  * `monthly`
  * `yearly`

For example, with same date range `2024-06-01 ~ 2024-06-30`:
* When `date_granularity` is `daily`, it contains 30 data points standing for 30 days
* When `date_granularity` is `monthly`, it contains only 1 data point standing for 1 month

#### *Complete Date Range
Currently, DeLoreans doesn't support partial date range according to date granularity.

For example, with same date range `2024-06-01 ~ 2024-06-30`:
* When `date_granularity` is `monthly`, it is valid which stands for complete June 2024
* When `date_granularity` is `yearly`, it is invalid which is only part of 2024

#### Located date period's granularity
Any date range would locate at a rougher date period.

For example,
* 2024-06-01 allocates to June 2024
* July 2024 allocates to 2024

June 2024 and Yr. 2024 are the rougher date period as background. Their granularity which are `monthly` and `yearly` is declared by the parameter `offset_granularity`. Currently, supported options are,
* `daily`
* `weekly`
* `monthly`
* `yearly`
* `periodic`, which makes given date range itself be the location

#### Offset
Offset stands for the distance away from the given date range's location.

For example, comparing with the same period in previous year. `previous` means the compared date range locates at a date period (background and rougher period) 1-year away from the given one. So that 1-year is the distance and it's unit (granularity).

It is integer.
* When positive, pointing to a period in future
* When negative, pointing to a period in the past

## Usage

### June 2024 compared with same month in the year before last
```python
>>> import datetime
>>> import deloreans
>>>
>>> kwargs = dict()
>>> # given date range
>>> kwargs["start_date"] = datetime.date(2024, 6, 1)
>>> kwargs["end_date"] = datetime.date(2024, 6, 30)
>>> # granularity of date range (monthly)
>>> kwargs["date_granularity"] = deloreans.DateGranularity.MONTHLY
>>> # the one before last so that 2 unit periods away in the past
>>> kwargs["offset"] = -2
>>> # allocate to yearly period so that the granularity is 'yearly'
>>> kwargs["offset_granularity"] = deloreans.OffsetGranularity.YEARLY
>>>
>>> compared_start_date, compared_end_date = deloreans.get(**kwargs)
>>> compared_start_date
datetime.date(2022, 6, 1)
>>> compared_end_date
datetime.date(2022, 6, 30)
```

### W01 ~ W13 in 2024 compared with same period in 9 years ago
```python
>>> import datetime
>>> import deloreans
>>>
>>> kwargs = dict()
>>> # given date range according to ISO 8601 definition
>>> kwargs["start_date"] = datetime.date(2024, 1, 1)
>>> kwargs["end_date"] = datetime.date(2024, 3, 31)
>>> # granularity of date range (weekly)
>>> kwargs["date_granularity"] = deloreans.DateGranularity.WEEKLY
>>> # the one before last so that 2 unit periods away in the past
>>> kwargs["offset"] = -9
>>> # allocate to yearly period so that the granularity is 'yearly'
>>> kwargs["offset_granularity"] = deloreans.OffsetGranularity.YEARLY
>>>
>>> compared_start_date, compared_end_date = deloreans.get(**kwargs)
>>> compared_start_date
datetime.date(2014, 12, 29)  # start date of W01 2015
>>> compared_end_date
datetime.date(2015, 3, 29)  # end date of W13 2015
```

### W01 ~ W13 in 2024 compared with same period in 9 years ago, but week starts from Sunday instead of Monday
```python
>>> import datetime
>>> import deloreans
>>>
>>> kwargs = dict()
>>>
>>> kwargs["start_date"] = datetime.date(2023, 12, 31)
>>> kwargs["end_date"] = datetime.date(2024, 3, 30)
>>> kwargs["date_granularity"] = deloreans.DateGranularity.WEEKLY
>>> kwargs["offset"] = -9
>>> kwargs["offset_granularity"] = deloreans.OffsetGranularity.YEARLY
>>> # declare that week starts from Sunday
>>> # 0 is Monday, 1 is Tuesday, through 6 is Sunday
>>> kwargs["firstweekday"] = 6
>>>
>>> compared_start_date, compared_end_date = deloreans.get(**kwargs)
>>> compared_start_date
datetime.date(2015, 1, 4)  # start date of W01 2015 which is Sunday
>>> compared_end_date
datetime.date(2015, 4, 4)  # end date of W13 2015 which is Saturday
```

### April to June in 2024 compared with previous adjacent period
```python
>>> import datetime
>>> import deloreans
>>>
>>> kwargs = dict()
>>> # Given date range is April 2024 to June 2024
>>> kwargs["start_date"] = datetime.date(2024, 4, 1)
>>> kwargs["end_date"] = datetime.date(2024, 6, 30)
>>> kwargs["date_granularity"] = deloreans.DateGranularity.MONTHLY
>>> # previous one in that past so that -1
>>> kwargs["offset"] = -1
>>> # stands for the same size of given date range, in this case is 3 months
>>> kwargs["offset_granularity"] = deloreans.OffsetGranularity.PERIODIC
>>>
>>> compared_start_date, compared_end_date = deloreans.get(**kwargs)
>>> # previous adjacent period is January 2024 to March 2024
>>> compared_start_date
datetime.date(2024, 1, 1)  # start date of January 2024
>>> compared_end_date
datetime.date(2024, 3, 31)  # end date of March 2024
```

## Development Environment
### Docker (Recommended)
Execute the following commands, which sets up a service with development dependencies and enter into it.
```shell
> make run && make ssh
```
### Poetry
As a precondition, please [install Poetry](https://python-poetry.org/docs/1.7/#installation) which is a tool for dependency management and packaging in Python.

Then update and active the environment.
```shell
> poetry update && poetry shell
```

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

DeLoreans abstracts the process of date range offset to the above parameters. You can construct the input parameters representing various scenarios for another date range.

Above example stands for the scenario that year-over-year comparison on June 2024, which the compared date range is June 2023.

## Installing DeLoreans
DeLoreans is available on PyPI:

```console
$ python -m pip install deloreans
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

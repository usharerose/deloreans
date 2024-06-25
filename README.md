# DeLoreans
![badge](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/usharerose/2c9c2c824a9b4150718e84579abbe456/raw/352cd0092514c30c50538e14c1891ba51007465f/badge.json)

**DeLoreans** is a simple library, providing compared date range according to your scenario

```python
>> > import datetime
>> > import deloreans
>> > kwargs = {
    ...
'start_date': datetime.date(2024, 6, 10)
...
'end_date': datetime.date(2024, 6, 10)
...
'date_granularity': deloreans.DateGranularity.DAILY,
...
'offset': -1,
...
'offset_granularity': deloreans.OffsetGranularity.DAILY,
...}
>> > compared_start_date, compared_end_date = deloreans.get(**kwargs)
>> > compared_start_date
datetime.date(2024, 6, 9)
>> > compared_end_date
datetime.date(2024, 6, 9)
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

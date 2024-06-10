# DeLorean

**DeLorean** is a simple library, providing compared date range according to your scenario

```python
>>> import datetime
>>> import delorean
>>> kwargs = {
...     'start_date': datetime.date(2024, 6, 10)
...     'end_date': datetime.date(2024, 6, 10)
...     'date_granularity': 'daily',
...     'span_count': 1,
...     'span_granularity': 'daily',
... }
>>> compared_start_date, compared_end_date = delorean.get(**kwargs)
>>> compared_start_date
datetime.date(2024, 6, 9)
>>> compared_end_date
datetime.date(2024, 6, 9)
```

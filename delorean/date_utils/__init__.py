"""
delorean.date_utils

This module provides components on date-related parameters management
"""
from typing import Iterable

from delorean.date_utils.date_granularity import DateGranularity
from delorean.date_utils.date_range import DateRange
from delorean.date_utils.span_granularity import DateSpan, SpanGranularity  # NOQA


def _strict_zip(*iterables: Iterable) -> Iterable:
    """
    refer to: https://peps.python.org/pep-0618/#reference-implementation
    can call zip() with keyword arguments 'strict' instead in python 3.10 or later

    which validates iterables lengths' consistency
    In this scenario, it is for making sure that
    each date granularity has registered their valid span granularity
    """
    if not iterables:
        yield
    iterators = tuple(iter(iterable) for iterable in iterables)
    items = []
    try:
        while True:
            items = []
            for iterator in iterators:
                items.append(next(iterator))
            yield tuple(items)
    except StopIteration:
        pass

    if items:
        processed_iters = len(items)
        plural = " " if processed_iters == 1 else "s 1-"
        msg = f"_strict_zip() argument {processed_iters + 1} is shorter than argument{plural}{processed_iters}"
        raise ValueError(msg)

    sentinel = object()
    for i, iterator in enumerate(iterators[1:], 1):
        if next(iterator, sentinel) is not sentinel:
            plural = " " if i == 1 else "s 1-"
            msg = f"_strict_zip() argument {i+1} is longer than argument{plural}{i}"
            raise ValueError(msg)


# Commonly, finer date range can offset with rougher span granularity
# Here is the collection of valid combinations
# Please register the valid span granularity when support new date granularity
VALID_GRAINS_COMB = dict(_strict_zip(
    [item for name, item in DateGranularity.__members__.items()],
    [
        {
            SpanGranularity.DAILY,
            SpanGranularity.PERIODIC,
            SpanGranularity.WEEKLY,
            SpanGranularity.MONTHLY,
            SpanGranularity.YEARLY,
        },
        {
            SpanGranularity.DAILY,
            SpanGranularity.PERIODIC,
            SpanGranularity.WEEKLY,
            SpanGranularity.MONTHLY,
        },
        {
            SpanGranularity.DAILY,
            SpanGranularity.PERIODIC,
            SpanGranularity.WEEKLY,
        },
        {
            SpanGranularity.DAILY,
            SpanGranularity.PERIODIC,
        },
    ],
))

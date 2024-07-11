"""
exception message templates
"""


UNREGISTERED_DATE_GRANULARITY_TEMPLATE = "Unregistered date granularity: {date_granularity}"
UNREGISTERED_GRANULARITY_COMBO_TEMPLATE = """
    Unsupported Offset Granularity {offset_granularity} when Date Granularity is {date_granularity}
"""


INVALID_DATA_TYPE_TEMPLATE = "Received {input_args} as {input_dtype}, should be {dtype}"
INVALID_DATE_RANGE_TEMPLATE = """
    {end_date} as end date should be equal or greater than {start_date} as start date
"""


INVALID_WEEKDAY_ERROR_MSG = """
    weekday should be from 0 (Mon) to 6 (Sun)
"""


class IndexOverflowError(Exception):

    def __init__(self, *args, **kwargs):  # real signature unknown
        pass

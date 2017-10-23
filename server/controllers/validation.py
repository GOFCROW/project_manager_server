from datetime import datetime, date, time

# validator lack of time error
def to_bool(value):
    return value if  isinstance(value, bool) \
    else value.lower() not in ['false', '0']

def to_datetime(value):
    return value if isinstance(value, datetime) \
    else datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")

def to_date(value):
    return value if  isinstance(value, date) \
    else datetime.strptime(value, "%Y-%m-%d").date()

def to_time(value):
    return value if  isinstance(value, time) \
    else datetime.strptime(value, "%H:%M:%S").time()

CERBERUS_TYPES = {
    str: ('string', str),
    int: ('integer', int),
    bool: ('boolean', to_bool),
    float: ('float', float),
    datetime: ('datetime', to_datetime),
    date: ('date', to_date),
    time: ('string', to_time)
}

def cstr(type_, maxlength=None, required=True, nullable=False, **args):
    """Validation constraints"""
    dict_ = {
        'type': CERBERUS_TYPES[type_][0],
        'required': required,
        'nullable': nullable,
        'coerce': CERBERUS_TYPES[type_][1]
    }

    if maxlength is not None:
        dict_['maxlength'] = maxlength

    dict_.update(args)
    return dict_

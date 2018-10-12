from collections import OrderedDict


MAX_LINES = 2
ALLOWED_DAYS = ['mon', 'tue', 'wed', 'thu', 'fri']

INDEXED_DAYS = OrderedDict([
    ('mon', 0)
    ('tue', 1),
    ('wed', 2),
    ('thu', 3),
    ('fri', 4)
])

ACTIONS = {
    'mon': 'square',
    'tue': 'square',
    'wed': 'square',
    'thu': 'double',
    'fri': 'double'
}

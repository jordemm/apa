from .base import *

try:
    from .local import *
    print('local imported')
except:
    from .production import *
    print('production imported')

from .base import *

if DEBUG:
    from .dev import *
else:
    from .production import *

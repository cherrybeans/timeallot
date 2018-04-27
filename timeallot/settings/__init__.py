import os
import sys

if 'test' in sys.argv:
    from .test import *
else:
    if os.environ.get('PRODUCTION') == 'True':
        from .production import *
    else:
        try:
            from .local import *
        except ImportError as e:
            raise ImportError("Couldn't load local settings timeallot.settings.local")

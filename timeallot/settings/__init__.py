import os

if os.environ.get('PRODUCTION') == 'True':
    from .production import *
else:
    try:
        from .local import *
    except ImportError as e:
        raise ImportError(
            "Couldn't load local settings timeallot.settings.local")

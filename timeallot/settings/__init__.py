import os
import environ

from .base import *

if os.environ.get('ENV_CONFIG') in ['1', 'True', 'true']:
    from .production import *
else:
    try:
        from .local import *
    except ImportError as e:
        raise ImportError('Couldn\'t load local settings chemie.settings.local')
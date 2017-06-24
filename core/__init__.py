"""Package providing tools for glueing together the entire app.
"""

import glob
import importlib
import os
import sys
import types
import weakref


# The first task of this module is to mock core.api to obtain
# extra protection against reference cycles.

api = importlib.import_module(f'{__package__}.api')
sys.modules[f'{__package__}._api'] = api
sys.modules[f'{__package__}.api'] = api = weakref.proxy(api)


# The second task is to initialize all backend modules

def init_backed():
    """Import all backend modules and register
    all their public functions.

    No reference to the modules is stored:
    They will be kept alive by the reference
    in sys.module.

    Storing the reference here would also
    create a reference cycle.
    """
    for filename in glob.glob('backend/*.py'):
        filename, _ = os.path.splitext(filename)
        module = importlib.import_module(filename.replace(os.path.sep, '.'))
        # Equivalent to module.__dict__.items()
        functions = ((name, obj) for name, obj in vars(module).items()
                     if (isinstance(obj, types.FunctionType) and
                         not name.startswith('_'))
                    )
        for name, obj in functions:
            api.register(**{name: obj})

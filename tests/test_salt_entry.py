import unittest
import os
import os.path
import sys

import toast.salt_entry

class TestSaltEnteries(unittest.TestCase):
    def get_root_path(self):
        """Returns the path to a package or cwd if that cannot be found.  This
        returns the path of a package or the folder that contains a module.

        Not to be confused with the package path returned by :func:`find_package`.
        """
        import_name = __name__
        # Module already imported and has a file attribute.  Use that first.
        mod = sys.modules.get(import_name)
        if mod is not None and hasattr(mod, '__file__'):
            return os.path.dirname(os.path.abspath(mod.__file__))

        # Next attempt: check the loader.
        loader = pkgutil.get_loader(import_name)

        # Loader does not exist or we're referring to an unloaded main module
        # or a main module without path (interactive sessions), go with the
        # current working directory.
        if loader is None or import_name == '__main__':
            return os.getcwd()

        # For .egg, zipimporter does not have get_filename until Python 2.7.
        # Some other loaders might exhibit the same behavior.
        if hasattr(loader, 'get_filename'):
            filepath = loader.get_filename(import_name)
        else:
            # Fall back to imports.
            __import__(import_name)
            filepath = sys.modules[import_name].__file__

        # filepath is import_name.py for a module, or __init__.py for a package.
        return os.path.dirname(os.path.abspath(filepath))

    def _get_test_fixture(self, fixture_name):
        return os.path.join(
            self.get_root_path(), 'fixtures', fixture_name
        )

    def test_basic_states(self):
        fixture = self._get_test_fixture('basic_user_module.py')
        states = toast.salt_entry.top(fixture)
        self.assertEqual(states, {'base': ['vim']})

        pillars = toast.salt_entry.pillar(fixture, None, None)
        self.assertEqual(pillars, {})

    def test_basic_states_with_grains(self):
        fixture = self._get_test_fixture('basic_user_module_with_grains.py')
        states = toast.salt_entry.top(fixture)
        self.assertEqual(states, {'base': []})
        pillars = toast.salt_entry.pillar(fixture, None, None)
        self.assertEqual(pillars, {})

        grains = {'vim': True}
        states = toast.salt_entry.top(fixture, grains)
        self.assertEqual(states, {'base': ['vim']})

        pillars = toast.salt_entry.pillar(fixture, None, None, grains)
        self.assertEqual(pillars, {'vim': 'gvim'})

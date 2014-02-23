import imp
import sys

class Toaster:
    def __init__(self, path, grains):
        self.grains = grains
        self.path = path

    def _get_main_module(self):
        with open(self.path) as main_file:
            self.user_data_module = imp.load_module(
                'main', main_file, self.path,
                (".py", 'U', imp.PY_SOURCE)
            )

    def states(self):
        self.load()
        return {'base': self._states}

    def pillars(self):
        self.load()
        return self._pillars

    def load(self):
        self._get_main_module()
        ret = self.user_data_module.main(self.grains)

        self._states = ret.get('states', [])
        self._pillars = ret.get('pillars', {})

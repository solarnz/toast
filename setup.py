from setuptools import setup

setup(
    name='toast',
    packages=['toast'],
    py_modules=['salt.pillar.toast_adapter', 'salt.tops.toast_adapter'],
    version='0.1-dev',
    author='Chris Trotman',
    author_email='chris@trotman.io',
    description='Salt top state, on steroids.',
)

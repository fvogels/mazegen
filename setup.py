# https://docs.python.org/3/distutils/setupscript.html

from setuptools import setup


def fetch_version():
      '''
      Fetches version variable from version.py
      '''
      version = {}

      with open('mazegen/version.py') as f:
            exec(f.read(), version)

      return version['__version__']



setup(name='mazegen',
      version=fetch_version(),
      description='Maze Generator',
      url='https://github.com/fvogels/mazegen', # Git URL
      author='Frederic Vogels',
      author_email='frederic.vogels@ucll.be',
      license='MIT',
      packages=['mazegen'], # List of packages
      install_requires=[
          'pillow',
      ],
      entry_points = {
            'console_scripts': [ 'mazegen=mazegen.shell:main' ]
      },
      zip_safe=False)

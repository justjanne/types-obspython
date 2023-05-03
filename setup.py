from setuptools import setup

name = "types-obspython"
description = "Typing stubs for obspython"
long_description = '''
## Typing stubs for obspython

This is a PEP 561 type stub package for the `obspython` package. It
can be used by type-checking tools like
[mypy](https://github.com/python/mypy/),
[pyright](https://github.com/microsoft/pyright),
[pytype](https://github.com/google/pytype/),
PyCharm, etc. to check code that uses
`obspython`. The source for this package can be found at
https://github.com/justjanne/types-obspython. All fixes for
types and metadata should be contributed there.
'''.lstrip()

setup(name=name,
      version="29.0.2.2",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/justjanne/types-obspython",
      project_urls={
          "GitHub": "https://github.com/justjanne/types-obspython",
          "Issue tracker": "https://github.com/justjanne/types-obspython/issues",
      },
      install_requires=[],
      packages=['obspython-stubs'],
      package_data={'obspython-stubs': ['__init__.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)

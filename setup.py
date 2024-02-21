from setuptools import setup

setup(
    name='Labyrinthe',
    version='1',
    description='a little project of maze',
    author='Matteo Imbert',

    install_requires=[
        'matplotlib',
        'networkx',
        'pygraphviz',
        ],
    zip_safe=False,
)

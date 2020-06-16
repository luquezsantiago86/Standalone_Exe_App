from setuptools import find_packages
from cx_Freeze import setup, Executable


options = {
    'build_exe': {
        'includes': [
            'cx_Logging', 'idna',
        ],
        'packages': [
            'asyncio', 'flask', 'jinja2', 'dash', 'plotly', 'waitress'
        ],
        'excludes': ['tkinter']
    }
}

executables = [
    Executable('server.py',
               base='Win32GUI',    #'console',
               targetName='app1.exe')
]

setup(
    name='app1',
    packages=find_packages(),
    version='0.0.1',
    description='ms',
    executables=executables,
    options=options
)

# setup.py
from setuptools import setup, find_packages

setup(
    name='PolyGUIX',         # Name of your package
    version='0.1.0',             # Version number
    description='A wrapper for Tkinter and CustomTkinter. Easier to use!', 
    long_description=open('README.md').read(), 
    long_description_content_type='text/markdown', 
    url='https://github.com/striatp/PolyGUIX',  # GitHub URL
    author='Your Name', 
    author_email='sebastien.works@outlook.com', 
    license='MIT', 
    packages=find_packages(),    # Automatically finds all packages in your_package/
    install_requires=[           # Dependencies required for your package
        'tkinter',
        'customtkinter',
        'typing'
    ],
    classifiers=[                # Metadata for your package
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

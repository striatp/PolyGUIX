# setup.py
from setuptools import setup, find_packages

setup(
    name='your_package',         # Name of your package
    version='0.1.0',             # Version number
    description='A wrapper for Tkinter and CustomTkinter', 
    long_description=open('README.md').read(), 
    long_description_content_type='text/markdown', 
    url='https://github.com/yourusername/your_package',  # GitHub URL
    author='Your Name', 
    author_email='youremail@example.com', 
    license='MIT', 
    packages=find_packages(),    # Automatically finds all packages in your_package/
    install_requires=[           # Dependencies required for your package
        'tkinter',
        'customtkinter',
    ],
    classifiers=[                # Metadata for your package
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)

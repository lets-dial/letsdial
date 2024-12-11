from setuptools import setup, find_packages

setup(
    name='letsdial',  # Name of your package
    version='1.0.0',  # Version of your package
    author='Letsdial',  # Your name or the organization's name
    author_email='info@letsdial.com',  # Your email address
    description='A Python package for integrating Letsdial communication services.',
    long_description=open('README.md').read(),  # This will read your README.md for long description
    long_description_content_type='text/markdown',  # Specify the content type of the long description
    url='https://github.com/lets-dial/Letsdial.git',  # Link to your GitHub repository
    packages=find_packages(),  # Automatically find all packages in the project directory
    classifiers=[  # Additional metadata to categorize your project
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    install_requires=[  # List your package's dependencies here
        'requests',  # Example: add requests if your package depends on it
        'numpy',     # Example: if you're using numpy
        # Add any other libraries your project needs
    ],
    python_requires='>=3.7',  # Specify the minimum Python version required
)

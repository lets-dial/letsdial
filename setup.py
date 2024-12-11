from setuptools import setup, find_packages

setup(
    name='letsdial',
    version='0.1.0',  # Update this version based on your release
    author='Letsdial',
    author_email='info@letsdial.com',
    description='A brief description of your letsdial package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',  # If you're using markdown in the README
    url='https://github.com/lets-dial/lets-dial',  # Link to your GitHub repository
    packages=find_packages(),  # Automatically include all packages in the repo
    install_requires=[
        # Add any dependencies your package needs
        'requests',
        'flask',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='cone-core',
    version='0.0.1',
    description='That is a code but it can be used in python',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Stacks crew',
    author_email='stackshado2@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='code',
    packages=find_packages(),
    install_requires=['']
)
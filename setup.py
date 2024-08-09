from setuptools import setup, find_packages

setup(
    name='QIL',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'qiskit',
        'numpy',
        'pandas',
        'tensorflow',
        'stable-baselines3'
    ],
    author='Sean Finney',
    author_email='Finn@MyInfinite.Spcae',
    description='A hybrid quantum-classical language and framework',
    url='https://github.com/MyTruAI/QIL',
    license='MIT'
)

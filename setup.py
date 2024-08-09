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
    author='Your Name',
    author_email='your.email@example.com',
    description='A hybrid quantum-classical language and framework',
    url='https://github.com/yourusername/QIL',
    license='MIT'
)

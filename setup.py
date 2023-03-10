from setuptools import setup, find_packages

setup(
    name='pandas-association',  
    version="0.0.1", 
    python_requires=">=3.10.0",
    description="caluculate association about nominal variables in pandas framework",
    author='nonaka',
    packages=find_packages(),
    license='MIT',
    install_requires=["pandas>=1.5.3", "scipy>=1.10.0", "scikit-learn>=1.2.1", "pytest"],
)
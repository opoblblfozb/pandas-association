from setuptools import setup, find_packages

setup(
    name='pandas-association',  
    version="0.0.1", 
    description="caluculate association about nominal variables in pandas framework",
    author='nonaka',
    packages=find_packages(),
    license='MIT',
    install_requires=["pandas==1.5.3", "scipy==1.10.0"],
    extra_require={
        "dev": ["pytest", "black", "isort"]
    }
)
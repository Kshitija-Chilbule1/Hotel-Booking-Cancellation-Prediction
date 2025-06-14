from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Hotel-Booking-Cancellation-Prediction",
    version="0.1",
    author="KshitijaChilbule",
    packages=find_packages(),
    install_requires = requirements,
)
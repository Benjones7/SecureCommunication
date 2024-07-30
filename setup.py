from setuptools import setup, find_packages

setup(
    name="secure_comm",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
        # Example: 'cryptography'
    ],
    entry_points={
        'console_scripts': [
            'start-server=secure_comm.server:main',
            'start-client=secure_comm.client:main',
        ],
    },
    author="BenJones",
    author_email="ayobamibenjamin@gmail.com",
    description="A secure communication channel using AES encryption.",
    url="https://github.com/Benjones7/SecureCommunication",
)




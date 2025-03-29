from setuptools import setup, find_packages

setup(
    name="loanspeak",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["writer==0.8.2", "ollama==0.4.7"],
    entry_points={
        "console_scripts": [
            "loanspeak=loanspeak:main",
        ],
    },
)

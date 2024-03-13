from setuptools import setup, find_packages

setup(
    name="lpm_discretize",
    description="A library for discretizing dataframes and csf files",
    author="Ulli Schaechtle",
    author_email="ulli@mit.edu",
    packages=["lpm_discretize", "discretize_cli"],  # Automatically find packages in src
    package_dir={"": "src", "discretize_cli": "bin"},
    py_modules=["discretize"],  # Single module in src directory
    install_requires=[
        # XXX:This is solved via flake.nix.
        # Not filling anything in here to avoid duplication.
    ],
    entry_points={
        "console_scripts": [
            "discretize=discretize_cli.discretize:main",
        ],
    },
)

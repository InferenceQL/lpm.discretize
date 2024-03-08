# LPM.discretize

## Overview

A library and CLI tool for taking CSV files producing new CSV files where all
numerical columns have been discretized.

## Disclaimer
:warning: The purpose of the current version for this README.md is README-driven
development. The software does not work yet!

This is going pre-alpha software. We are currently testing it in real-world scenarios. In its present state, we discourage users from trying it.

## Installation

This library is packaged with [Nix Flakes](https://nixos.wiki/wiki/Flakes).
Include this as a Python module in your Flakes file or use the CLI directly (see
examples below).

## Usage


### Using LPM.discretize as a Python library

```python
# Get dependencies.
import polars as pl

from lpm_fidelity.distances import bivariate_distances_in_data
from lpm_fidelity.distances import univariate_distances_in_data
from lpm_fidelity.two_sample_testing import univariate_two_sample_testing_in_data

# Read in three csv files.
df_a = pl.read_csv("real-data.csv")
df_b = pl.read_csv("synthetic-data-lpm.csv")
df_c = pl.read_csv("synthetic-data-baseline.csv")

# Get discretized version of the dataframes above. Use Polar's types do decide what to discretize.
# By default, this discretizes with based on quartiles in `df_a`.
df_a_discretized, df_b_discretized, df_c_discretized =  discretize([df_a, df_b, df_c])

# Get discretized version of the dataframes above. Discretize column `foo`.
Below use a schema formatted like the standard output for inferenceQL structure learning.
df_a_discretized, df_b_discretized, df_c_discretized =  discretize(
    [df_a, df_b, df_c],
    {"foo":Keyword(numerical), "bar":Keyword(numerical)}
)
```
See docstrings for other usage patterns.

### LPM.discretize CLI

Usage information for the CLI can be printed with the following command.
```shell
nix run github:InferenceQL/lpm.discretize --help
```

Usage information for the CLI can be printed with the following command.
```shell
nix run github:InferenceQL/lpm.discretize -- --data real-data.csv --data synthetic-data-lpm.csv --data synthetic-data-baseline.csv
```

Assess univariate probabilistic distance metrics.
```shell
nix run . -- --data-1 foo.csv --data-2 bar.csv
```

## Test

Tests are automatically run through the flakes file.

During development, uses can either add Pytest to the flakes output and use the Nix shell:
```shell
nix develop -c  pytest tests/ -vvv
```
or they install the library globally.
```shell
python -m pip install --upgrade --force-reinstall  . && pytest tests/ -vvv
```
The latter worflow depends on pip and pytest being available globablly, too.


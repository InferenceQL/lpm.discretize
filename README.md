# LPM.discretize

## Overview

A library and CLI tool for taking CSV files producing new CSV files where all
numerical columns have been discretized.

## Disclaimer
This is pre-alpha software. We are currently testing it in real-world scenarios. In its present state, we discourage users from trying it.

## Installation

This library is packaged with [Nix Flakes](https://nixos.wiki/wiki/Flakes).
Include this as a Python module in your Flakes file or use the CLI directly (see
examples below).

## Usage

Users can discretize a single dataframe or a list of dataframes.

If multiple dataframes are supplied, one will be used as a reference point. This
is necessary for example when quantile based discretization is applied.

They can supply custom functions for discretization or use quantile-based discretization.

### Using LPM.discretize as a Python library

#### Discretize a single dataframe based on quantiles
Tak a single dataframe and discretize numerical columns based on a quantiles:
```python
# Get dependencies.
import polars as pl
from lpm_discretize import discretize_df_quantiles

# Read a csv files.
df = pl.read_csv("data.csv")

# Discretize this dataframe; all columns are discretized based on 4 quantiles. 
df_discretized =  discretize_df_quantiles(df, quantiles=4)
```
Users can list which columns will be discretized. Let's discretize only `foo` and
`bar`.
```python
df_discretized =  discretize_df_quantiles(df, quantiles=4, columns=["foo", "bar"])
```

Note that the `quantiles` argument here is overloaded. Users can supply an int to set the
number of quantiles for every column, or they supply a dictionary.
```python
df_discretized =  discretize_df_quantiles(df, quantiles={"foo": 4, "bar": 2}))
```

#### Discretize a single dataframe based on a map columns->discretization-functions

Users can supply their own discretization functions as dictionaries.
```python
from lpm_discretize import discretize_df
discretize(df, discretization_functions={"foo": lambda x: "yes" if x <= 1 else "no", "bar": lambda x: "ja" if x <= 6 else "nein"})
```

Of course, this can be wrapped into a list comprehension discretizing multiple dataframes.

#### Discretizing multiple dataframes based on quantiles

```python
import polars as pl
from lpm_discretize import discretize_df_quantiles

# Read three csv files.
df_a = pl.read_csv("real-data.csv")
df_b = pl.read_csv("synthetic-data-lpm.csv")
df_c = pl.read_csv("synthetic-data-baseline.csv")

# Get discretized version of the dataframes above. Use Polar's types do decide what to discretize.
# By default, this discretizes with based on quartiles in `df_a`.
df_a_discretized, df_b_discretized, df_c_discretized =  discretize_quantiles([df_a, df_b, df_c], quantiles=4)
```

```python
Below use a list of columns to discretize
df_a_discretized, df_b_discretized, df_c_discretized =  discretize_quantiles(
    [df_a, df_b, df_c],
    quantiles=4,
    columns=["foo", "bar"]
)
```



See docstrings for other usage patterns.

### LPM.discretize CLI

Usage information for the CLI can be printed with the following command.
```shell
nix run github:InferenceQL/lpm.discretize --help
```

Usage information for the CLI can be printed with the following command, this
internally invokes `discretize_df_quantiles`.
```shell
nix run github:InferenceQL/lpm.discretize -- --data data.csv
```

For customization purposes, we expect users to use this tool as a Python
library. See above.

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


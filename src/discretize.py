import polas as pl

def _readable_category_name(idx, lower_bound=None, upper_bound=None):
    """
    Description:
        Create a readable category name based on upper and lower bounds.

    Parameters:
    - idx (int):  will translate to a letter.
    - lower_bound (float): lower bound of the category.
    - upper_bound (float): upper bound of the category.

    Returns:
        A string with a readable category name, including an alphabetical index,
        if index is <= 26 (index > 26 should be a rare case for bound-based
        categorization; so having it work - yet slightly less readable seems
        fine).
     """
     assert (lower_bound is not None) or (upper_bound is not None), \
             "At least one bound needs to be defined!"


def _get_quantile_based_discretization_function(column, quantiles=4):
    """
    Description:
        Takes a reference column that downn the road needs to be discretized and
        returns a function can be used for that. Relies on Polar's qcut
        discretization but retuns a function that can easily be re-used
        and returns human-readable output.

    Parameters:
    - colummn (Polars series or list):  A sequence
    - quantile (int): The number of quantiles used for discretization (default =
      4).

    Returns:
        A function that can be applied to a column for discretization.
     """


def discretize_column(column, discretization_function):
    """
    Description:
        Discretize a numerical column

    Parameters:
    - colummn (Polars series or list):  A sequence
    - discretization_function (function): A functoin that processes the numerical values and
                                          discretizes them.

    Returns:
        A new list with discretized values

    Examples:
    >>> discretize_column([1,2,1], lambda x: "yes" if x <= 1 else "no")
        ["yes", "no", "yes"]

    >>> discretize_column([1,2,3,4], lambda xs: pl.Series(xs).qcut(4))
        [
            "(-inf, 1.75]",
            "(1.75, 2.5]",
            "(2.5, 3.25]",
            "(3.25, inf]"
        ]
     """


def discretize_df(df, discretization_functions):
    """
    Description:
        Discretize all numerical columns in a Polars dataframe.

    Parameters:
    - df (Polars dataframe):  A Polars dataframe for which a subset of columns
                              need to be discretized.
    - discretization_functions (dict):
        - a dict from column name to functions, to apply different
          discretization schemes for different columns.

    Returns:
        A new Polars dataframe, where numerical columns are discretized.

    Examples:
    >>> print(df)
        ┌─────┬─────┬─────┬─────┐
        │ foo ┆ bar ┆ ... ┆ baz │
        │ --- ┆ --- ┆ --- ┆ --- │
        │ f64 ┆ i64 ┆ ... ┆ str │
        ╞═════╪═════╪═════╪═════╡
        │ 1.0 ┆ 8   ┆ ... ┆ x   │
        │ 2.0 ┆ 7   ┆ ... ┆ y   │
        │ 3.0 ┆ 6   ┆ ... ┆ x   │
        │ 4.0 ┆ 5   ┆ ... ┆ x   │
        └─────┴─────┴─────┴─────┘

    >>> discretize(df, discretization_scheme={
        "foo": lambda x: "yes" if x <= 1 else "no",
        "bar": lambda x: "ja" if x <= 6 else "nein"})
        ┌───────┬────────┬─────┬─────┐
        │ foo   ┆ bar    ┆ ... ┆ baz │
        │ ---   ┆ ---    ┆ --- ┆ --- │
        │ str   ┆ str    ┆ ... ┆ str │
        ╞═══════╪════════╪═════╪═════╡
        │ "yes" ┆ "nein" ┆ ... ┆ x   │
        │ "no"  ┆ "nein" ┆ ... ┆ y   │
        │ "no"  ┆ "ja"   ┆ ... ┆ x   │
        │ "no"  ┆ "ja"   ┆ ... ┆ x   │
        └───────┴────────┴─────┴─────┘
    """

def discretize(dataframes, reference_idx=0, discretization_scheme=4, schema=None):
    """
    Description:
        Discretize all numerical columns in a list of dataframes supplied. One
        dataframe in the list is chosen as a reference for empirical
        discretization, e.g. based on quantiles (see parameter reference_idx
        below).

    Parameters:
    - dataframes (list):  A list of Polars dataframes.
    - reference_idx (int): Which of these dataframes should be the reference point for
      empirical discretization (e.g. based on quantiles).
    - discretization_scheme (int | function | dict): either
        - a int n, discretizing all columns into n quantiles (default, n=4, corresponding to quartiles).
        - a function, discretizing all numerical columns using this function.
        - a dict from column name to ints or functions, to apply different
          discretization schemes for different columns.
    - schema:  A map indicating statistical types for columns
      (optional, default: Statistical types are guessed based on Polars' types).

    Returns:
        A list of Polars dataframes, where numerical columns are discretized.

    Examples:
    >>> print(dfs)
        [
            ┌─────┬─────┬─────┬─────┐
            │ foo ┆ bar ┆ ... ┆ baz │
            │ --- ┆ --- ┆ --- ┆ --- │
            │ f64 ┆ i64 ┆ ... ┆ str │
            ╞═════╪═════╪═════╪═════╡
            │ 1.0 ┆ 8   ┆ ... ┆ x   │
            │ 2.0 ┆ 7   ┆ ... ┆ y   │
            │ 3.0 ┆ 6   ┆ ... ┆ x   │
            │ 4.0 ┆ 5   ┆ ... ┆ x   │
            └─────┴─────┴─────┴─────┘,
            ┌─────┬─────┬─────┬─────┐
            │ foo ┆ bar ┆ ... ┆ baz │
            │ --- ┆ --- ┆ --- ┆ --- │
            │ f64 ┆ i64 ┆ ... ┆ str │
            ╞═════╪═════╪═════╪═════╡
            │ 4.0 ┆ 5   ┆ ... ┆ z   │
            │ 2.0 ┆ 7   ┆ ... ┆ y   │
            │ 3.0 ┆ 6   ┆ ... ┆ z   │
            │ 4.0 ┆ 5   ┆ ... ┆ x   │
            └─────┴─────┴─────┴─────┘,
            ...
        ]

    >>> discretize(dfs)
        [
            ┌─────────────────────────┬──────────────────────────┬─────┬─────┐
            │ foo                     ┆ bar                      ┆ ... ┆ baz │
            │ ---                     ┆ ---                      ┆ --- ┆ --- │
            │ str                     ┆ str                      ┆ ... ┆ str │
            ╞═════════════════════════╪══════════════════════════╪═════╪═════╡
            │ "(a) Very Low (≤ 1.75)" ┆ "(d) Very High (> 7.25)" ┆ ... ┆ x   │
            │ "(b) Low (1.75 - 2.5)"  ┆ "(c) High (6.5 - 7.25)"  ┆ ... ┆ y   │
            │ "(c) High (2.5 - 3.25)" ┆ "(b) Low (5.75 - 6.5)"   ┆ ... ┆ x   │
            │ "(d) Very High (> 3.25)"┆ "(a) Very Low (≤ 5.75)"  ┆ ... ┆ x   │
            └─────────────────────────┴──────────────────────────┴─────┴─────┘,
            ┌─────────────────────────┬──────────────────────────┬─────┬─────┐
            │ foo                     ┆ bar                      ┆ ... ┆ baz │
            │ ---                     ┆ ---                      ┆ --- ┆ --- │
            │ str                     ┆ str                      ┆ ... ┆ str │
            ╞═════════════════════════╪══════════════════════════╪═════╪═════╡
            │ "(d) Very High (> 3.25)"┆ "(a) Very Low (≤ 5.75)"  ┆ ... ┆ z   │
            │ "(b) Low (1.75 - 2.5)"  ┆ "(c) High (6.5 - 7.25)"  ┆ ... ┆ y   │
            │ "(c) High (2.5 - 3.25)" ┆ "(b) Low (5.75 - 6.5)"   ┆ ... ┆ z   │
            │ "(d) Very High (> 3.25)"┆ "(a) Very Low (≤ 5.75)"  ┆ ... ┆ x   │
            └─────────────────────────┴──────────────────────────┴─────┴─────┘,
        ...
        ]

    >>> discretize(dfs, discretization_scheme=2)
        [
            ┌─────────────────────┬─────────────────────┬─────┬─────┐
            │ foo                 ┆ bar                 ┆ ... ┆ baz │
            │ ---                 ┆ ---                 ┆ --- ┆ --- │
            │ str                 ┆ str                 ┆ ... ┆ str │
            ╞═════════════════════╪═════════════════════╪═════╪═════╡
            │ "(a) Low (≤ 2.5)"   ┆ "(b) High (> 6.5 )" ┆ ... ┆ x   │
            │ "(a) Low (≤ 2.5)"   ┆ "(b) High (> 6.5 )" ┆ ... ┆ y   │
            │ "(b) High (> 2.5 )" ┆ "(a) Low (≤ 2.5)"   ┆ ... ┆ x   │
            │ "(b) High (> 2.5 )" ┆ "(a) Low (≤ 2.5)"   ┆ ... ┆ x   │
            └─────────────────────┴─────────────────────┴─────┴─────┘,
            ┌─────────────────────┬─────────────────────┬─────┬─────┐
            │ foo                 ┆ bar                 ┆ ... ┆ baz │
            │ ---                 ┆ ---                 ┆ --- ┆ --- │
            │ str                 ┆ str                 ┆ ... ┆ str │
            ╞═════════════════════╪═════════════════════╪═════╪═════╡
            │ "(b) High (> 2.5 )" ┆ "(a) Low (≤ 2.5)"   ┆ ... ┆ x   │
            │ "(a) Low (≤ 2.5)"   ┆ "(b) High (> 6.5 )" ┆ ... ┆ y   │
            │ "(b) High (> 2.5 )" ┆ "(a) Low (≤ 2.5)"   ┆ ... ┆ x   │
            │ "(b) High (> 2.5 )" ┆ "(a) Low (≤ 2.5)"   ┆ ... ┆ x   │
            └─────────────────────┴─────────────────────┴─────┴─────┘,
        ...
        ]

    >>> discretize(dfs, discretization_scheme={"foo":4, "bar":2})
        [
            ┌─────────────────────────┬─────────────────────┬─────┬─────┐
            │ foo                     ┆ bar                 ┆ ... ┆ baz │
            │ ---                     ┆ ---                 ┆ --- ┆ --- │
            │ str                     ┆ str                 ┆ ... ┆ str │
            ╞═════════════════════════╪═════════════════════╪═════╪═════╡
            │ "(a) Very Low (≤ 1.75)" ┆ "(b) High (> 6.5 )" ┆ ... ┆ x   │
            │ "(b) Low (1.75 - 2.5)"  ┆ "(b) High (> 6.5 )" ┆ ... ┆ y   │
            │ "(c) High (2.5 - 3.25)" ┆ "(a) Low (≤ 2.5)"   ┆ ... ┆ x   │
            │ "(d) Very High (> 3.25)"┆ "(a) Low (≤ 2.5)"   ┆ ... ┆ x   │
            └─────────────────────────┴─────────────────────┴─────┴─────┘,
            ┌─────────────────────────┬─────────────────────┬─────┬─────┐
            │ foo                     ┆ bar                 ┆ ... ┆ baz │
            │ ---                     ┆ ---                 ┆ --- ┆ --- │
            │ str                     ┆ str                 ┆ ... ┆ str │
            ╞═════════════════════════╪═════════════════════╪═════╪═════╡
            │ "(d) Very High (> 3.25)"┆ "(a) Low (≤ 2.5)"   ┆ ... ┆ x   │
            │ "(b) Low (1.75 - 2.5)"  ┆ "(b) High (> 6.5 )" ┆ ... ┆ y   │
            │ "(c) High (2.5 - 3.25)" ┆ "(a) Low (≤ 2.5)"   ┆ ... ┆ x   │
            │ "(d) Very High (> 3.25)"┆ "(a) Low (≤ 2.5)"   ┆ ... ┆ x   │
            └─────────────────────────┴─────────────────────┴─────┴─────┘,
        ...
        ]
    >>> discretize(dfs, discretization_scheme={"foo": lambda x: "yes" if x <= 1 else "no", "bar":2})
        [
            ┌───────┬─────────────────────┬─────┬─────┐
            │ foo   ┆ bar                 ┆ ... ┆ baz │
            │ ---   ┆ ---                 ┆ --- ┆ --- │
            │ str   ┆ str                 ┆ ... ┆ str │
            ╞═══════╪═════════════════════╪═════╪═════╡
            │ "yes" ┆ "(b) High (> 6.5 )" ┆ ... ┆ x   │
            │ "no"  ┆ "(b) High (> 6.5 )" ┆ ... ┆ y   │
            │ "no"  ┆ "(a) Low (≤ 2.5)"   ┆ ... ┆ x   │
            │ "no"  ┆ "(a) Low (≤ 2.5)"   ┆ ... ┆ x   │
            └───────┴─────────────────────┴─────┴─────┘,
            ┌───────┬─────────────────────┬─────┬─────┐
            │ foo   ┆ bar                 ┆ ... ┆ baz │
            │ ---   ┆ ---                 ┆ --- ┆ --- │
            │ str   ┆ str                 ┆ ... ┆ str │
            ╞═══════╪═════════════════════╪═════╪═════╡
            │ "no"  ┆ "(a) Low (≤ 2.5)"   ┆ ... ┆ x   │
            │ "no"  ┆ "(b) High (> 6.5 )" ┆ ... ┆ y   │
            │ "no"  ┆ "(a) Low (≤ 2.5)"   ┆ ... ┆ x   │
            │ "no"  ┆ "(a) Low (≤ 2.5)"   ┆ ... ┆ x   │
            └───────┴─────────────────────┴─────┴─────┘,
        ...
        ]

    """
    # Check that the columns agree.
    for df in dataframes[1:]
        assert set(df.columns) == set(dataframes[0].columns)

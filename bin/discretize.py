import argparse
import polars as pl

from lpm_discretize import discretize_df_quantiles


def main():
    """Main function for discretizing a single csv file from the commandline."""
    description = "Discretize a dataframe based on quantiles"
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument("-d", "--data", type=str, help="Path to a CSV.")
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        help="Path to output CSV - prints to stdout if not set.",
        default=None,
    )
    parser.add_argument(
        "--quantiles", type=int, help="number of quantiles used", default=4
    )
    parser.add_argument(
        "--decimals",
        type=int,
        help="number of decimals reported regarding quantiles",
        default=1,
    )

    args = parser.parse_args()

    df = pl.read_csv(args.data)

    result = discretize_df_quantiles(
        df, quantiles=args.quantiles, decimals=args.decimals
    )

    if args.output is None:  # Print to stdout.
        print(result.write_csv(args.output))
    else:
        result.write_csv(args.output)


if __name__ == "__main__":
    main()

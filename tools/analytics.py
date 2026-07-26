import pandas as pd
from langchain.tools import tool


def to_dataframe(result: dict):
    return pd.DataFrame(
        result["rows"],
        columns=result["columns"]
    )


@tool
def dataframe_summary(result: dict):
    """
    Returns summary statistics for a dataset.
    """

    df = to_dataframe(result)

    return {
        "shape": df.shape,
        "columns": df.columns.tolist(),
        "summary": df.describe(include="all").to_string()
    }


@tool
def missing_values(result: dict):
    """
    Returns missing values per column.
    """

    df = to_dataframe(result)

    return df.isnull().sum().to_dict()


@tool
def correlation_matrix(result: dict):
    """
    Computes correlation between numeric columns.
    """

    df = to_dataframe(result)

    numeric = df.select_dtypes(include="number")

    if numeric.empty:
        return "No numeric columns."

    return numeric.corr().round(2).to_dict()


@tool
def group_statistics(result: dict, group_by: str, value: str):
    """
    Computes grouped statistics.
    """

    df = to_dataframe(result)

    output = (
        df.groupby(group_by)[value]
        .agg(["count", "sum", "mean", "min", "max"])
        .reset_index()
    )

    return output.to_dict(orient="records")


@tool
def statistics(result: dict):
    """
    Returns descriptive statistics.
    """

    df = to_dataframe(result)

    return df.describe(include="all").to_string()
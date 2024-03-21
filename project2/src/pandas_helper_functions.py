import holoviews as hv


def subset_rows_where(df, column, value, operator="=="):
    """Return a subset of rows where the condition is met."""

    import operator

    ops = {
        "==": operator.eq,
        "!=": operator.ne,
        ">": operator.gt,
        "<": operator.lt,
        ">=": operator.ge,
        "<=": operator.le,
    }

    if operator not in ops:
        raise ValueError(f"Operator {operator} not supported.")
    else:
        op = ops.get(operator)
        return df[op(df[column], value)]


def holoviews_histplot(df, column, mean=False, median=False, mode=False, bins=20):
    """Return a Holoviews histogram plot."""
    hist = hv.Histogram(df[column], bins=bins)
    plot = hist.opts(
        title=f"Histogram of {column}",
        xlabel=column,
        ylabel="Frequency",
        width=600,
        height=400,
    )

    if mean:
        mean = df[column].mean()
        plot *= hv.VLine(mean).opts(color="red", line_dash="dashed")
    if median:
        median = df[column].median()
        plot *= hv.VLine(median).opts(color="green", line_dash="dashed")
    if mode:
        mode = df[column].mode().values[0]
        plot *= hv.VLine(mode).opts(color="blue", line_dash="dashed")

    return plot

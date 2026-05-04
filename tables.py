import pandas as pd
from rich.console import Console
from rich.table import Table
from rich import box

def print_df(df, title="Data Summary", show_index=True):
    console = Console()
    
    table = Table(
            title=f"[bold magenta]{title}[/bold magenta]",
            box=box.ROUNDED,
            header_style="bold cyan",
            row_styles=["none", "dim"],
            title_justify="left"
        )
    
    if show_index:
        # Use the index name if it exists, otherwise default to "Index"
        index_name = str(df.index.name) if df.index.name is not None else ""
        table.add_column(index_name, justify="right", style="italic white", no_wrap=True)

    for column in df.columns:
        if pd.api.types.is_numeric_dtype(df[column]):
            table.add_column(column, justify="right", style="green")
        else:
            table.add_column(column, justify="left")

    for row in df.itertuples(index=show_index):
        # Convert all elements to strings for Rich
        table.add_row(*[str(item) for item in row])

    console.print(table)
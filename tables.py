import pandas as pd
from rich.console import Console
from rich.table import Table
from rich import box

def print_df(df, title="Data Summary"):
    console = Console()
    
    table = Table(
        title=f"[bold magenta]{title}[/bold magenta]",
        box=box.ROUNDED,
        header_style="bold cyan",
        row_styles=["none", "dim"],
        title_justify="left",
        show_lines=False
    )

    for column in df.columns:
        if pd.api.types.is_numeric_dtype(df[column]):
            table.add_column(column, justify="right", style="green")
        else:
            table.add_column(column, justify="left")

    for _, row in df.iterrows():
        # Convert all elements to strings for Rich
        table.add_row(*[str(item) for item in row])

    console.print(table)
"""A module that performs basic math operations."""

import altair as alt
import pandas as pd

alt.renderers.enable("png", scale_factor=2, ppi=144)


def plot_pyramid():
    category = ["Sky", "Shady side of a pyramid", "Sunny side of a pyramid"]
    color = ["#416D9D", "#674028", "#DEAC58"]
    df = pd.DataFrame({"category": category, "value": [75, 10, 15]})

    alt.Chart(df, width=150, height=150).mark_arc(outerRadius=80).encode(
        alt.Theta("value:Q").scale(range=[2.356, 8.639]),
        alt.Color("category:N")
        .title(None)
        .scale(domain=category, range=color)
        .legend(orient="none", legendX=160, legendY=50),
        order="value:Q",
    ).configure_view(strokeOpacity=0).save("pyramid.png")

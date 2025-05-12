import plotly.graph_objects as go

# Sample data
tropes = [
    "Enemies to Lovers",
    "Friends to Lovers",
    "Fake Dating",
    "Grumpy x Sunshine",
    "Forced Proximity",
    "Love Triangle",
    "Second Chance",
    "Forbidden Love"
]

rating = [10, 5, 7, 6, 8, 4, 9, 3]  # Percentages

# Create bar chart
fig = go.Figure(
    data=[go.Bar(x=tropes, y=rating, marker_color='indianred')],
    layout=go.Layout(
        title="My Rating of Romance Tropes",
        xaxis=dict(title="Trope"),
        yaxis=dict(title="Rating"),
    )
)

# Show plot
fig.show()

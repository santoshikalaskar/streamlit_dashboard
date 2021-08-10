import pandas as pd
import plotly.express as px
import streamlit as st

class Dashboard:
    def __init__(self):
        pass

    @st.cache
    def load_datset(self):
        cities_df = pd.read_csv("all_courier_data.csv")
        return cities_df

    def plot_map(self, cities_df):
        fig = px.scatter_mapbox(cities_df,
                                lat="LAT",
                                lon="LON",
                                hover_name="Location",
                                hover_data=["DoctorCity", "postal_code"],
                                zoom=6,
                                height=400)
        fig.update_layout(mapbox_style="open-street-map")
        fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 10})
        return fig

if __name__ == "__main__":
    dash_obj = Dashboard()
    st.title("Dashboard")
    cities_df = dash_obj.load_datset()
    st.write(cities_df.head(10))
    st.markdown("**scatter_mapbox**")
    fig = dash_obj.plot_map(cities_df)
    st.plotly_chart(fig)
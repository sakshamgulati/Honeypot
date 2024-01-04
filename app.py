import streamlit as st
import pandas as pd
from utils import feature_engineering
import plotly.express as px


# Load the data from honeypot.json
data = pd.read_json("data/honeypot.json")


# Create the Streamlit app
def main():
    # Create three columns

    # Place the image in the first column

    st.image("images/coalition.png")

    # Place the title in the second column

    st.title("Take Home Assessment")
    # create a subtitle
    st.subheader("Curated By: Saksham Gulati")
    # add a description to the title
    st.text(
        "This is a simple app to display high-level information about the honey pot project. For more details please visit:https://colab.research.google.com/drive/123jgxOuIuBkQliNkBXmsA_vSJiRfJbHm?usp=sharing"
    )

    # Leave the third column empty

    # Display the data
    feature_rich_df = feature_engineering(data)
    col1, col2 = st.columns(2)
    tags_filter = col1.multiselect(
        "Select type of Attack:",
        options=list(feature_rich_df["tags"].unique()),
        default=list(["TCP_SYN", "RDP_SCANNER"]),
    )
    col1.markdown("""---""")
    attack_from_location_filter = col2.multiselect(
        "Select Country where attack originated from:",
        options=list(feature_rich_df["country_name_1"].unique()),
        default=list(["China", "Netherlands"]),
    )
    col2.markdown("""---""")
    hour_filter = col1.multiselect(
        "Select hour of Attack:",
        options=list(feature_rich_df["hour"].unique()),
        default=list([22]),
    )
    col1.markdown("""---""")
    proxy_filter = col2.multiselect(
        "Select proxy:",
        options=list(feature_rich_df["proxy_type"].unique()),
        default=list(["DCH", "VPN"]),
    )
    col2.markdown("""---""")
    attack_to_location_filter = col2.multiselect(
        "Select Country which was attacked:",
        options=list(feature_rich_df["country_name"].unique()),
        default=list(["Hong Kong", "United Arab Emirates"]),
    )

    port_filter = col1.multiselect(
        "Select Port bucket of attack:",
        options=list(feature_rich_df["port_bucket"].unique()),
        default=list(["Well-known Ports", "Registered Ports", "Dynamic/Private Ports"]),
    )

    filtered_data = feature_rich_df[
        feature_rich_df["tags"].isin(tags_filter)
        & feature_rich_df["country_name_1"].isin(attack_from_location_filter)
        & feature_rich_df["hour"].isin(hour_filter)
        & feature_rich_df["country_name"].isin(attack_to_location_filter)
        & feature_rich_df["port_bucket"].isin(port_filter)
        & feature_rich_df["proxy_type"].isin(proxy_filter)
    ]
    minute_data = filtered_data.groupby("minute").size().to_frame("freq").reset_index()
    attacks_per_min = px.line(
        minute_data, x="minute", y="freq", title="Attacks per minute"
    )
    st.plotly_chart(attacks_per_min)
    col3, col4 = st.columns(2)
    col3.write(
        filtered_data["tags"]
        .value_counts()
        .to_frame("Frequency")
        .reset_index()
        .sort_values(by=["Frequency"], ascending=False)
        .head(5)
    )
    # Use st.plotly_chart() to display the plot

    chart_type = col4.radio(
        "Select visualization", ("Attack Originating from:", "Attacked")
    )
    if chart_type == "Attack Originating from:":
        attack_from = (
            filtered_data.groupby("country_name_1")
            .size()
            .to_frame("freq")
            .reset_index()
            .sort_values(by=["freq"], ascending=False)
        )
        attacks_per_country = px.choropleth(
            attack_from,
            locations="country_name_1",
            locationmode="country names",
            color="freq",
            hover_name="country_name_1",
            scope="world",
        )
        st.plotly_chart(attacks_per_country)
    else:
        attack_to = (
            filtered_data.groupby("country_name")
            .size()
            .to_frame("freq")
            .reset_index()
            .sort_values(by=["freq"], ascending=False)
        )
        attacks_per_country = px.choropleth(
            attack_to,
            locations="country_name",
            locationmode="country names",
            color="freq",
            hover_name="country_name",
            scope="world",
        )
        st.plotly_chart(attacks_per_country)
    st.text(
        "This is a simple app to display high-level information about the honey pot project. For more details please visit:https://colab.research.google.com/drive/123jgxOuIuBkQliNkBXmsA_vSJiRfJbHm?usp=sharing"
    )
    table = (
        filtered_data.groupby(["ip", "proxy_type", "port"])
        .size()
        .to_frame("Scanned_Counts")
        .reset_index()
        .sort_values(by=["Scanned_Counts"], ascending=False)
        .head(10)
    )
    st.dataframe(table, use_container_width=True)


if __name__ == "__main__":
    main()

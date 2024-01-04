import streamlit as st
import pandas as pd
from utils import feature_engineering

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
    st.subheader("By: Saksham Gulati")
    # add a description to the title
    st.text("This is a simple app to display high-level information about the project")

    # Leave the third column empty

    # Display the data
    feature_rich_df = feature_engineering(data)

    st.write(feature_rich_df)


if __name__ == "__main__":
    main()

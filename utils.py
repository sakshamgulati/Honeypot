import pandas as pd
import numpy as np
import logging
import ipaddress
import json
import urllib.request
from urllib.request import urlopen
import json


def feature_engineering(data):
    logging.basicConfig(
        level=logging.INFO,  # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        format="%(asctime)s - %(levelname)s - %(message)s",
        force=True,
    )
    logging.info("Data Loaded!")
    exploded_data = data.explode("tags")
    logging.info(
        f"rows of our new data:{exploded_data.shape[0]}, earlier rows:{data.shape[0]}"
    )
    exploded_data["port_bucket"] = exploded_data["port"].apply(
        lambda x: "Well-known Ports"
        if x <= 1023
        else (
            "Registered Ports" if x >= 1024 and x < 49151 else "Dynamic/Private Ports"
        )
    )
    unique_as = list(exploded_data["as_num"].unique())
    asn_lookup = pd.DataFrame(unique_as, columns=["as_numbers"])
    asn_location = [
        "MICROSOFT-CORP-MSN-AS-BLOCK, US",
        "AMAZON-AES, US",
        "GOOGLE-CLOUD-PLATFORM, US",
        "AKAMAI-LINODE-AP Akamai Connected Cloud, SG",
        "ALIBABA-CN-NET Hangzhou Alibaba Advertising Co.,Ltd., CN",
        "ALIBABA-CN-NET Alibaba US Technology Co., Ltd., CN",
        "AMAZON-02, US",
        "DIGITALOCEAN-ASN, US",
    ]
    asn_lookup["as_description"] = asn_location
    exploded_data = pd.merge(
        asn_lookup,
        exploded_data,
        left_on=["as_numbers"],
        right_on=["as_num"],
        how="inner",
    )
    logging.info("AS numbers extracted")
    logging.info("Subnet values extracted")
    exploded_data["hour"] = exploded_data["timestamp"].dt.hour
    exploded_data["date"] = exploded_data["timestamp"].dt.date
    exploded_data["minute"] = exploded_data["timestamp"].dt.minute

    exploded_data["hour_minute"] = exploded_data["timestamp"].dt.strftime("%H-%M")
    exploded_data.sort_values(by=["timestamp"], inplace=True)
    logging.info(f"The only date present:{exploded_data.date.unique()}")
    logging.info("Date and Time values extracted")
    return exploded_data

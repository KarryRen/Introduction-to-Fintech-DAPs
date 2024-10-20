# -*- coding: utf-8 -*-
# @Time    : 2024/10/11 18:22
# @Author  : Karry Ren

""" Concat data of all Codes. """

import pandas as pd
import os

# ---- Get the data file ---- #
daily_freq_trading_data_file_list = sorted(os.listdir("../../../../Data/daily_trading_factors/raw_data/"))
concat_df = pd.DataFrame()

# ---- For loop to collect ---- #
df_list = []
for i, data_file in enumerate(daily_freq_trading_data_file_list):
    daily_freq_trading_df = pd.read_csv(f"../../../../Data/daily_trading_factors/raw_data/{data_file}")
    assert str(daily_freq_trading_df["Date"].iloc[0]) == "20100104" and str(daily_freq_trading_df["Date"].iloc[-1]) == "20240531"
    df_list.append(daily_freq_trading_df)

# ---- Concat the df ---- #
concat_df = pd.concat(df_list)
print(concat_df)
concat_df.to_csv("../../../../Data/daily_trading_factors/processed_factors/raw_daily_trading_values.csv", index=False)
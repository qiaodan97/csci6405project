import pandas as pd

df = pd.read_csv("D:\\winter2023\\CSCI6405\\project\\processed_dataset\\"
                  "Gross domestic product, expenditure-based, (Yukon_1991_2022).csv")
df_years = pd.DataFrame()

for year in range(1991, 2023):
    year_str = str(year)
    quarter_cols = [f"Q{i} {year_str}" for i in range(1, 5)]
    year_sum = df[quarter_cols].replace(",", "", regex=True).astype(int).sum(axis=1)
    df_years[year_str] = year_sum

drop_cols = []
for year in range(1991, 2023):
    year_str = str(year)
    quarter_cols = [f"Q{i} {year_str}" for i in range(1, 5)]
    drop_cols.extend(quarter_cols)
df = df.drop(columns=drop_cols)

df_concat = pd.concat([df, df_years], axis=1)
df_concat = df_concat.drop(columns=["2022"])

df_concat.to_csv("D:\\winter2023\CSCI6405\\project\\processed_dataset_new\\"
                 "Yukon_gdp_yearly.csv", index=False)
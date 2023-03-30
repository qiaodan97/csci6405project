import pandas as pd
import numpy as np

file_name = "NewfoundlandAndLabrador"
province = "Newfoundland and Labrador"
is_terrotory = False
# read in the CSV files
# education
df2 = pd.read_csv("D:\\winter2023\\CSCI6405\\project\\processed_dataset\\"
                  "Number of students in elementary and secondary schools("+file_name+"_1997_2021).csv")
df2.set_index(df2.columns[0], inplace=True)
prefix = '2_Number of students in elementary and secondary schools_'
new_index = {old_index: prefix + old_index for old_index in df2.index}
df2.rename(index=new_index, inplace=True)

df3 = pd.read_csv("D:\\winter2023\\CSCI6405\\project\\processed_dataset\\"
                  "Number of full-time and part-time educators (2002_2017).csv")
df3.set_index(df3.columns[0], inplace=True)
prefix = '3_Number of full-time and part-time educators_'
new_index = {old_index: prefix + old_index for old_index in df3.index}
df3.rename(index=new_index, inplace=True)

df9 = pd.read_csv("D:\\winter2023\\CSCI6405\\project\\processed_dataset\\"
                  "Postsecondary enrolments(EachProvince_1992_2021).csv")
df9.set_index(df9.columns[0], inplace=True)
prefix = '9_Postsecondary enrolments_'
new_index = {old_index: prefix + old_index for old_index in df9.index}
df9.rename(index=new_index, inplace=True)

# economics
df1 = pd.read_csv("D:\\winter2023\\CSCI6405\\project\\processed_dataset\\"
                  "Live births("+file_name+"_1991_2021).csv")
df1.set_index(df1.columns[0], inplace=True)
prefix = '1_Live births_'
new_index = {old_index: prefix + old_index for old_index in df1.index}
df1.rename(index=new_index, inplace=True)

# for federal
if province == "Canada":
    df4 = pd.read_csv("D:\\winter2023\CSCI6405\\project\\processed_dataset_new\\"
                 "Canada_gdp_yearly.csv")
# for province
else:
    df4 = pd.read_csv("D:\\winter2023\\CSCI6405\\project\\processed_dataset\\"
                  "Gross domestic product, expenditure-based, ("+file_name+"_1991_2022).csv")
df4.set_index(df4.columns[0], inplace=True)
prefix = '4_Canada_gdp_yearly_'
new_index = {old_index: prefix + old_index for old_index in df4.index}
df4.rename(index=new_index, inplace=True)

# federal only
if province == "Canada":
    df5 = pd.read_csv("D:\\winter2023\\CSCI6405\\project\\processed_dataset\\"
                      "Household spending(2010_2019).csv")
    df5.set_index(df5.columns[0], inplace=True)
    prefix = '5_Household spending_'
    new_index = {old_index: prefix + old_index for old_index in df5.index}
    df5.rename(index=new_index, inplace=True)

df6 = pd.read_csv("D:\\winter2023\\CSCI6405\\project\\processed_dataset\\"
                  "Estimates of population (EachProvince_2001_2021).csv")
df6.set_index(df6.columns[0], inplace=True)
prefix = '6_Estimates of population_'
new_index = {old_index: prefix + old_index for old_index in df6.index}
df6.rename(index=new_index, inplace=True)

df7 = pd.read_csv("D:\\winter2023\\CSCI6405\\project\\processed_dataset\\"
                  "Dependency ratio (EachProvince_2001_2021).csv")
df7.set_index(df7.columns[0], inplace=True)
prefix = '7_Dependency ratio_'
new_index = {old_index: prefix + old_index for old_index in df7.index}
df7.rename(index=new_index, inplace=True)

# federal only
if province == "Canada":
    df8 = pd.read_csv("D:\\winter2023\\CSCI6405\\project\\processed_dataset\\"
                      "Canadian government finance statistics for the federal government(stock_2008_2021).csv")
    df8.set_index(df8.columns[0], inplace=True)
    prefix = '8_Canadian government finance statistics for the federal government_'
    new_index = {old_index: prefix + old_index for old_index in df8.index}
    df8.rename(index=new_index, inplace=True)


# fill missing data with nan
df1 = df1.replace('..', np.nan)
df2 = df2.replace('..', np.nan)
df3 = df3.replace('..', np.nan)
df4 = df4.replace('..', np.nan)
# federal only
if province == "Canada":
    df5 = df5.replace('..', np.nan)
df6 = df6.replace('..', np.nan)
df7 = df7.replace('..', np.nan)
# federal only
if province == "Canada":
    df8 = df8.replace('..', np.nan)
df9 = df9.replace('..', np.nan)

# select certain rows from df3, df6, df7, and df9
if is_terrotory == False:
    df3_selected = df3.loc[df3.index.str.contains(province, regex=False)]

    df6_selected = df6.loc[df6.index.str.contains(province, regex=False)]
    df7_selected = df7.loc[df7.index.str.contains(province, regex=False)]
    df9_selected = df9.loc[df9.index.str.contains(province, regex=False)]
else:
    df3_selected = df3[df3.index.str.contains(f"{province}|Territories", regex=True)]
    df6_selected = df6[df6.index.str.contains(f"{province}|Territories", regex=True)]
    df7_selected = df7[df7.index.str.contains(f"{province}|Territories", regex=True)]
    df9_selected = df9[df9.index.str.contains(f"{province}|Territories", regex=True)]
# for federal
if province == "Canada":
    df_concat = pd.concat([df1, df2, df3_selected, df4, df6_selected, df7_selected, df9_selected, df5, df8], axis=0)
# for province
else:
    df_concat = pd.concat([df1, df2, df3_selected, df4, df6_selected, df7_selected, df9_selected], axis=0)

df_concat.to_csv("D:\\winter2023\CSCI6405\\project\\processed_dataset_new\\"
                 +province+"_dataset.csv", index=True)
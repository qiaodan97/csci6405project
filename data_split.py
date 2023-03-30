import pandas as pd
import numpy as np

canada_set = pd.read_csv("D:\\winter2023\\CSCI6405\\project\\final_dataset\\"
                  "Canada_transformed.csv")

provincial_set = pd.read_csv("D:\\winter2023\\CSCI6405\\project\\final_dataset\\"
                  "all_provinces_transformed_renamed.csv")
# df_concat.to_csv("D:\\winter2023\CSCI6405\\project\\processed_dataset_new\\"
#                  +province+"_dataset.csv", index=True)
# canada, overall
canada_overall = [
    "Area_Year",
    "9_Postsecondary enrolments_Canada",
    "2_Number of students in elementary and secondary schools_Total, school type Total, program type",
    "3_Number of full-time and part-time educators_Canada",
    "1_Live births_Total, Canada and place of residence of mother outside Canada 10 11",
    "6_Estimates of population_Canada",
    "7_Dependency ratio_Canada",
    "5_Household spending_Total expenditure",
    "4_Canada_gdp_yearly_Final consumption expenditure",
    "4_Canada_gdp_yearly_Gross fixed capital formation",
    "4_Canada_gdp_yearly_Investment in inventories",
    "4_Canada_gdp_yearly_Exports of goods and services",
    "4_Canada_gdp_yearly_Less: imports of goods and services",
    "4_Canada_gdp_yearly_Statistical discrepancy",
    "4_Canada_gdp_yearly_Gross domestic product at market prices",
    "4_Canada_gdp_yearly_Final domestic demand",
    "8_Canadian government finance statistics for the federal government_Gross operating balance 5 6",
    "8_Canadian government finance statistics for the federal government_Net operating balance 7",
    "8_Canadian government finance statistics for the federal government_Net worth 3 10 11",
]

# provincial, overall
provincial_overall = [
    "Area_Year",
"9_Postsecondary enrolments",
"2_Number of students in elementary and secondary schools_Total, school type Total, program type",
"3_Number of full-time and part-time educators",
"1_Live births_Total, Canada and place of residence of mother outside Canada 10 11",
"6_Estimates of population",
"7_Dependency ratio",
"4_Canada_gdp_yearly_Final consumption expenditure",
"4_Canada_gdp_yearly_Gross fixed capital formation",
"4_Canada_gdp_yearly_Investment in inventories",
"4_Canada_gdp_yearly_Exports of goods and services",
"4_Canada_gdp_yearly_Less: imports of goods and services",
"4_Canada_gdp_yearly_Statistical discrepancy",
"4_Canada_gdp_yearly_Gross domestic product at market prices",
"4_Canada_gdp_yearly_Final domestic demand",
]

# KeyError:
# '8_Canadian government finance statistics for the federal government_Compensation of employees',
# '8_Canadian government finance statistics for the federal government_Use of goods and services',
# '8_Canadian government finance statistics for the federal government_Nonfinancial assets'] not in index"

# canada, details
canada_details = [
    "Area_Year",
"9_Postsecondary enrolments_Canada",
"2_Number of students in elementary and secondary schools_Public school Total, program type",
"2_Number of students in elementary and secondary schools_Priviate school Total, program type",
"2_Number of students in elementary and secondary schools_Home-schooling Total, program type",
"3_Number of full-time and part-time educators_Canada",
"1_Live births_Canada, place of residence of mother 10",
"1_Live births_Place of residence of mother outside Canada 11",
"6_Estimates of population_Canada",
"7_Dependency ratio_Canada",
"5_Household spending_Food purchased from stores",
"5_Household spending_Food purchased from restaurants",
"5_Household spending_Rented living quarters",
"5_Household spending_Owned living quarters",
"5_Household spending_Water, fuel and electricity for principal accommodation",
"5_Household spending_Other accommodation",
"5_Household spending_Communications",
"5_Household spending_Household furnishings",
"5_Household spending_Household appliances",
"5_Household spending_Clothing and accessories",
"5_Household spending_Private transportation",
"5_Household spending_Public transportation",
"5_Household spending_Direct health care costs to household",
"5_Household spending_Personal care",
"5_Household spending_Recreational equipment and related services",
"5_Household spending_Home entertainment equipment and services",
"5_Household spending_Recreational services",
"5_Household spending_Recreational vehicles and associated services",
"5_Household spending_Education",
"5_Household spending_Reading materials and other printed matter",
"5_Household spending_Tobacco products, alcoholic beverages and cannabis for non-medical use",
"5_Household spending_Tobacco products and alcoholic beverages (Terminated)",
"5_Household spending_Games of chance",
"5_Household spending_Miscellaneous expenditures",
"5_Household spending_Income taxes 8",
"5_Household spending_Personal insurance payments and pension contributions",
"5_Household spending_Gifts of money, support payments and charitable contributions",
"4_Canada_gdp_yearly_Durable goods",
"4_Canada_gdp_yearly_Semi-durable goods",
"4_Canada_gdp_yearly_Non-durable goods",
"4_Canada_gdp_yearly_Services",
"4_Canada_gdp_yearly_Non-profit institutions serving households final consumption expenditure",
"4_Canada_gdp_yearly_General governments final consumption expenditure",
"4_Canada_gdp_yearly_Non-residential structures",
"4_Canada_gdp_yearly_Machinery and equipment",
"4_Canada_gdp_yearly_Intellectual property products",
"4_Canada_gdp_yearly_Residential structures",
"4_Canada_gdp_yearly_Non-profit institutions serving households gross fixed capital formation",
"4_Canada_gdp_yearly_General governments gross fixed capital formation",
"4_Canada_gdp_yearly_Non-farm",
"4_Canada_gdp_yearly_Farm",
"4_Canada_gdp_yearly_Exports of goods",
"4_Canada_gdp_yearly_Exports of services",
"4_Canada_gdp_yearly_Imports of goods",
"4_Canada_gdp_yearly_Imports of services",
"4_Canada_gdp_yearly_Statistical discrepancy",
"4_Canada_gdp_yearly_Gross domestic product at market prices",
"4_Canada_gdp_yearly_Final domestic demand",
"8_Canadian government finance statistics for the federal government_Gross operating balance 5 6",
"8_Canadian government finance statistics for the federal government_Taxes on income, profits and capital gains",
"8_Canadian government finance statistics for the federal government_Taxes on property",
"8_Canadian government finance statistics for the federal government_Taxes on goods and services",
"8_Canadian government finance statistics for the federal government_Taxes on international trade and transactions",
"8_Canadian government finance statistics for the federal government_Other taxes",
"8_Canadian government finance statistics for the federal government_Social contributions",
"8_Canadian government finance statistics for the federal government_Grants, revenue",
"8_Canadian government finance statistics for the federal government_Property income",
"8_Canadian government finance statistics for the federal government_Sales of goods and services",
"8_Canadian government finance statistics for the federal government_Fines, penalties and forfeits",
"8_Canadian government finance statistics for the federal government_Voluntary transfers other than grants",
"8_Canadian government finance statistics for the federal government_Miscellaneous revenue 8",
"8_Canadian government finance statistics for the federal government_Compensation of employees 9",
"8_Canadian government finance statistics for the federal government_Use of goods and services 9",
"8_Canadian government finance statistics for the federal government_Interest expense",
"8_Canadian government finance statistics for the federal government_Subsidies",
"8_Canadian government finance statistics for the federal government_Grants, expense",
"8_Canadian government finance statistics for the federal government_Social benefits",
"8_Canadian government finance statistics for the federal government_Other expense",
"8_Canadian government finance statistics for the federal government_Nonfinancial assets 12",
"8_Canadian government finance statistics for the federal government_Currency and deposits, assets",
"8_Canadian government finance statistics for the federal government_Debt securities, assets",
"8_Canadian government finance statistics for the federal government_Loans, assets",
"8_Canadian government finance statistics for the federal government_Equity and investment fund shares, assets",
"8_Canadian government finance statistics for the federal government_Insurance and pension, assets",
"8_Canadian government finance statistics for the federal government_Other accounts receivable",
"8_Canadian government finance statistics for the federal government_Currency and deposits, liabilities",
"8_Canadian government finance statistics for the federal government_Debt securities, liabilities",
"8_Canadian government finance statistics for the federal government_Loans, liabilities",
"8_Canadian government finance statistics for the federal government_Insurance, pension and standardized guarantee schemes, liabilities",
"8_Canadian government finance statistics for the federal government_Other accounts payable",
"8_Canadian government finance statistics for the federal government_Monetary gold and special drawing rights (SDR), liabilities",
]

# provincial, details
provincial_details = [
    "Area_Year",
"9_Postsecondary enrolments",
"2_Number of students in elementary and secondary schools_Public school Total, program type",
"2_Number of students in elementary and secondary schools_Priviate school Total, program type",
"2_Number of students in elementary and secondary schools_Home-schooling Total, program type",
"3_Number of full-time and part-time educators",
"1_Live births_Canada, place of residence of mother 10",
"1_Live births_Place of residence of mother outside Canada 11",
"6_Estimates of population",
"7_Dependency ratio",
"4_Canada_gdp_yearly_Durable goods",
"4_Canada_gdp_yearly_Semi-durable goods",
"4_Canada_gdp_yearly_Non-durable goods",
"4_Canada_gdp_yearly_Services",
"4_Canada_gdp_yearly_Non-profit institutions serving households final consumption expenditure",
"4_Canada_gdp_yearly_General governments final consumption expenditure",
"4_Canada_gdp_yearly_Non-residential structures",
"4_Canada_gdp_yearly_Machinery and equipment",
"4_Canada_gdp_yearly_Intellectual property products",
"4_Canada_gdp_yearly_Residential structures",
"4_Canada_gdp_yearly_Non-profit institutions serving households gross fixed capital formation",
"4_Canada_gdp_yearly_General governments gross fixed capital formation",
"4_Canada_gdp_yearly_Non-farm",
"4_Canada_gdp_yearly_Farm",
"4_Canada_gdp_yearly_Exports of goods to other countries",
"4_Canada_gdp_yearly_Exports of services to other countries",
"4_Canada_gdp_yearly_Exports of goods to other provinces",
"4_Canada_gdp_yearly_Exports of services to other provinces",
"4_Canada_gdp_yearly_Imports of goods from other countries",
"4_Canada_gdp_yearly_Imports of services from other countries",
"4_Canada_gdp_yearly_Imports of goods from other provinces",
"4_Canada_gdp_yearly_Imports of services from other provinces",
"4_Canada_gdp_yearly_Statistical discrepancy",
"4_Canada_gdp_yearly_Gross domestic product at market prices",
"4_Canada_gdp_yearly_Final domestic demand",
]

canada_set_overall = canada_set.loc[:, canada_overall]
canada_set_detailed = canada_set.loc[:, canada_details]
provincial_set_overall = provincial_set.loc[:, provincial_overall]
provincial_set_detailed = provincial_set.loc[:, provincial_details]
canada_set_overall = canada_set_overall.replace(',', '', regex=True)
canada_set_detailed = canada_set_detailed.replace(',', '', regex=True)
provincial_set_overall = provincial_set_overall.replace(',', '', regex=True)
provincial_set_detailed = provincial_set_detailed.replace(',', '', regex=True)

canada_set_overall.to_csv("D:\\winter2023\CSCI6405\\project\\final_dataset\\canada_set_overall.csv", index=False)
canada_set_detailed.to_csv("D:\\winter2023\CSCI6405\\project\\final_dataset\\canada_set_detailed.csv", index=False)
provincial_set_overall.to_csv("D:\\winter2023\CSCI6405\\project\\final_dataset\\provincial_set_overall.csv", index=False)
provincial_set_detailed.to_csv("D:\\winter2023\CSCI6405\\project\\final_dataset\\provincial_set_detailed.csv", index=False)

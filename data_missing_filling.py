import pandas as pd
import numpy as np
import numpy as np
from sklearn.impute import KNNImputer

imputer = KNNImputer()
canada_set_overall = pd.read_csv("D:\\winter2023\\CSCI6405\\project\\final_dataset\\"
                  "canada_set_overall.csv")
canada_set_overall.set_index('Area_Year', inplace=True)
canada_set_overall_imputer = imputer.fit_transform(canada_set_overall)
canada_set_overall.fillna(-1, inplace=True)


imputer = KNNImputer()
canada_set_detailed = pd.read_csv("D:\\winter2023\\CSCI6405\\project\\final_dataset\\"
                  "canada_set_detailed.csv")
canada_set_detailed.set_index('Area_Year', inplace=True)
canada_set_detailed_imputer = imputer.fit_transform(canada_set_detailed)
canada_set_detailed.fillna(-1, inplace=True)


imputer = KNNImputer()
provincial_set_overall = pd.read_csv("D:\\winter2023\\CSCI6405\\project\\final_dataset\\"
                  "provincial_set_overall.csv")
provincial_set_overall.set_index('Area_Year', inplace=True)
provincial_set_overall_imputer = imputer.fit_transform(provincial_set_overall)
provincial_set_overall.fillna(-1, inplace=True)

imputer = KNNImputer()
provincial_set_detailed = pd.read_csv("D:\\winter2023\\CSCI6405\\project\\final_dataset\\"
                  "provincial_set_detailed.csv")
provincial_set_detailed.set_index('Area_Year', inplace=True)
provincial_set_detailed_imputer = imputer.fit_transform(provincial_set_detailed)
provincial_set_detailed.fillna(-1, inplace=True)

pd.DataFrame(canada_set_overall_imputer).to_csv("D:\\winter2023\CSCI6405\\project\\final_dataset\\canada_set_overall_imputer.csv", index=True)
canada_set_overall.to_csv("D:\\winter2023\CSCI6405\\project\\final_dataset\\canada_set_overall_nega.csv", index=True)
pd.DataFrame(canada_set_detailed_imputer).to_csv("D:\\winter2023\CSCI6405\\project\\final_dataset\\canada_set_detailed_imputer.csv", index=True)
canada_set_detailed.to_csv("D:\\winter2023\CSCI6405\\project\\final_dataset\\canada_set_detailed_nega.csv", index=True)
pd.DataFrame(provincial_set_overall_imputer).to_csv("D:\\winter2023\CSCI6405\\project\\final_dataset\\provincial_set_overall_imputer.csv", index=True)
provincial_set_overall.to_csv("D:\\winter2023\CSCI6405\\project\\final_dataset\\provincial_set_overall_nega.csv", index=True)
pd.DataFrame(provincial_set_detailed_imputer).to_csv("D:\\winter2023\CSCI6405\\project\\final_dataset\\provincial_set_detailed_imputer.csv", index=True)
provincial_set_detailed.to_csv("D:\\winter2023\CSCI6405\\project\\final_dataset\\provincial_set_detailed_nega.csv", index=True)
import glob

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error
import numpy as np
import pandas as pd

file_pattern2 = "D:\\winter2023\\CSCI6405\\project\\finalfinal_dataset\\*detailed*.csv"
file_pattern3 = "D:\\winter2023\\CSCI6405\\project\\finalfinal_dataset\\*overall*.csv"

file_paths2 = glob.glob(file_pattern2)
file_paths3 = glob.glob(file_pattern3)
#
# year = "2010"
# target = "economics"
#
# mse_dict = {}
# for file_paths in [file_paths2]:
#     for file_path in file_paths:
#             df = pd.read_csv(file_path)
#
#
#             df["province"] = df['Area_Year'].str.split("_", n=1, expand=True)[0]
#             df["year"] = df['Area_Year'].str.split("_", n=1, expand=True)[1]
#             df.set_index(['Area_Year'],drop=True)
#         # print(df.columns)
#         # print(df["province"])
#         # print(df["year"])
#
#
#             file_name = file_path.split("\\")[-1].split(".")[0]
#             test_data1 = df.loc[df['year'] == year]
#             train_data1 = df.loc[df['year'] != year]
#
#             # test_data1 = df.loc[df['province'] == province].loc[df['year'] == "2010"]
#             # train_data1 = df.loc[df['province'] == province].loc[df['year'] == "2010"]
#
#             test_data1 = test_data1.drop(["province", "year"], axis=1)
#             train_data1 = train_data1.drop(["province", "year"], axis=1)
#             # test_data1 = test_data1.drop(["province", "year"], axis=1)
#             # train_data1 = train_data1.drop(["province", "year"], axis=1)
#             # print(train_data1.shape)
#             province = df['province'][0]
#             if province != "Canada":
#                 # for index in [1, 2, 3]: # 0 is the index
#                 if target == "economics":
#                     X_train_1 = train_data1.iloc[:, 1:6]
#                     Y_train_1 = train_data1.iloc[:, 6:]
#                     X_test_1 = test_data1.iloc[:, 1:6]
#                     Y_test_1 = test_data1.iloc[:, 6:]
#                 else:
#                     Y_train_1 = train_data1.iloc[:, 1:6]
#                     X_train_1 = train_data1.iloc[:, 6:]
#                     Y_test_1 = test_data1.iloc[:, 1:6]
#                     X_test_1 = test_data1.iloc[:, 6:]
#                 # column_name = test_data1.columns[index]
#                 # Polynomial Regression
#                 poly = PolynomialFeatures(degree=3)
#                 X_train_poly = poly.fit_transform(X_train_1)
#                 X_test_poly = poly.fit_transform(X_test_1)
#                 model_poly = LinearRegression()
#                 model_poly.fit(X_train_poly, Y_train_1)
#                 y_pred_poly = model_poly.predict(X_test_poly)
#                 mse_poly = mean_squared_error(Y_test_1, y_pred_poly)
#
#                 # Save MSE to dictionary
#                 mse_dict[f"{file_name}: {province}_{target}"] = mse_poly
#
#                 print(f"{file_name}: {province}_{target} MSE = {mse_poly:.2f}")
#
# # Convert dictionary to dataframe and save to CSV
# mse_df = pd.DataFrame.from_dict(mse_dict, orient='index', columns=['MSE'])
# mse_df.index.name = 'Index'
# mse_df.to_csv('D:\\winter2023\\CSCI6405\\project\\linear_regression_each_province\\all_province_detailed_'+target+'_'+year+'.csv')


year = "2021"
target = "economics"

mse_dict = {}
for file_paths in [file_paths3]:
    for file_path in file_paths:
            df = pd.read_csv(file_path)


            df["province"] = df['Area_Year'].str.split("_", n=1, expand=True)[0]
            df["year"] = df['Area_Year'].str.split("_", n=1, expand=True)[1]
            df.set_index(['Area_Year'],drop=True)
        # print(df.columns)
        # print(df["province"])
        # print(df["year"])


            file_name = file_path.split("\\")[-1].split(".")[0]
            test_data1 = df.loc[df['year'] == year]
            train_data1 = df.loc[df['year'] != year]

            # test_data1 = df.loc[df['province'] == province].loc[df['year'] == "2010"]
            # train_data1 = df.loc[df['province'] == province].loc[df['year'] == "2010"]

            test_data1 = test_data1.drop(["province", "year"], axis=1)
            train_data1 = train_data1.drop(["province", "year"], axis=1)
            # test_data1 = test_data1.drop(["province", "year"], axis=1)
            # train_data1 = train_data1.drop(["province", "year"], axis=1)
            # print(train_data1.shape)
            province = df['province'][0]
            if province != "Canada":
                # for index in [1, 2, 3]: # 0 is the index
                if target == "economics":
                    X_train_1 = train_data1.iloc[:, 1:4]
                    Y_train_1 = train_data1.iloc[:, 4:]
                    X_test_1 = test_data1.iloc[:, 1:4]
                    Y_test_1 = test_data1.iloc[:, 4:]
                else:
                    Y_train_1 = train_data1.iloc[:, 1:4]
                    X_train_1 = train_data1.iloc[:, 4:]
                    Y_test_1 = test_data1.iloc[:, 1:4]
                    X_test_1 = test_data1.iloc[:, 4:]
                # column_name = test_data1.columns[index]
                # Polynomial Regression
                poly = PolynomialFeatures(degree=3)
                X_train_poly = poly.fit_transform(X_train_1)
                X_test_poly = poly.fit_transform(X_test_1)
                model_poly = LinearRegression()
                model_poly.fit(X_train_poly, Y_train_1)
                y_pred_poly = model_poly.predict(X_test_poly)
                mse_poly = mean_squared_error(Y_test_1, y_pred_poly)

                # Save MSE to dictionary
                mse_dict[f"{file_name}: {province}_{target}"] = mse_poly

                print(f"{file_name}: {province}_{target} MSE = {mse_poly:.2f}")

# Convert dictionary to dataframe and save to CSV
mse_df = pd.DataFrame.from_dict(mse_dict, orient='index', columns=['MSE'])
mse_df.index.name = 'Index'
mse_df.to_csv('D:\\winter2023\\CSCI6405\\project\\linear_regression_each_province\\all_province_overall_'+target+'_'+year+'.csv')
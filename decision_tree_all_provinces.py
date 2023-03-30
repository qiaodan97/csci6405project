import glob

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

file_pattern2 = "D:\\winter2023\\CSCI6405\\project\\finalfinal_dataset\\*detailed*.csv"
file_pattern3 = "D:\\winter2023\\CSCI6405\\project\\finalfinal_dataset\\*overall*.csv"

file_paths2 = glob.glob(file_pattern2)
file_paths3 = glob.glob(file_pattern3)

target = "year"
features = "education"

accuracy_dict = {}

for file_paths in [file_paths3]:
    for file_path in file_paths:
            df = pd.read_csv(file_path)

            df["province"] = df['Area_Year'].str.split("_", n=1, expand=True)[0]
            df["year"] = df['Area_Year'].str.split("_", n=1, expand=True)[1]
            df.set_index(['Area_Year'],drop=True)
            if features == 'economics':
                df = df.iloc[:, 1:4].join(df.iloc[:, -2:])

            elif features == 'education':
                df = df.iloc[:, 4:]

            train_data, test_data = train_test_split(df, test_size=0.3, random_state=42)

            province = df['province'][0]
            if province != "Canada":
                file_name = file_path.split("\\")[-1].split(".")[0]

                test_data1 = test_data.drop(["province", "year"], axis=1)
                train_data1 = train_data.drop(["province", "year"], axis=1)

                if target == "year":
                    X_train_1 = train_data.drop(["province", "year"], axis=1).iloc[:, 1:]
                    Y_train_1 = train_data["year"]
                    X_test_1 = test_data.drop(["province", "year"], axis=1).iloc[:, 1:]
                    Y_test_1 = test_data["year"]
                else:
                    X_train_1 = train_data.drop(["province", "year"], axis=1).iloc[:, 1:]
                    Y_train_1 = train_data["province"]
                    X_test_1 = test_data.drop(["province", "year"], axis=1).iloc[:, 1:]
                    Y_test_1 = test_data["province"]

                # Decision Tree Classifier
                model_dt = DecisionTreeClassifier()
                model_dt.fit(X_train_1, Y_train_1)
                y_pred_dt = model_dt.predict(X_test_1)
                accuracy_dt = accuracy_score(Y_test_1, y_pred_dt)

                # Save accuracy to dictionary
                accuracy_dict[f"{file_name}: {target}"] = accuracy_dt

                print(f"{file_name}: {target} Accuracy = {accuracy_dt:.2f}")

# Convert dictionary to dataframe and save to CSV
accuracy_df = pd.DataFrame.from_dict(accuracy_dict, orient='index', columns=['Accuracy'])
accuracy_df.index.name = 'Index'
accuracy_df.to_csv('D:\\winter2023\\CSCI6405\\project\\decision_tree\\all_province_overall_'+features+'_'+target+'_accuracy.csv')




accuracy_dict = {}

for file_paths in [file_paths2]:
    for file_path in file_paths:
            df = pd.read_csv(file_path)

            df["province"] = df['Area_Year'].str.split("_", n=1, expand=True)[0]
            df["year"] = df['Area_Year'].str.split("_", n=1, expand=True)[1]
            df.set_index(['Area_Year'],drop=True)

            if features == 'economics':
                df = df.iloc[:, 1:6].join(df.iloc[:, -2:])

            elif features == 'education':
                df = df.iloc[:, 6:]

            train_data, test_data = train_test_split(df, test_size=0.3, random_state=42)

            province = df['province'][0]
            if province != "Canada":
                file_name = file_path.split("\\")[-1].split(".")[0]

                test_data1 = test_data.drop(["province", "year"], axis=1)
                train_data1 = train_data.drop(["province", "year"], axis=1)

                if target == "year":
                    X_train_1 = train_data.drop(["province", "year"], axis=1).iloc[:, 1:]
                    Y_train_1 = train_data["year"]
                    X_test_1 = test_data.drop(["province", "year"], axis=1).iloc[:, 1:]
                    Y_test_1 = test_data["year"]
                else:
                    X_train_1 = train_data.drop(["province", "year"], axis=1).iloc[:, 1:]
                    Y_train_1 = train_data["province"]
                    X_test_1 = test_data.drop(["province", "year"], axis=1).iloc[:, 1:]
                    Y_test_1 = test_data["province"]

                # Decision Tree Classifier
                model_dt = DecisionTreeClassifier()
                model_dt.fit(X_train_1, Y_train_1)
                y_pred_dt = model_dt.predict(X_test_1)
                accuracy_dt = accuracy_score(Y_test_1, y_pred_dt)

                # Save accuracy to dictionary
                accuracy_dict[f"{file_name}: {target}"] = accuracy_dt

                print(f"{file_name}: {target} Accuracy = {accuracy_dt:.2f}")

# Convert dictionary to dataframe and save to CSV
accuracy_df = pd.DataFrame.from_dict(accuracy_dict, orient='index', columns=['Accuracy'])
accuracy_df.index.name = 'Index'
accuracy_df.to_csv('D:\\winter2023\\CSCI6405\\project\\decision_tree\\all_province_detailed_'+features+'_'+target+'_accuracy.csv')

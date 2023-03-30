from sklearn.preprocessing import MinMaxScaler, StandardScaler
import pandas as pd

file_paths = [
    "D:\\winter2023\\CSCI6405\\project\\final_dataset\\canada_set_overall_imputer.csv",
    "D:\\winter2023\\CSCI6405\\project\\final_dataset\\canada_set_overall_nega.csv",
    "D:\\winter2023\\CSCI6405\\project\\final_dataset\\canada_set_detailed_imputer.csv",
    "D:\\winter2023\\CSCI6405\\project\\final_dataset\\canada_set_detailed_nega.csv",
    "D:\\winter2023\\CSCI6405\\project\\final_dataset\\provincial_set_overall_imputer.csv",
    "D:\\winter2023\\CSCI6405\\project\\final_dataset\\provincial_set_overall_nega.csv",
    "D:\\winter2023\\CSCI6405\\project\\final_dataset\\provincial_set_detailed_imputer.csv",
    "D:\\winter2023\\CSCI6405\\project\\final_dataset\\provincial_set_detailed_nega.csv"
]

for file_path in file_paths:
    data = pd.read_csv(file_path, index_col=0)
    non_norm_file_path = file_path.split(".csv")[0] + "_nonorm.csv"
    data.to_csv(non_norm_file_path, index=True)

    minmax_scaler = MinMaxScaler()
    minmax_data = pd.DataFrame(minmax_scaler.fit_transform(data), columns=data.columns, index=data.index)

    minmax_file_path = file_path.split(".csv")[0] + "_minmax.csv"
    minmax_data.to_csv(minmax_file_path, index=True)

    std_scaler = StandardScaler()
    std_data = pd.DataFrame(std_scaler.fit_transform(data), columns=data.columns, index=data.index)

    std_file_path = file_path.split(".csv")[0] + "_std.csv"
    std_data.to_csv(std_file_path, index=True)

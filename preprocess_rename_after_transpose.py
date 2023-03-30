import os
import pandas as pd

folder_path = "D:\\winter2023\\CSCI6405\\project\\processed_dataset_new\\"
df_list = []

for file_name in os.listdir(folder_path):
    if file_name.endswith("_transformed.csv") :
        df = pd.read_csv(os.path.join(folder_path, file_name), index_col=0)

        # "_transformed.csv"
        prefix = file_name[:-16]
        new_columns = {}
        for column in df.columns:
            new_columns[column] = column.rsplit("_", 1)[0]
        df.rename(columns=new_columns, inplace=True)

        df.to_csv(os.path.join(folder_path, prefix + "_transformed_renamed.csv"), index=True)

import os
import pandas as pd

folder_path = "D:\\winter2023\\CSCI6405\\project\\processed_dataset_new\\"
df_list = []

for file_name in os.listdir(folder_path):
    if file_name.endswith("_transformed_renamed.csv") and file_name != "Canada_transformed_renamed.csv":
        df = pd.read_csv(os.path.join(folder_path, file_name))
        df_list.append(df)

merged_df = pd.concat(df_list, axis=0)
merged_df.to_csv(os.path.join(folder_path, "all_datasets_transformed.csv"), index=False)

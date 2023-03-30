import os
import pandas as pd

folder_path = "D:\\winter2023\\CSCI6405\\project\\processed_dataset_new\\"

for file_name in os.listdir(folder_path):
    if file_name.endswith("_dataset.csv"):
        df = pd.read_csv(os.path.join(folder_path, file_name))
        df.set_index(df.columns[0], inplace=True)

        # "_dataset.csv"
        prefix = file_name[:-12]

        df.columns = [prefix + "_" + str(col) for col in df.columns]

        df = df.transpose()
        df.reset_index(inplace=True)

        df.rename(columns={'index': 'Area_Year'}, inplace=True)

        df.to_csv(os.path.join(folder_path, prefix + "_transformed.csv"), index=False)

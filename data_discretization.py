from sklearn.preprocessing import KBinsDiscretizer
import pandas as pd
import glob

n_bins = 10
encode = 'ordinal'
strategy = 'kmeans'

file_pattern1 = "D:\\winter2023\\CSCI6405\\project\\final_dataset\\*_nonorm.csv"
file_pattern2 = "D:\\winter2023\\CSCI6405\\project\\final_dataset\\*_minmax.csv"
file_pattern3 = "D:\\winter2023\\CSCI6405\\project\\final_dataset\\*_std.csv"

file_paths1 = glob.glob(file_pattern1)
file_paths2 = glob.glob(file_pattern2)
file_paths3 = glob.glob(file_pattern3)

for file_paths in [file_paths1, file_paths2, file_paths3]:
    for file_path in file_paths:
        data = pd.read_csv(file_path, index_col=0)
        nondiscretized_file_path = file_path.split(".csv")[0] + "_nondiscretized.csv"
        data.to_csv(nondiscretized_file_path, index=True)
        kbd = KBinsDiscretizer(n_bins=n_bins, encode=encode, strategy=strategy)
        data.iloc[:, :] = kbd.fit_transform(data.iloc[:, :])
        discretized_file_path = file_path.split(".csv")[0] + "_discretized.csv"
        data.to_csv(discretized_file_path, index=True)

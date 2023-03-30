import pandas as pd
import numpy as np
import glob

file_pattern1 = "D:\\winter2023\\CSCI6405\\project\\finalfinal_dataset\\*_discretized.csv"
file_pattern2 = "D:\\winter2023\\CSCI6405\\project\\finalfinal_dataset\\*_nondiscretized.csv"

output_folder = "D:\\winter2023\\CSCI6405\\project\\dataset_statistics\\"

for file_pattern in [file_pattern1, file_pattern2]:
    file_paths = glob.glob(file_pattern)

    for file_path in file_paths:
        data = pd.read_csv(file_path, index_col=0)

        upper_bound = data.max()
        lower_bound = data.min()
        std_dev = data.std()
        mean = data.mean()
        cov_matrix = np.cov(data.values.T, ddof=0)
        corr_matrix = np.corrcoef(data.values.T)

        cov_matrix[np.isnan(cov_matrix)] = 0
        corr_matrix[np.isnan(corr_matrix)] = 0

        results_df = pd.DataFrame({'Upper Bounds': upper_bound,
                                   'Lower Bounds': lower_bound,
                                   'Standard Deviation': std_dev,
                                   'Mean': mean})

        results_df.to_csv(output_folder + file_path.split('\\')[-1].split('.')[0] + '_stats.csv')
        np.savetxt(output_folder + file_path.split('\\')[-1].split('.')[0] + '_covariance.csv', cov_matrix,
                   delimiter=',')
        np.savetxt(output_folder + file_path.split('\\')[-1].split('.')[0] + '_correlation.csv', corr_matrix,
                   delimiter=',')

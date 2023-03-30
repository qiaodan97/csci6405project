# import pandas as pd
# import glob
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.decomposition import PCA
# from matplotlib.colors import ListedColormap

import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from matplotlib.colors import ListedColormap

from matplotlib.ticker import Formatter

class ProvinceFormatter(Formatter):
    def __init__(self, province_codes, province_names):
        self.province_codes = province_codes
        self.province_names = province_names

    def __call__(self, x, pos=None):
        code = int(x)
        if code in self.province_codes:
            return self.province_names[code]
        else:
            return ""

file_pattern2 = "D:\\winter2023\\CSCI6405\\project\\finalfinal_dataset\\*minmax*.csv"
file_pattern3 = "D:\\winter2023\\CSCI6405\\project\\finalfinal_dataset\\*std*.csv"

file_paths2 = glob.glob(file_pattern2)
file_paths3 = glob.glob(file_pattern3)

for file_paths in [file_paths2, file_paths3]:
    for file_path in file_paths:
        data = pd.read_csv(file_path, index_col=0)
        file_name = file_path.split("\\")[-1].split(".")[0]
        province = pd.Series([index.split("_")[0] for index in data.index])
        year = pd.Series([index.split("_")[1] for index in data.index]).astype(int)

        pca = PCA(n_components=2)
        components = pca.fit_transform(data)

        # create a scatter plot of PCA components, colored by year
        cmap = ListedColormap(plt.cm.viridis(np.linspace(0, 1, len(year.unique()))))
        year_labels = [f"{y} ({c})" for y, c in zip(year.unique(), cmap.colors)]
        print(year_labels)
        fig, ax = plt.subplots()
        sc = ax.scatter(components[:, 0], components[:, 1], c=year.astype(int), cmap=cmap)
        ax.set_xlabel('PC1')
        ax.set_ylabel('PC2')
        ax.set_title(f'PCA plot (colored by year)')
        fig.colorbar(sc, ax=ax, ticks=year.unique(), label="Year")
        # ax.legend(handles=sc.legend_elements()[0], labels=year_labels, loc="lower right")
        fig.savefig(f'D:\\winter2023\\CSCI6405\\project\\pca_figures\\{file_name[:-4]}_year.png')

        cmap = ListedColormap(plt.cm.viridis(np.linspace(0, 1, len(province.unique()))))
        province_codes = province.astype('category').cat.codes
        province_labels = dict(zip(province_codes.unique(), province.unique()))
        # create a scatter plot of PCA components, colored by province
        fig, ax = plt.subplots()
        sc = ax.scatter(components[:, 0], components[:, 1], c=province_codes, cmap=cmap)
        ax.set_xlabel('PC1')
        ax.set_ylabel('PC2')
        ax.set_title(f'PCA plot (colored by location)')
        formatter = ProvinceFormatter(province_codes.unique(), province_labels)
        fig.colorbar(sc, ax=ax, ticks=province_codes.unique(), label="Province", format=formatter)
        ## save the figure
        fig.savefig(f'D:\\winter2023\\CSCI6405\\project\\pca_figures\\{file_name[:-4]}_province.png')


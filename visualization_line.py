import glob
import os
import pandas as pd
import matplotlib.pyplot as plt

save_dir = 'D:\\winter2023\\CSCI6405\\project\\line_figures'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

file_pattern2 = "D:\\winter2023\\CSCI6405\\project\\finalfinal_dataset\\*minmax*.csv"
file_pattern3 = "D:\\winter2023\\CSCI6405\\project\\finalfinal_dataset\\*std*.csv"
file_pattern1 = "D:\\winter2023\\CSCI6405\\project\\finalfinal_dataset\\*nonorm*.csv"

file_paths2 = glob.glob(file_pattern2)
file_paths3 = glob.glob(file_pattern3)
file_paths1 = glob.glob(file_pattern1)
for file_paths in [file_paths1, file_paths2, file_paths3]:
    for file_path in file_paths:
        df = pd.read_csv(file_path)
        df.columns = df.columns.str.replace(": ", "_")
        # print(df.columns)
        # print(df.index.str.split('_', n=1, expand=True))
        # df['province'] = df.index.get_level_values(0)
        # df['year'] = df.index.get_level_values(1)
        df["province"] = df['Area_Year'].str.split("_", n=1, expand=True)[0]
        df["year"] = df['Area_Year'].str.split("_", n=1, expand=True)[1]
        df.set_index(['Area_Year'], drop=True)
        # print(df.columns)
        # print(df["province"])
        # print(df["year"])

        # df[["province", "year"]] = df.index.str.split("_", expand=True)
        prvovince_set = [["Prince Edward Island",
                          "Nova Scotia",
                          "New Brunswick",
                          "Newfoundland and Labrador", ],
                         ["Ontario", ],
                         ["British Columbia", ],
                         ["Alberta",
                          "Saskatchewan",
                          "Manitoba", ],
                         ["Quebec", ]]

        province = df['province'][0]
        if province != "Canada":
            file_name = file_path.split("\\")[-1].split(".")[0]
            for indicator in df.columns[1:-2]:
                fig, ax = plt.subplots()
                index = 0
                for provinces in prvovince_set:
                    selected_df = df[df['province'].isin(provinces)]
                    # print(selected_df)
                    # values = selected_df[indicator].values
                    values = selected_df.groupby('year')[indicator].sum().values
                    years = range(1991, 2022)
                    # print(str(index + 1))
                    ax.plot(years, values, label="P" + str(index + 1))
                    # print(years)
                    # print(values)
                    # ax.plot(years, values, label="C"+str(index))
                    index = index + 1
                ax.set_xlabel('Year')
                ax.set_ylabel('Value')
                ax.set_title(indicator)
                # ax.legend(bbox_to_anchor=(1.02, 1), loc='upper left')

                ax.legend(loc='upper left', bbox_to_anchor=(1.0, 1.0), ncol=1, fontsize='small')
                # fig.subplots_adjust(right=0.7)
                # ax.legend()
                fig.savefig(os.path.join(save_dir, f'{file_name[:-4]}_{indicator}.png'))
                plt.close(fig)



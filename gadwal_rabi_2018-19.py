# Importing pandas
import pandas as pd

# Importing the dataset
row_skip = [8, 16, 17, 18, 19]
df = pd.read_excel('Rabi 2018-19 Actual & Normal Areas.xlsx', skiprows=row_skip)

# Remove last column -- percentage of area sown
df.drop(df.columns[len(df.columns)-1], axis=1, inplace=True)

# Drop rows with NaNs in all columns
df = df.dropna(how='all')

# Naming the columns - to be able to access them
rows, cols = df.shape
col_list = ['Col' + str(i) for i in range(cols)]
df.columns = col_list

# New dataframe
colms = ['Year', "Season", "District name", "Mandal name", "Crop", "Normal", "Actual"]
df_all = pd.DataFrame(columns=colms)

# Getting the types of crop
crop_list = df.loc[0:0, col_list[2:]]
crop_list = crop_list.values.tolist()[0]
crop_list = [x for x in crop_list if str(x) != 'nan']

# Repeat mandal list based on number of crops
mandal_list = df['Col1'][2:].values.tolist()
mandal_num = len(mandal_list)
mandal_names = mandal_list*len(crop_list)
df_all['Mandal name'] = mandal_names

# Update Crop column depending on mandal names
crop_names = []
for each_crop in crop_list:
    crop_names += len(mandal_list) * [each_crop]
df_all['Crop'] = crop_names

# Year
df_all.Year = '2018-2019'
# Season
df_all['Season'] = "Rabi"
# District name
df_all['District name'] = "Jogulamba Gadwal"

# Normal and actual sown
for crop_num in range(len(crop_list)):
    df_all['Normal'][mandal_num*crop_num:mandal_num+mandal_num*crop_num] = df[col_list[2+crop_num*2]][2:]
    df_all['Actual'][mandal_num*crop_num:mandal_num+mandal_num*crop_num] = df[col_list[3+crop_num*2]][2:]

# Replace nan values with zeros
df_all.fillna(0)

# Rename column names
df_rename = ['year', 'season', 'district_name', 'mandal_name', 'crop', 'actual_area', 'normal_area']
df_all.columns = df_rename

# Export to csv file
df_all.to_csv('gadwal_rabi_2018-19.csv', index=False)

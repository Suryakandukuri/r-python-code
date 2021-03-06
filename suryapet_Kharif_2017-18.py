# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), '../../../../../../../../../var/folders/zq/b5ts9cfj21n_2v_vp7p8w4hr0000gn/T'))
	print(os.getcwd())
except:
	pass

#%%
# Import pandas
import pandas as pd


#%%
df = pd.read_excel("Dist Suryapet 2016 to 2018-19 Areas.xlsx", sheet_name = 'KHARIF 2017-18')


#%%
# Remove total and division rows from the dataframe
df = df[df[df.columns[1]].str.lower().str.contains('total', na=False) == False]
df = df[df[df.columns[1]].str.lower().str.contains('division', na=False) == False]


#%%
# Drop rows with NaNs in all columns
df = df.dropna(how='all')
df = df.dropna(how='all', axis=1)
# Drop rows where the values in the first three columns
# are empty
df = df.dropna(subset=[df.columns[0],df.columns[1],df.columns[2]], how = 'all')


#%%
# Naming the columns - to be able to access them
rows, cols = df.shape
col_list = ['Col' + str(i) for i in range(cols)]
df.columns = col_list


#%%
# New dataframe
colms = ['year', "season", "districtName", "mandalName", "crop", "normalAreaSown", "actualAreaSown"]
df_all = pd.DataFrame(columns=colms)


#%%
# Getting the types of crop
crop_list = df.loc[0:0, col_list[2:]]
crop_list = crop_list.values.tolist()[0]
crop_list = [x.replace('\n', ' ').strip().capitalize() for x in crop_list if str(x) != 'nan']


#%%
# Repeat mandal list based on number of crops
mandal_list = df['Col1'][2:].values.tolist()
mandal_list = [x.capitalize() for x in mandal_list]
mandal_num = len(mandal_list)
mandal_names = mandal_list*len(crop_list)
df_all['mandalName'] = mandal_names


#%%
# Update Crop column depending on mandal names
crop_names = []
for each_crop in crop_list:
    crop_names += len(mandal_list) * [each_crop]
df_all['crop'] = crop_names


#%%
# Year
df_all.year = '2017-2018'
# Season
df_all['season'] = "Kharif"
# District name
df_all['districtName'] = "Suryapet"


#%%
# Normal and actual sown
for crop_num in range(len(crop_list)):
    df_all['normalAreaSown'][mandal_num*crop_num:mandal_num+mandal_num*crop_num] = df[col_list[2+crop_num*2]][2:]
    df_all['actualAreaSown'][mandal_num*crop_num:mandal_num+mandal_num*crop_num] = df[col_list[3+crop_num*2]][2:]

# Replace nan values with zeros
#df_all.fillna(0)

# Export to csv file
df_all.to_csv('suryapet_Kharif_2017-18.csv', index=False)


#%%



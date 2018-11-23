import pandas as pd
import json
import itertools
from pandas.io.json import json_normalize


def cartesian(df1, df2):
	rows = itertools.product(df1.iterrows(), df2.iterrows())
	df = pd.DataFrame(left.append(right) for (_, left), (_, right) in rows)
	return df.reset_index(drop=True)


def main():
	# Process csv file
	df_base = pd.read_csv('navData.csv', delimiter=',', index_col=False)
	print(df_base)

	# Process json file
	with open('calibration.json') as data_file:
		data = json.load(data_file)

	df_calib = json_normalize(data, 'cameras', ['roll', 'elevation', 'azimuth'],
		record_prefix='cameras_',errors='ignore')
	df_calib = df_calib[['cameras_roll', 'cameras_elevation', 'cameras_azimuth']]
	print(df_calib)

	# Merge two dataframe create 79 * 4 rows
	df_final = cartesian(df_base, df_calib)

	# Sepcial treatment for int cols
	int_col = ['id','weekH','millisec','week']
	for col in int_col:
		df_final[col] = df_final[col].astype(int)

	df_final.to_csv('final_file.csv', index=False)


if __name__ == '__main__':
	main()
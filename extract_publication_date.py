# import argparse
import sys
from htmldate import find_date
import pandas as pd
from tqdm import tqdm

# read url csv file
input_csv = sys.argv[1]
df = pd.read_csv(input_csv) 

# list to store date values
pub_date = []

print("Collecting publication dates from URLs...")
for url in tqdm(df.iloc[:,0]):
	# for each url, find date and save to pub_date column
	try:
		# if no error, store date value
		print("Analyzing url: {}".format(url))
		date = find_date(url)
		pub_date.append(date)
	except Exception as error:
		# else store error value
		# print(type(error).__name__)
		pub_date.append(type(error).__name__)

# write output file with pub_date
print("Writing output file...")
output_fn = "output.csv"
df['publication_date'] = pub_date

df.to_csv(output_fn)
print("See output file: {}".format(output_fn))




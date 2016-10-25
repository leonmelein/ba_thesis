import csv
import sys
import pickle

def importOccupationalTitles(filename, delimit=";"):
	title_class = {}

	# Load CSV file with example occupational titles
	with open(filename, newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=delimit)
		for row in spamreader:
			print(row)
			submajor_group = int(row[0][:2])
			raw_occupational_titles = [x.strip() for x in row[2].split(',')]
			occupational_titles = []
			for title in raw_occupational_titles:
				discoupled_titles = [x.strip() for x in title.split('/')]
				occupational_titles += discoupled_titles

			print(submajor_group, "-", occupational_titles)
			title_class[submajor_group] =  title_class.get(submajor_group, []) +  occupational_titles

		# Save occupational dict to disk
		with open('occupational_dict.pickle', 'wb+') as f:
			pickle.dump(title_class, f)

if len(sys.argv) == 0:
	"You must pass a comma separated file for importing!"
else:
	importOccupations(sys.argv[1])
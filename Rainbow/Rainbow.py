from scripts.excel import *;
from scripts.scholar import *;

if __name__ == "__main__":
	REFERENCES = excel("source\Proceedings - 20190530.xlsx")
	REFERENCES.print_file()

	SCHOLAR = scholar()

	for index, value in REFERENCES.get_file_dictionary().iterrows():
		Name = ''; Initials = ''; Surname = ''
		if str(value[14]).lower() is not "nan" or value[14] is not None: Name = value[14];
		if str(value[13]).lower() is not "nan" or value[13] is not None: Initials = value[13];
		if str(value[12]).lower() is not "nan" or value[12] is not None: Surname = value[12];

		author = '\'{0} {1}. {2}\''.format(Name, Initials, Surname)
		title = '\'{0}\''.format(value[6])
		print("{0:5}: {1}- by {2}".format(index, title, author))
		
		Scholarly_Authors = []
		Scholarly_Publications = []

		Gscholar_Authors = []
		Gscholar_Publications = []

		ArXiv_Publications = []
		
		#AUTHORS
		print(next(SCHOLAR.query_scholarly(author = 'Steven A. Cholewiak')))
		"""
		try:
			Scholarly_Authors.append(SCHOLAR.query_scholarly(author = author))
			print(Scholarly_Authors)
		except Exception as e:
			print("!\t{0}\t{1}".format(author, e))

		try:
			Gscholar_Authors.append(SCHOLAR.query_gscholar(author))
		except Exception as e:
			print("!\t{0}\t{1}".format(author, e))


		#PUBLICATIONS
		try:
			Scholarly_Publications.append(SCHOLAR.query_scholarly(pub = title))
		except Exception as e:
			print("!\t{0}\t{1}".format(author, e))

		try:
			Gscholar_Publications.append(SCHOLAR.query_gscholar(title))
		except Exception as e:
			print("!\t{0}\t{1}".format(author, e))
		
		try:
			ArXiv_Publications.append(SCHOLAR.query_arxiv(title))
		except Exception as e:
			print("!\t{0}\t{1}".format(author, e))


		print(SCHOLAR.query_crossref(author = author, pub = title))

		print(SCHOLAR.query_doaj(title))
		"""



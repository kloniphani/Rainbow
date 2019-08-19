import pandas as pd

class excel(object):
	"""description of class"""
	
	_file = None
	_sheet = None
	_file_dictionary = None
	_data_frame = None

	def __init__(self, file = None, sheet = None, header=[0,1]):
		try:
			self._file = file; self._sheet = sheet;
			self._file_dictionary = pd.read_excel(file, sheet_name=sheet, header=header)
			
			print("Successfully loaded:\t{0}".format(file))
		except Exception as e:
			print(e)

	def get_file_dictionary(self):
		return pd.concat(self._file_dictionary.values(), axis = 0);
	
	def print_file(self):
		if self._file_dictionary is not None:
			print("\n{0}\n".format(self._file_dictionary))
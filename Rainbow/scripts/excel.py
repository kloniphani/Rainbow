import pandas as pd

class excel(object):
	"""description of class"""
	
	_file = None
	_sheet = None
	_dfs = None

	def __init__(self, file = None, sheet = None):
		try:
			self._file = file; self._sheet = sheet;
			self._dfs = pd.read_excel(file, sheet_name=sheet)
			
			print("Successfully loaded:\t{0}".format(file))
		except Exception as e:
			print(e)

	def print_file(self):
		if self._dfs is not None:
			print("\n{0}\n".format(self._dfs))
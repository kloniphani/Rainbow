class scholar(object):
	"""description of class"""
	
	def	query_acm_digital(self):
		pass

	def query_gscholar(self, query):
		import gscholar;
		return gscholar.query(query);

	def query_scholarly(self, author = None, keyword = None, pub = None):
		import scholarly;
		
		RESULTS = {}
		if author is not None and keyword is not None and pub is not None:
			RESULTS['author'] =	scholarly.search_author(author);
			RESULTS['keyword'] = scholarly.search_keyword(keyword);
			RESULTS['pub'] = scholarly.search_pubs_query(pub);
			return RESULTS;
		elif author is not None:
			return scholarly.search_author(author);
		elif keyword is not None:
			return scholarly.search_keyword(keyword);
		elif pub is not None:
			return scholarly.search_pubs_query(pub);
		
	def query_arxiv(self, query):
		import arxiv;
		return arxiv.query(query);

	def query_crossref(self, author = None, pub = None):
		from crossref.restful import Works
		works = Works()

		if author is not None and pub is not None:
			return works.query(title = pub, author = author)
		elif author is not None:
			return works.query(author = author)
		elif pub is not None:
			return works.query(title = pub)

	def query_dblp(self, query):
		pass

	def query_doaj(self, query):
		import requests
		headers = {'Accept': 'application/json',}
		response = requests.get('https://doaj.org/api/v1/search/articles/{0}'.format(query), headers=headers)
		return response.text;

	def query_semantic(self, authour_id = None, pub_id = None):
		import requests
		headers = {'Accept': 'application/json',}

		RESULTS = {}
		if authour_id is not None and pub_id is not None:
			response = requests.get('http://api.semanticscholar.org/v1/author/{0}'.format(authour_id), headers=headers)
			return response.text;
			RESULTS['author'] =	response.text;

			response = requests.get('http://api.semanticscholar.org/v1/paper/{0}'.format(pub_id), headers=headers)
			RESULTS['pub'] = response.text;

			return RESULTS;
		elif authour_id is not None:
			response = requests.get('http://api.semanticscholar.org/v1/author/{0}'.format(authour_id), headers=headers)
			return response.text;
		elif pub_id is not None:
			response = requests.get('http://api.semanticscholar.org/v1/paper/{0}'.format(pub_id), headers=headers)
			return response.text;

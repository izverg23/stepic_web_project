def hello(environ, start_response) :
	status = '200 OK'
	headers = [ ('Content-Type', 'text/plan') ]
	
	queryString = environ.QUERY_STRING
	queryList = queryString.split('&')
	body = ''
	i = 0
	for element in queryList :
		body += element[i] + '<br>'
		i += 1

	print body
	start_response(status, headers)
	return body
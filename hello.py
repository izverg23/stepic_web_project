def application(environ, start_response):                                       

	queryString = environ['QUERY_STRING']
	queryList = queryString.split('&')
	body = ''
	for element in queryList :
		body += element + '\n'
	status = '200 OK'                                                           
	
	response_headers = [                                                        
		('Content-Type', 'text/plain'),                                         
	]                                                                           

	start_response(status, response_headers)                                    

	return [response_body]
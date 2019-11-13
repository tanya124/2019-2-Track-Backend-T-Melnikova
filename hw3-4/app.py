def handler(environ, start_response):
    data = b'Hello, world'
    headers = [('Content-Type', 'text/plain'),
            ('Content-Lenght', str(len(data)))]
    start_resoponse('200 OK', headers)
    return [data]

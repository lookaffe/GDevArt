import webapp2
from scripts import scrape

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('''
        	<html>
        		<head><title>Scrape</title></head>
        		<body>
        			<p>Insert URL</p>
        			<form action="/" method="post">
        				<div>http://<textarea name="selURL" rows="1" cols="60"></textarea></div>
						<div><input type="submit" value="Scrape!"></div>
        			</form>
        		</body>
        	</html>''')
    
    def post(self):
	    url = self.request.get('selURL')
	    res = scrape.scrape(url)
	    self.response.write(res)

app = webapp2.WSGIApplication([('/', MainHandler)], debug=True)

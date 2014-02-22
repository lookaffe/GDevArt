import webapp2
from scripts import scrape
from webapp2_extras import jinja2

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
        self._render('visualization.html', data=res)

    def _render(self, template, **value):
        j = jinja2.get_jinja2()
        html = j.render_template(template, **value)
        self.response.write(html)


app = webapp2.WSGIApplication([('/', MainHandler)], debug=True)

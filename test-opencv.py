import webapp2


class GeneralHandler(webapp2.RequestHandler):
    def get(self, file_path):
        self.response.out.write("Visited: " + file_path)


app = webapp2.WSGIApplication([
    webapp2.Route(r"/<file_path:[*]+>", GeneralHandler, name="file_path")
])

import tornado.ioloop
import tornado.web
import os, sys

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		#self.write("Hello World!")
		self.render('index.html')

handlers = [
    (r"/", MainHandler),
]

settings = dict(
	template_path=os.path.join(os.path.dirname(__file__), "templates"),
)

application = tornado.web.Application(handlers, **settings)

if __name__ == "__main__":
	application.listen(sys.argv[1])
	tornado.ioloop.IOLoop.instance().start()
import waitress
import app

waitress.serve(app.create_app(), port=8080)

from .views import Handler

handler = Handler()


def setup_routes(app):
    app.router.add_route('GET', '/', handler.index)
    app.router.add_route('GET', '/status', handler.status)

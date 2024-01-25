menu = [
    {'id': 0, 'title': 'Home', 'url_name': 'home'},
    {'id': 1, 'title': 'Catalog', 'url_name': 'catalog'},
    {'id': 2, 'title': 'Reviews', 'url_name': 'reviews'},
    {'id': 3, 'title': 'Contacts', 'url_name': 'contacts'}
]


def get_aerien_context(request):
    return {'mainmenu': menu}

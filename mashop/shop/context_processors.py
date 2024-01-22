menu = [
    {'id': 0, 'title': 'Home', 'url_name': 'home'},
    {'id': 2, 'title': 'Catalog', 'url_name': 'catalog'},
    {'id': 3, 'title': 'Reviews', 'url_name': 'reviews'},
    {'id': 4, 'title': 'Contacts', 'url_name': 'contacts'}
]


def get_aerien_context(request):
    return {'mainmenu': menu}

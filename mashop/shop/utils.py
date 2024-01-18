menu = [
    {'title': 'About us', 'url_name': 'about'},
    {'title': 'Catalog', 'url_name': 'catalog'},
    {'title': 'Reviews', 'url_name': 'reviews'},
    {'title': 'Contacts', 'url_name': 'contacts'}
]


class DataMixin:
    paginate_by = 5
    title_page = None
    extra_context = {}

    def __init__(self):
        if self.title_page:
            self.extra_context['title'] = self.title_page

    @staticmethod
    def get_mixin_context(context, **kwargs):
        context['menu'] = menu
        context.update(kwargs)
        return context

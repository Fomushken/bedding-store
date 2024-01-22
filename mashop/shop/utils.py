class DataMixin:
    paginate_by = 5
    title_page = None
    menu_active = None
    extra_context = {}

    def __init__(self):
        if self.title_page:
            self.extra_context['title'] = self.title_page
        
        if self.menu_active is not None:
            self.extra_context['menu_active'] = self.menu_active

    @staticmethod
    def get_mixin_context(context, **kwargs):
        context.update(kwargs)
        return context

from django.http import HttpResponse


class DataMixin:
    paginate_by = 9
    title_page = None
    menu_active = None
    cat_selected = None
    extra_context = {}

    def __init__(self):
        if self.title_page:
            self.extra_context['title'] = self.title_page
        
        if self.menu_active is not None:
            self.extra_context['menu_active'] = self.menu_active

        if self.cat_selected is not None:
            self.extra_context['cat_selected'] = self.cat_selected

    @staticmethod
    def get_mixin_context(context, **kwargs):
        context.update(kwargs)
        return context
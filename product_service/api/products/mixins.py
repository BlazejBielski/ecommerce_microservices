from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class CacheMixin:
    cache_timeout = 60 * 15

    def get_cache_timeout(self):
        return self.cache_timeout

    def dispatch(self, *args, **kwargs):
        return cache_page(self.get_cache_timeout())(super(CacheMixin, self).dispatch)(*args, **kwargs)

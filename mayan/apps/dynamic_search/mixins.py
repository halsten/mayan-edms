from __future__ import unicode_literals

from django.http import Http404
from django.utils.encoding import force_text

from .classes import SearchModel


class SearchModelMixin(object):
    def get_search_model_name(self):
        return self.kwargs.get(
            'search_model', self.request.GET.get(
                '_search_model', self.request.POST.get('_search_model')
            )
        )

    def get_search_model(self):
        try:
            return SearchModel.get(self.get_search_model_name())
        except KeyError as exception:
            raise Http404(force_text(exception))

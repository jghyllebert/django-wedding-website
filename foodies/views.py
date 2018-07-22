from django.views.generic.edit import FormView

from .forms import SearchForm
from .get_places import GooglePlaces


class SearchPlaceView(FormView):
    form_class = SearchForm
    template_name = 'foodies/search.html'

    def form_valid(self, form):
        context = self.get_context_data(form=form)
        context['results'] = GooglePlaces().find_places(query=form['name'])
        return self.render_to_response(context)

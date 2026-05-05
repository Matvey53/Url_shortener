from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import (
    FormView, TemplateView, View, DetailView
)

from .forms import UrlForm
from .models import Url
from .services import create_short_code


class MainPageView(FormView):
    template_name = 'links/main.html'
    form_class = UrlForm
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.short_code = create_short_code()
        self.object.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse(
            'links:success_page',
            kwargs={'short_code': self.object.short_code}
        )


class SuccessPageView(DetailView):
    model = Url
    template_name = 'links/success_page.html'
    context_object_name = 'url'
    slug_field = 'short_code'
    slug_url_kwarg = 'short_code'


class RedirectView(View):
    def get(self, request, short_code):
        url = get_object_or_404(Url, short_code=short_code, is_active=True)
        url.clicks += 1
        url.save(update_fields=['clicks'])
        return redirect(url.original_url)


class StatsPageView(DetailView):
    model = Url
    template_name = 'links/stats.html'
    context_object_name = 'url'
    slug_field = 'short_code'
    slug_url_kwarg = 'short_code'

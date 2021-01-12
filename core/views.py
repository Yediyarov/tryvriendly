from django.shortcuts import render
from django.views.generic import TemplateView, ListView

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class TermsView(TemplateView):
    template_name = 'termandconditions.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


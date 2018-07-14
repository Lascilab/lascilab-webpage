# -*- encoding: utf-8 -*-

from django.views.generic import TemplateView

from index.models import BannerImage


class Index(TemplateView):
    template_name = 'index/index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['banner_images'] = BannerImage.objects.all()
        return context


class History(TemplateView):
    template_name = 'index/history.html'
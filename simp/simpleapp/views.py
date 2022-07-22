from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product


class ProductsList(ListView):
    model = Product  # Указываем модель, объекты которой мы будем выводить
    ordering = 'name'  # Поле, которое будет использоваться для сортировки объектов
    # Указываем имя шаблона, в котором будут все инструкции о том, как именно пользователю должны быть показаны наши объекты
    template_name = 'products.html'
    # Это имя списка, в котором будут лежать все объекты. Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'products'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next_sale'] = None #'Распродажа уже в эту пятницу!!!'
        return context

class ProductDetail(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'


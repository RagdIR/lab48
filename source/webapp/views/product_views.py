from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.models import Product
from webapp.forms import ProductForm

class SearchView(ListView):
    template_name = 'index.html'
    ordering = ['category', 'name']
    search_fields = ['name__icontains']

    def get_queryset(self):
        return super().get_queryset().filter(amount__gt=0)


class IndexView(ListView):
    # def index_view(request):
    #     is_admin = request.GET.get('is_admin', None)
    #     # if is_admin:
    #     data = Product.objects.all()
    #     # return render(request, 'index.html', context={'products': data})
    #     # else:
    #     #     data = Product.objects.filter('amount').values('min_value > 0')
    #     return render(request, 'index.html', context={
    #             'products': data
    #     })

    model = Product
    template_name = 'index.html'
    ordering = ['category', 'name']
    search_fields = ['name__icontains']
    paginate_by = 5
    context_object_name = 'products'

    def get_queryset(self):
        return super().get_queryset().filter(amount__gt=0)

class ProductView(DetailView):
    form_class = ProductForm
    model = Product
    template_name = 'product/product_view.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         tasks, page, is_paginated = self.paginate_tasks(self.object)
#         context['page_obj'] = page
#         context['is_paginated'] = is_paginated
#         print(context)
#         return context
#
#     def paginate_tasks(self, project):
#         product = project.project.all().order_by('-updated_at')
#         if tasks.count() > 0:
#             paginator = Paginator(tasks, self.paginate_tasks_by, orphans=self.paginate_tasks_orphans)
#             page_number = self.request.GET.get('page', 1)
#             page = paginator.get_page(page_number)
#             is_paginated = paginator.num_pages > 1
#             return page.object_list, page, is_paginated
#         else:
#             return tasks, None, False


# def product_view(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {'product': product}
#     return render(request, 'product/product_view.html', context)


# def product_create_view(request):
#     if request.method == "GET":
#         return render(request, 'product/product_create.html', context={
#             'form': ProductForm()
#         })
#     elif request.method == 'POST':
#         form = ProductForm(data=request.POST)
#         if form.is_valid():
#             product = Product.objects.create(
#                 name=form.cleaned_data['name'],
#                 description=form.cleaned_data['description'],
#                 category=form.cleaned_data['category'],
#                 amount=form.cleaned_data['amount'],
#                 price=form.cleaned_data['price'],
#             )
#             return redirect('product_view', pk=product.pk)
#         else:
#             return render(request, 'product/product_create.html', context={
#                 'form': form
#             })
#     else:
#         return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/product_create.html'

    def get_success_url(self):
        return reverse('product_view', kwargs={'pk': self.object.pk})


# def product_update_view(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     if request.method == "GET":
#         form = ProductForm(initial={
#             'name': product.name,
#             'description': product.description,
#             'category': product.category,
#             'amount': product.amount,
#             'price': product.price
#         })
#         return render(request, 'product/product_update.html', context={
#             'form': form,
#             'product': product
#         })
#     elif request.method == 'POST':
#         form = ProductForm(data=request.POST)
#         if form.is_valid():
#             product.name = form.cleaned_data['name']
#             product.description = form.cleaned_data['description']
#             product.category = form.cleaned_data['category']
#             product.amount = form.cleaned_data['amount']
#             product.price = form.cleaned_data['price']
#             product.save()
#             return redirect('product_view', pk=product.pk)
#         else:
#             return render(request, 'product/product_update.html', context={
#                 'product': product,
#                 'form': form
#             })
#     else:
#         return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/product_update.html'

    def get_success_url(self):
        return reverse('product_view', kwargs={'pk': self.object.pk})

# def product_delete_view(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     if request.method == 'GET':
#         return render(request, 'product/product_delete.html', context={'product': product})
#     elif request.method =='POST':
#         product.delete()
#         return redirect('index')
#     else:
#         return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product/product_delete.html'
    success_url = reverse_lazy('index')
from django.http import  JsonResponse

from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


from .models import Article

from .forms import ArticleForm


class ArticleListView(ListView):
    model = Article
    template_name = "article/article_list.html"
    context_object_name = "articles"
    ordering = ['-published_date']  # Order articles by published date in descending order


class ArticleDetailView(DetailView):
    model = Article
    template_name = "article/detail.html"
    context_object_name = "article"

    def get_context_data(self, **kwargs):
        # Add additional context (latest articles) to the template
        context = super().get_context_data(**kwargs)
        context['article_list'] = Article.objects.order_by("-published_date")[:15]
        return context


class ArticleCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article/create_article.html'
    context_object_name = 'article'
    permission_required = 'article.add_article'

    def form_valid(self, form):
        # Handle valid form submission and save the form
        form.save()
        return JsonResponse({'success': True})

    def form_invalid(self, form):
        # Handle invalid form submission and return errors as JSON
        errors = {field: error.get_json_data(escape_html=True) for field, error in form.errors.items()}
        return JsonResponse({'success': False, 'errors': errors})



class ArticleDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Article
    context_object_name = 'article'
    permission_required = 'article.delete_article'


    def delete(self, request, *args, **kwargs):
        # Override delete to return a JSON response
        self.object = self.get_object()
        self.object.delete()
        return JsonResponse({'success': True})

    def post(self, request, *args, **kwargs):
        # Delegate POST requests to the delete method
        return self.delete(request, *args, **kwargs)


class ArticleUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article/update_article.html'
    context_object_name = 'article'
    permission_required = 'article.change_article'


    def form_valid(self, form):
        # If the form is valid, save it and return a success response
        form.save()
        return JsonResponse({'success': True})

    def form_invalid(self, form):
        # If the form is invalid, return errors as JSON
        errors = {field: error.get_json_data(escape_html=True) for field, error in form.errors.items()}
        return JsonResponse({'success': False, 'errors': errors})






#Article list
# def index(request):
#     article = Article.objects.order_by('-published_date')
#     return render(request , "article/article_list.html", {"article": article})


# Update article
# Update views
# def update(request, id):
#     article = get_object_or_404(Article, pk=id)
#     if request.method == 'POST':
#         form = ArticleForm(request.POST, instance=article)
#         if form.is_valid():
#             form.save()
#             return JsonResponse({'success': True})
#         else:
#             errors = {field: error.get_json_data(escape_html=True) for field, error in form.errors.items()}
#             return JsonResponse({'success': False, 'errors': errors})  
#     else:
#         form = ArticleForm(instance=article)
#     return render(request, 'article/update_article.html', {'form': form})


# Delete view
# def delete(request, id):

#     article = get_object_or_404(Article, pk=id)

#     if request.method == 'POST':

#         article.delete()

#         return JsonResponse({'success': True})
    
#     return JsonResponse({'success': False, 'errors': 'Invalid request method'})  

# Create article
# def detail(request, id):
#     article_list = Article.objects.order_by("-published_date")[:15]
#     article = get_object_or_404(Article, pk=id)
#     return render(request, "article/detail.html", {"article": article, "article_list": article_list})

# # def create_article(request):
#     if request.method == 'POST':
#         form = ArticleForm(request.POST, request.FILES)
#         if form.is_valid():
#             print(request.FILES)
#             form.save()
#             return JsonResponse({'success': True})
#         else:
#             errors = {field: error.get_json_data(escape_html=True) for field, error in form.errors.items()}
#             return JsonResponse({'success': False, 'errors': errors})  
#     else:
#         form = ArticleForm()
#     return render(request, 'article/create_article.html', {'form': form})

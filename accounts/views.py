from django.shortcuts import render
# from django.

# Create your views here.
class IndexView(TemplateView):
    template_name ='index.html'
    queryset=PhotoPost.objects.order_by('-posted_at')

    paginate_by = 9
from django.shorcuts import render

def post_list(request):
    retur render(request, 'blog/post_list.html', {})

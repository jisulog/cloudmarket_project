from django.views.generic import ListView
from market.models import Post

# Create your views here.
# CBV(Class Based View) 사용하기

class PostList(ListView):
    paginate_by = 10
    def get_queryset(self):
        return Post.objects.order_by('-create_date')
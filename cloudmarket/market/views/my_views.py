from django.views.generic import ListView
from market.models import Post, Comment
from django.db.models import Q
from django.urls import reverse_lazy

'''
class BookListView(generic.ListView):
    model = Book
    context_object_name = 'my_book_list'   # your own name for the list as a template variable
    queryset = Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    template_name = 'books/my_arbitrary_template_name_list.html'  # Specify your own template name/location
'''

class MyPostList(ListView):
    context_object_name='mypost'
    paginate_by = 5 # 제네릭 뷰의 강력함 : 이 코드 한줄이면 뒤부턴 페이징을 신경쓸 필요가 없다
    template_name='market/mypost_list.html'
    global mypost_list
    
    def get_queryset(self):
        global mypost_list
        mypost_list=Post.objects.order_by('-create_date')
        print(self.request.user.username)
        print(self.request.user)
        print(self.request.user.id)
        print(self.request.user.last_name)
        mypost_list=mypost_list.filter(
            Q(user_id__username=self.request.user.username) 
            #아이디로 비교 user_id__username과 user.username
        ).distinct()
        mypost_count = mypost_list.exclude().count()
        #paginate된 거 말고 전체 글 저장하는 거 찾아봐야 - context _object_name은 현재 페이지네이트되서 5개만저장됨
        #get context data overriding 하기
        print(mypost_count)
        return mypost_list #return 타입 역시 queryset. 복잡하게 생각말기(render, reverse_lazy 필요없음)

    def get_context_data(self, **kwargs):
        global mypost_list
        # 기본 구현을 호출해 context를 가져온다.
        context = super(MyPostList, self).get_context_data(**kwargs)
        # 모든 책을 쿼리한 집합을 context 객체에 추가한다.
        context['mypost'] = mypost_list
        return context 
        
        
    
    def get_success_url(self):
        return reverse_lazy('market:mypostlist', args=[1])
        
#믹스 인  , 다중상속

class MyCommentList(ListView):
    context_object_name='mycomment'
    paginate_by = 5 # 제네릭 뷰의 강력함 : 이 코드 한줄이면 뒤부턴 페이징을 신경쓸 필요가 없다
    template_name='market/mycomment_list.html'
    global mycomment_list
    
    def get_queryset(self): #오버라이딩해준 것 object list
        global mycomment_list
        mycomment_list=Comment.objects.order_by('-create_date')
        mycomment_list=mycomment_list.filter(
            Q(user_id__username=self.request.user.username) 
            #아이디로 비교 user_id__username과 user.username
        ).distinct()
        return mycomment_list #return 타입 역시 queryset. 복잡하게 생각말기(render, reverse_lazy 필요없음)

    def get_context_data(self, **kwargs):#object list
        global mycomment_list
        # 기본 구현을 호출해 context를 가져온다.
        context = super(MyCommentList, self).get_context_data(**kwargs)
        # 모든 책을 쿼리한 집합을 context 객체에 추가한다.
        context['mycomment'] = mycomment_list
        return context 

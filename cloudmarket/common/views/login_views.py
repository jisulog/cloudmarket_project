from common.forms import UserForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class CreateUserView(CreateView):  # 제네릭의 CreateView는 폼하고 연결돼서, 혹은 모델하고 연결돼서 새로운 데이터를 넣을 때 사용.
    template_name = 'common/signup.html'     # 회원가입 할 때 띄울 폼 템플릿
    form_class = UserForm
    success_url = reverse_lazy('market:postlist') # 성공하면 어디로 갈지, create_user_done은 url name
    # 여기서 reverse가 아닌 reverse_lazy를 사용하는 이유: 제네릭뷰 같은경우 타이밍 문제 때문에 reverse_lazy를 사용해야함

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


'''
def signup(request):
    """
    계정생성
    """
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('market:postlist')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})
'''
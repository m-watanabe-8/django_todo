from django.contrib.auth import login, authenticate
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView as BaseLoginView,LogoutView as BaseLogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import SignUpForm,LoginForm


# ユーザー作成
class SignupView(CreateView):
    template_name = "accounts/signup.html" 
    form_class = SignUpForm
    success_url = reverse_lazy("todo:todo-list")

    def form_valid(self, form):
        # ユーザー作成後にそのままログイン状態にする設定
        response = super().form_valid(form)
        account_id = form.cleaned_data.get("account_id")
        password = form.cleaned_data.get("password1")
        user = authenticate(account_id=account_id, password=password)
        # 認証成功の確認
        if user is not None:  
            login(self.request, user)
        return response
    
class LoginView(BaseLoginView):
    template_name = "accounts/login.html" 
    form_class = LoginForm
    # 既にログインしているユーザーをリダイレクト
    redirect_authenticated_user = True

class LogoutView(BaseLogoutView):
    success_url = reverse_lazy("accounts:login")

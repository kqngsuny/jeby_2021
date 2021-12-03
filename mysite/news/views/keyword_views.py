from django.views.generic import ListView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from ..models import Keyword


class KeywordList(LoginRequiredMixin, ListView):
    """
    키워드 리스트를 반환한다.
    """

    login_url = "common:login"
    model = Keyword

    def get_queryset(self):
        current_user = self.request.user
        keyword_list = Keyword.objects.filter(author=current_user)

        return keyword_list


class KeywordCreate(LoginRequiredMixin, CreateView):
    """
    키워드를 생성한다.
    """

    login_url = "common:login"
    success_url = reverse_lazy("news:keyword_list")
    model = Keyword
    fields = ["title", "content", "mailing"]

    def form_valid(self, form):
        keyword_last = Keyword.objects.last()
        if keyword_last:
            form.instance.order = keyword_last.pk + 1
        else:
            form.instance.order = 1

        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            response = super(KeywordCreate, self).form_valid(form)

            return response
        else:
            return redirect("news:keyword_list")


class KeywordUpdate(LoginRequiredMixin, UpdateView):
    """
    키워드를 수정한다.
    """

    login_url = "common:login"
    success_url = reverse_lazy("news:keyword_list")
    model = Keyword
    fields = ["title", "content", "mailing"]

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(KeywordUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


class KeywordDelete(LoginRequiredMixin, DeleteView):
    """
    키워드를 삭제한다.
    """

    login_url = "common:login"
    success_url = reverse_lazy("news:keyword_list")
    model = Keyword

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(KeywordDelete, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied
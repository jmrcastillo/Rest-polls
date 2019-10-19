

from django.urls import path
# Router
from rest_framework.routers import DefaultRouter
from .apiviews import PollViewSet
from .apiviews import ChoiceList, CreateVote


# router for polls
router = DefaultRouter()
router.register('polls', PollViewSet, base_name="polls")


urlpatterns = [
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/",
         CreateVote.as_view(),
         name="create_vote"),
]

urlpatterns += router.urls

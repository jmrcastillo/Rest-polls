

from django.conf.urls import url
from .views import polls_list, polls_detail
from .apiviews import PollList, PollDetail


urlpatterns = [
    url(r"^polls/$", PollList.as_view(), name="polls"),
    url(r"^polls/(?P<slug>\w+)", PollDetail.as_view(), name="polls_detail")
]

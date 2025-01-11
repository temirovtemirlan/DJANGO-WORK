from django.urls import path
from .views import HallListApiView, HallCreateApiView, HallDetailViewRUD

urlpatterns = [
    path('hall-list/', HallListApiView.as_view()),
    path('hall-create/', HallCreateApiView.as_view()),
    path('hall-details/<int:id>', HallDetailViewRUD.as_view())
]
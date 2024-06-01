from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView
from sse_app.views import sse_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', GraphQLView.as_view(graphiql=True)),
    path('events/', sse_view),
]

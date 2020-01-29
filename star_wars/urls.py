# from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

from graphene_django.views import GraphQLView

from star_wars.schema import schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', GraphQLView.as_view(graphiql=True, schema=schema)),
]

# from django.conf.urls import url, include
# from django.urls import path
# from django.contrib import admin

# from graphene_django.views import GraphQLView

# from cookbook.schema import schema

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('graphql/', GraphQLView.as_view(graphiql=True, schema=schema)),
# ]


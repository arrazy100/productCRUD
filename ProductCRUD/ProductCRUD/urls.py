"""ProductCRUD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import include, path, re_path

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title='Product CRUD',
        default_version='v1',
        description=
        '''
            <ul><b>**CREATE A RESTFUL API** </b> 
            <li>API<ul>
                <li>Product :list,  create, read, update, delete</li>
                <li>Category : list, create</li>
            </ul></li>
            <li>Auto generate code in create product if field is empty else if already exists code then increase 1 in the last of code</li>
            <li>validation (The choice is yours)</li>
            <li>store to database</li>
            <li>push code to repository like github, gitlab, bitbucket or etc.</li>
            </ul>
            <p>
            <ul><b>**PLUS VALUE** </b> 
            <li>  create a docker file to run in docker environment</li>
            <li>  generate api documentation like swagger</li>
            </ul>
        '''
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    # url='http://localhost:8080'
)

swagger_urls = [
    path(
        '',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui',
    )
]

urlpatterns = [
    path('', include('app.urls'))
] + swagger_urls

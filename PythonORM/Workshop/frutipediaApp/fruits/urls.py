from django.urls.conf import path, include
from fruits.views import index_view, dashboard_view, create_fruit_view, create_category_view, details_fruit_view, \
    edit_fruit_view, delete_fruit_view

urlpatterns = [
    path('', index_view, name='index'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('create-fruit/', create_fruit_view, name='create-fruit'),
    path('create-category/', create_category_view, name='create-category'),
    path('<int:fruit_id>/', include(
        [
            path('details-fruit/', details_fruit_view, name='details-fruit'),
            path('edit-fruit/', edit_fruit_view, name='edit-fruit'),
            path('delete-fruit/', delete_fruit_view, name='delete-fruit'),
        ]
    ))

]


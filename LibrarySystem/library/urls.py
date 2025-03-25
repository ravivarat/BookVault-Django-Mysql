from django.urls import path
from . import views
from django.shortcuts import redirect

urlpatterns = [
    # ✅ Home and Authentication URLs
    path('', views.home, name='home'),
    path('signup/', views.admin_signup, name='admin_signup'),          # Admin signup
    path('admin-login/', views.admin_login, name='admin_login'),       # Admin login
    path('logout/', views.admin_logout, name='admin_logout'),          # Admin logout

    # ✅ Admin CRUD URLs
    path('books/', views.book_list, name='book_list'),                 # List books (Admin)
    path('books/create/', views.book_create, name='book_create'),      # Create book
    path('books/<int:book_id>/edit/', views.book_update, name='book_update'),  # Update book
    path('books/<int:book_id>/delete/', views.book_delete, name='book_delete'),  # Delete book

    # ✅ Student URLs
    path('student/', views.student_book_list, name='student_view'),
    # path('student/', views.student_book_list, name='student_book_list'),         # Student home
    # path('student/books/', views.student_book_list, name='student_book_list'),  # Student book list
]



#
# from django.urls import path
# from . import views
# from django.shortcuts import redirect
#
# urlpatterns = [
#     # path('', views.testing, name='testing'),
#     path('', views.home, name='home'),
#     # path('', lambda request: redirect('admin_login')),
#     path('admin-login/', views.admin_login, name='admin_login'),  # Admin login
#     path('books/', views.book_list, name='book_list'),  # CRUD operations
#     path('student/', views.student_view, name='student_view'),    # Student view
#     path('signup/', views.admin_signup, name='admin_signup'),
#     path('login/', views.admin_login, name='admin_login'),
#     # path('books/', views.book_list, name='book_list'),  # Books info page
#     path('logout/', views.admin_logout, name='admin_logout'),
#     path('student/', views.student_view, name='student_view'),
#     # Admin CRUD URLs
#     path('books/', views.book_list, name='book_list'),
#     path('books/create/', views.book_create, name='book_create'),
#     path('books/<int:book_id>/edit/', views.book_update, name='book_update'),
#     path('books/<int:book_id>/delete/', views.book_delete, name='book_delete'),
#
#     # Student View Books
#     path('student/books/', views.student_book_list, name='student_book_list'),
# ]
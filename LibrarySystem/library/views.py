from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Book

# def testing(request):
#     return redirect('test.html')

from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from .models import Book
from django.contrib.auth import authenticate, login
from django.contrib import messages


def home(request):
    return render(request, 'home.html')


# Admin Signup
def admin_signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists!')
            return redirect('admin_signup')

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        messages.success(request, 'Admin account created successfully!')
        return redirect('admin_login')

    return render(request, 'signup.html')




# Admin Logout
def admin_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('admin_login')


# Student View - Display all books
# def student_view(request):
#     books = Book.objects.all()
#     return render(request, 'student_view.html', {'books': books})


# def book_list(request):
#     """ Display all books """
#     books = Book.objects.all()
#     return render(request, 'book_lis_admin.html', {'books': books})
#
# # Books info page (only accessible after admin login)
# @login_required
# def book_list(request):
#     books = Book.objects.all()
#     return render(request, 'book_lis_admin.html', {'books': books})


from .models import Admin


def admin_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # Check if the admin exists in the database
        try:
            admin = Admin.objects.get(email=email)
        except Admin.DoesNotExist:
            messages.error(request, 'Invalid email or password')
            return redirect('admin_login')

        # Check password
        if admin.password == password:
            # Use Django's session to authenticate admin
            request.session['admin_id'] = admin.id
            request.session['admin_email'] = admin.email
            messages.success(request, 'Login successful!')
            return redirect('book_list')  # Redirect to books page
        else:
            messages.error(request, 'Invalid email or password')
            return redirect('admin_login')

    return render(request, 'admin_login.html')


# 📌 List all books (Admin)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'admin/book_list_admin.html', {'books': books})
# 📌 View Books for Students (Read-only)


def student_book_list(request):
    books = Book.objects.all()
    return render(request, 'student/book_list.html', {'books': books})



# 📌 Create new book (Admin)
def book_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        isbn = request.POST['isbn']
        available = request.POST.get('available') == 'on'  # Checkbox value
        published_date = request.POST['published_date']

        # Create new book
        Book.objects.create(
            title=title,
            author=author,
            isbn=isbn,
            available=available,
            published_date=published_date
        )
        messages.success(request, 'Book added successfully!')
        return redirect('book_list')

    return render(request, 'admin/book_form.html')


# 📌 Update book (Admin)
def book_update(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.isbn = request.POST['isbn']
        book.available = request.POST.get('available') == 'on'
        book.published_date = request.POST['published_date']

        book.save()
        messages.success(request, 'Book updated successfully!')
        return redirect('book_list')

    return render(request, 'admin/book_form.html', {'book': book})


# 📌 Delete book (Admin)
def book_delete(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    messages.success(request, 'Book deleted successfully!')
    return redirect('book_list')



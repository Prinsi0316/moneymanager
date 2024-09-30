from django.urls import path
from . import views
from .views import notes_view, rename_note_view, delete_note_view


urlpatterns = [
    path('', views.index, name='index'),          # Homepage
    path('records/', views.records, name='records'),
    path('notes/', notes_view, name='notes'),
    path('reports/', views.reports, name='reports'),
    path('profile/', views.profile, name='profile'),
path('submit-rating/', views.submit_rating, name='submit_rating'),  # Ensure this is defined
    path('add-new/', views.add_new, name='add-new'),
    path('payment/', views.payment, name='payment'),
path('rename_note/', rename_note_view, name='rename_note'),
    path('delete_note/', delete_note_view, name='delete_note'),



]

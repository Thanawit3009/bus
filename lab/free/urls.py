from django.urls import path
from .views import CourseListView, CourseDeleteView, course_idsearch, course_namesearch, editcourseview

urlpatterns = [
    path('course/', CourseListView.as_view(), name='course_list'),  # ✅ แสดงรายการคอร์ส
    path('course/delete/<str:pk>/', CourseDeleteView.as_view(), name='course_delete'),  # ✅ ลบคอร์ส
    path("search/", course_idsearch,name="search_id"),
    path("namesearch/",course_namesearch, name="search_name"),
    path("course/update/<str:pk>", editcourseview.as_view(),name="update_course"),
]

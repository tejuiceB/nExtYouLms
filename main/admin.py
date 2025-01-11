from django.contrib import admin
from .models import Course, Enrollment

admin.site.register(Course)
admin.site.register(Enrollment)
from django.contrib import admin
from .models import Course, CourseStudent

# Unregister the Course model if it is already registered
admin.site.unregister(Course)

# Custom admin class for the Course model
class CourseAdmin(admin.ModelAdmin):
    # Restrict adding courses to staff users (admins)
    def has_add_permission(self, request):
        # Only allow superusers or staff users to add courses
        return request.user.is_staff  # staff users can add courses

    def has_change_permission(self, request, obj=None):
        # Only staff can change courses
        return request.user.is_staff

    def has_delete_permission(self, request, obj=None):
        # Only staff can delete courses
        return request.user.is_staff

    list_display = ['title', 'instructor', 'category', 'price']
    search_fields = ['title', 'instructor__username']

# Register the Course model with the custom admin class
admin.site.register(Course, CourseAdmin)
admin.site.register(CourseStudent)  # Assuming this model doesn't need restriction

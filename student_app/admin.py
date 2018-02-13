from django.contrib import admin
from student_app.models import *

class SchoolAdmin(admin.ModelAdmin):
	actions = ['enable']

	fieldsets = (
	    ('School Data', {'fields': ('name', 'address', 'contact_no', 'email', 'website', 'rating',)}),
	    ('Permission', {'fields': ('enabled', )}),
		('Date', {'fields': ('created_date', 'modified_date')}),
	)

	#exclude = ('rating', 'contact_no',)

	search_fields = ('name','address')
	ordering = ('name',)
	list_display = ('name', 'website', 'rating', 'created_date', 'modified_date')
	list_display_links = ('name', 'website')
	list_filter = ('name', 'rating')
	readonly_fields = ('created_date', 'modified_date')

	def enable(self, request, queryset):
		queryset.update(enabled=True)


class StudentAdmin(admin.ModelAdmin):
	actions = ['enable']

	fieldsets = (
	    ('Student Data', {'fields': ('first_name', 'last_name', 'image', 'residental_address', 'email',)}),
	    ('Educational Details', {'fields': ('school', 'standard', 'roll_no', 'fees')}),
	    ('Permission', {'fields': ('enabled', )}),
		('Date', {'fields': ('created_date', 'modified_date')}),
	)

	search_fields = ('first_name', 'last_name', 'residental_address')
	ordering = ('first_name',)
	list_display = ('first_name', 'school', 'standard', 'created_date', 'modified_date')
	list_display_links = ('first_name',)
	list_filter = ('standard',)
	readonly_fields = ('created_date', 'modified_date')

	def enable(self, request, queryset):
		queryset.update(enabled=True)


admin.site.register(School, SchoolAdmin)
admin.site.register(Student, StudentAdmin)

from django.contrib import admin
from django import forms
from contact.models import ContactContent


# Register your models here.

class ContactContentAdmin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(ContactContentAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'content':
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
        return formfield


admin.site.register(ContactContent, ContactContentAdmin)

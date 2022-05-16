from django.contrib import admin
from .models import Article, Reporter

# Register your models here.


class ReporterAdmin(admin.ModelAdmin):
    pass
admin.site.register(Reporter, ReporterAdmin)
admin.site.register(Article, ReporterAdmin)
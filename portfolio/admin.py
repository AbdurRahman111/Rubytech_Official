from django.contrib import admin
from .models import Portfolio, Portfolio_Category, Portfolio_Details, Newsletter_Table, contact_form

# Register your models here.

# Portfolio
admin.site.register(Portfolio_Category),
admin.site.register(contact_form),
admin.site.register(Newsletter_Table),

class P_Details_Inline(admin.StackedInline):
    model = Portfolio_Details

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    inlines = [
        P_Details_Inline,
        ]
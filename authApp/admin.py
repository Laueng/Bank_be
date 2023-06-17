from django.contrib import admin
from .models.user import User
from .models.account import Account

"""
The models are registered in the application.
"""

admin.site.register(User)
admin.site.register(Account)
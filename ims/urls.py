from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    path("accounts/", include("accounts.urls")),
    path("inventory/", include("inventory.urls")),
    path("purchases/", include("purchases.urls")),
    path("sales/", include("sales.urls")),
    path("reports/", include("reports.urls")),

    path("", include("inventory.urls")),  # Home page
]

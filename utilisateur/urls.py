from django.urls import path,include
from .views import*
from rest_framework.urlpatterns import format_suffix_patterns

from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns=format_suffix_patterns([
    #Crée des donateur
    path('donateurm/', CreateDonateur.as_view(),name='registers-donateurm'),
    path('donateurorg/',CreateDonateurOr.as_view(),name='registers-donateurorg'),
    #Effectuer des dons
    path('efdoargent/',EffectuerDonsArg.as_view(),name='registers-donArg'),
    path('efdoobjet/',EffectuerDonsObj.as_view(),name='registers-donOjets'),
    #Afficher ses dons
    path('argent/', Argen.as_view(),name='detail-donard'),
    path('natures/', Nature.as_view(),name='detail-donnd'),
    path('argend/<int:pk>/', Argend.as_view(),name='detail-donard'),
    path('natured/<int:pk>/', Natured.as_view(),name='detail-donnd'),
    #connexion
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
])
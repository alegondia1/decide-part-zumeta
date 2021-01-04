from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.CensusCreate.as_view(), name='census_create'),
    path('<int:voting_id>/', views.CensusDetail.as_view(), name='census_detail'),
    path('group_by_voter/', views.group_by_voter, name='grouping_voter'),
    path('group_by_voter/<int:voter_id>', views.voter_census, name="voter_census"),
    path('group_by_voting/', views.group_by_voting, name='grouping_voting'),
    path('group_by_voting/<int:voting_id>', views.voting_census, name="voting_census"),
    path('group_by_adscripcion/', views.group_by_adscripcion, name='grouping_adscripcion'),
    path('group_by_adscripcion/<str:adscripcion>', views.adscripcion_census, name="adscripcion_census"),
    path('all_census/',views.all_census, name='all_census'),
    path('filter_by_voting/<int:voting_id>',views.filter_by_voting, name='filter_by_voting'),
    path('filter_by_adscripcion/<str:adscripcion>',views.filter_by_adscripcion, name='filter_by_adscripcion')
]

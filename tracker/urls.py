from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


app_name = "tracker"
urlpatterns = [
    path("", views.home, name="home"),
    path("view/", views.disp, name="disp"),
    path("view/trend", views.disp_month, name="disp_month"),
    path("view/trend/apps", views.appwise, name="appwise"),
    path("view/trend/apps/view", views.appwise_suc, name="appwisesuc"),
    # path("view/analysis", views.scr_graph, name="analysis"),
    path("view/goals", views.disp_goal, name="dispgoal"),
    path("view/goals/add", views.add_goal, name="addgoal"),
    path("view/goals/add/success", views.add_goal_suc, name="addgoalsuc"),
    path("view/goals/edit", views.edit_goal, name="editgoal"),
    path("view/goals/delete", views.del_goal, name="delgoal"),
    path("view/goals/delete/success", views.del_goal_suc, name="delgoalsuc"),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),               #for some reason was not included in default auth configs
    path('accounts/signup/', views.signup, name='signup'),                  #adding(registering) a new user
    #for adding, deleting, modifying vehicles

]

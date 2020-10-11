"""TICTACTOE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

"""

from django.conf import settings

from django.contrib import admin
from django.urls import path, include

from django.conf.urls import  url

from .views import welcome

from django.contrib.auth.views import LoginView

from django.contrib.auth.views import LogoutView




from PLAYER.views  import signup_function_view

from Forum.views import (
welcome_to_game_apps_view,
 list_view,
 detail_forum, 
 create_post, 
 post_reply,
  update_reply,
  update_post,
  my_view,
  my_view1,
  user_profile_view,
  user_contribution_view,
  post_reply_in_reply,
  view_replies_in_reply,
  update_reply_in_reply,
  user_account_view,
  update_user_profile,
  settings_view,
  list_user_members,
  send_email_message,
  display_mail_messages,
  send_email_message_to_user,
  view_friends_of_this_user,
  add_friend,
  personalize_account,
  usermember_delete_view,

  )




from GameApps.views import (display_available_games, authors_view, display_rules,

  display_app_to_rate, display_apps_rating) 


urlpatterns = [
                path('admin/', admin.site.urls),
              

                #player
               path('', welcome, name='Game_apps_welcome'),


               path('login/', LoginView.as_view(template_name="PLAYER/LOGIN_FORM.html"),
               name='player_login'),
               path('logout/', LogoutView.as_view(), name='player_logout'),
               path('signup', signup_function_view, name='player_signup'),


               #forum

               path("game-apps-welcome/", welcome_to_game_apps_view, name="welcome_to_game_apps_view"),

               path('list-posts/', list_view, name="list_view"),
               path('detail-forum/<int:id>/', detail_forum, name="detail_forum"),
               path('create/', create_post, name="create_post"),

               path('list-posts/create/', create_post, name="create_post"),

               path('update/<int:id>/', update_post, name="update_post"),

               path('reply/<int:id>/', post_reply, name="post_reply"),
               path('update-message/<int:id>/', update_reply, name="update_reply"),
               path('list-posts/update/<int:id>/', my_view, name="my_view"),
               path('list-posts/reply/<int:id>/', my_view1, name="my_view1"),
           
               path('user/<int:id>/', user_profile_view, name='user_profile_view'),
               path('user/work/<int:id>/', user_contribution_view, name='user_contribution_view'),
               path('reply-in-reply/<int:id>/', post_reply_in_reply, name="post_reply_in_reply"),

               path('replies-to-reply/<int:id>/', view_replies_in_reply, name="view_replies_in_reply"),

               path('update-message-in-reply/<int:id>/', update_reply_in_reply, name="update_reply_in_reply"),

               #gameapps

               path('game-apps/', display_available_games, name='display_available_games'),

               path("authors/", authors_view, name="authors"), 

               path("user-account/<int:id>/", user_account_view, name="user_account_view"), 

              # path("create-user/", create_user_profile, name="create_user_profile"),


              path("update-user-profile/<int:id>/", update_user_profile, name="update_user_profile"),

              path("settings/<int:id>/", settings_view, name="settings_view"),

              
              path("usermembers/", list_user_members, name="list_user_members"),

              path("send-email/", send_email_message, name="send_email_message" ),

              path("access-emails/<int:id>/", display_mail_messages, name="display_mail_messages" ),
 
              path("send-mail-to-user/<int:id>/", send_email_message_to_user, name="send_email_message_to_user" ),

              
              path("friends/<int:id>/", view_friends_of_this_user, name="view_friends_of_this_user" ),

              path("add-user-friend/<int:id1>/<int:id2>/", add_friend, name="add_friend" ),


              path("rules-to-become-usermember/", display_rules, name="display_rules"),


              path("app-rating/<int:id>/", display_app_to_rate, name="display_app_to_rate"),


              path("user/work/<int:id>/send-mail-to-user/", send_email_message_to_user, name="send_email_message_to_user" ),


              path("personalize-user-account/<int:id>/", personalize_account, name="personalize_account"),


              path("user-account/<int:id>/personalize-user-account/", personalize_account, name="personalize_account"),

              
              path("user-account-delete/<int:id>/", usermember_delete_view, name="usermember_delete_view"),

              
              path("apps-rating/", display_apps_rating, name="display_apps_rating"),


]


if settings.DEBUG:
  #test mode
  from django.conf.urls.static import static
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



















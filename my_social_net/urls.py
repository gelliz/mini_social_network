from django.urls import include, path, re_path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from auth_user.views import signup_save, signup_page, user_login, user_logout, activate_account
from user_records.views import add_record, delete_record, add_like, add_repost, add_comment
from photo.views import person_photo, delete_photo
from chat.views import show_all_my_chats, new_message, delete_chat
from .views import (
    show_main,
    search_page,
    show_person_page,
    page_all_person_friends,
    my_settings,
    add_freind,
    delete_friendship,
    show_person_friends,
    accept_refuse_friend,
)

urlpatterns = [
    # Examples:
    # url(r'^$', 'my_social_net.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    path('admin/', admin.site.urls),
    path('', show_main),

    # персонализация
    path('signup_save', signup_save),
    path('signup', signup_page),
    path('login', user_login),
    path('logout', user_logout),
    # path('activate/<uidb64>/<token>/', activate_account, name='activate'),

    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', activate_account, name='activate'),

    # страница пользователя
    path('person/id_<int:person_id>', show_person_page),
    path('person/id_<int:person_id>/friends', page_all_person_friends),

    # для авторизированного пользователя
    path('my_settings', my_settings),
    path('add_freind', add_freind),
    path('delete_friend', delete_friendship),
    path('my_friends', show_person_friends),
    path('accept_refuse_friend', accept_refuse_friend),
    path('add_record', add_record),
    path('delete_record', delete_record),
    path('add_like', add_like),
    path('add_repost', add_repost),
    path('add_comment', add_comment),
    path('person/id_<int:person_id>/photo', person_photo),
    path('delete_photo', delete_photo),
    path('my_chats', show_all_my_chats),
    path('new_message', new_message),
    path('delete_chat', delete_chat),

    # поиск
    path('search', search_page),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

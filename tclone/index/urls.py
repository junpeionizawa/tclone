from django.urls import path
from . import views

urlpatterns = [

   path('',views.index, name = 'index'),
   path('',views.index,name = 'index')
   #ツイート新規作成機能で作成したツイートの、idの番号
   path('delete/<int:tweet_id>', views.delete, name='delete'), # この行を追加
   #更新
   path('update/<int:tweet_id>', views.update, name='update'), # この行を追加
]


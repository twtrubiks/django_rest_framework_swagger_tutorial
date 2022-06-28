# django-rest-framework-swagger-tutorial

Django-REST-Swagger 基本教學

* [Youtube Tutorial](https://youtu.be/ayTF26EIMFU)

相信大家在網路上一定都看過 **API 文件**，

那我們該如何撰寫 **API 文件** 給別人看呢 ？

今天我要教大家使用 [drf-yasg](https://github.com/axnsan12/drf-yasg) 來完成他 ！！

***溫馨小提醒***

建議大家先對 [Django](https://github.com/django/django) 以及 [Django REST framework](http://www.django-rest-framework.org/) ( DRF ) 有基礎的知識。

如果還不熟的人，可以先閱讀我之前寫的

[Django 基本教學 - 從無到有 Django-Beginners-Guide](https://github.com/twtrubiks/django-tutorial)

以及

[Django-REST-framework 基本教學 - 從無到有 DRF-Beginners-Guide](https://github.com/twtrubiks/django-rest-framework-tutorial)

先建立一些基本觀念，再來看這篇比較清楚。

## 教學

我們依照 [Django-REST-framework 基本教學 - 從無到有 DRF-Beginners-Guide](https://github.com/twtrubiks/django-rest-framework-tutorial) 這篇繼續延伸下去。

請在你的命令提示字元 (cmd ) 底下輸入

安裝 [drf-yasg](https://github.com/axnsan12/drf-yasg)
>pip install drf-yasg

### drf-yasg 設定

***請記得要將 [drf-yasg](https://github.com/axnsan12/drf-yasg) 加入設定檔***

請在 [settings.py](https://github.com/twtrubiks/django_rest_framework_swagger_tutorial/blob/master/django_rest_framework_swagger_tutorial/settings.py) 裡面的 **INSTALLED_APPS** 加入下方程式碼

```python
INSTALLED_APPS = (
    ...
    'django.contrib.staticfiles',
    'drf_yasg',
    'rest_framework',
)
```

接著我們設定 Routers 路由 ，請將 [urls.py](https://github.com/twtrubiks/django_rest_framework_swagger_tutorial/blob/master/django_rest_framework_swagger_tutorial/urls.py) 增加一些程式碼

```python
......

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
#    public=True,
   public=False, # need login
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # for rest_framework
    path('api/', include(router.urls)),
    # for rest_framework auth
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    re_path('swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path('swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path('redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
```

最後執行 Django ，然後瀏覽 [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)

你應該會看到如下圖 (如果你沒看到任何東西，可以點一下 **Show/Hide** )

![alt tag](http://i.imgur.com/qY9pz8N.png)

也可以瀏覽 [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)

![alt tag](https://i.imgur.com/WsHAMmk.png)

### 執行畫面

畫面非常漂亮，功能也非常完善，

我們可以在上面執行 **GET** , **POST** , **PUT** , **PATCH** , **DELETE** , 甚至可以直接看到執行結果，

我介紹幾個給大家當範例，看完大家就會比較了解

 ***POST***

點選編號 1 的地方，他會幫你把範例貼到左手邊，修改完值之後，直接按 **Try it out!**

![](http://i.imgur.com/RtDc29v.png)

接著你會發現下面有 Response ， 以這個範例來講，201 就是新增成功

![](http://i.imgur.com/y0tSltJ.png)

 ***GET***

 接著我們再去  **GET** ，我們剛剛新增的那筆的確有在裡面

![](http://i.imgur.com/rKf0KdN.png)

有沒有發現非常強大 :open_mouth:

接下來你可能會擔心，這樣我的資料不就會被任何人任意操作?

不用擔心，和之前介紹的 [授權 (Authentication)](https://github.com/twtrubiks/django-rest-framework-tutorial#授權-authentications-) 是一樣的。

## 授權（ Authentication ）

在 [urls.py](https://github.com/twtrubiks/django_rest_framework_swagger_tutorial/blob/master/django_rest_framework_swagger_tutorial/urls.py) 底下程式碼,

```python
urlpatterns = [
    ......
    # for rest_framework auth
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    ......
]
```

在 [views.py](https://github.com/twtrubiks/django_rest_framework_swagger_tutorial/blob/master/musics/views.py) 底下加入  **permission**

```python
# Create your views here.
class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    permission_classes = (IsAuthenticated,)
```

在 [settings.py](https://github.com/twtrubiks/django_rest_framework_swagger_tutorial/blob/master/django_rest_framework_swagger_tutorial/settings.py) 底下加入下方程式碼

設定 SWAGGER_SETTINGS 為使用 rest_framework login, logout

```python
SWAGGER_SETTINGS = {
    'LOGIN_URL': 'rest_framework:login',
    'LOGOUT_URL': 'rest_framework:logout'
}
```

也要把 [urls.py](https://github.com/twtrubiks/django_rest_framework_swagger_tutorial/blob/master/django_rest_framework_swagger_tutorial/urls.py) 中的 public 設為 `False`.

可參考 [https://drf-yasg.readthedocs.io/en/stable/settings.html](https://drf-yasg.readthedocs.io/en/stable/settings.html)

執行 Django, 然後瀏覽 [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)

你會發現，當你沒有登入的時候，你是看不到這些 API 的內容,

![alt tag](http://i.imgur.com/b3rbEZw.png)

登入之後你才有權限可以看到這些資料

我的 帳號/密碼 設定為 twtrubiks/password123 ，

Swagger 的基本介紹我們就介紹到這邊，更多的說明可以參考 [drf-yasg](https://github.com/axnsan12/drf-yasg)

## 執行環境

* Python 3.8

## Reference

* [Django](https://www.djangoproject.com/)
* [Django-REST-framework](https://www.django-rest-framework.org/)
* [drf-yasg](https://github.com/axnsan12/drf-yasg)

## License

MIT license

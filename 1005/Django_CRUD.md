### `Django CRUD`

***

#### 가상환경 / Django 설치

- `.gitignore`로 가상환경 폴더가 git에 관리되지 않게 설정

- `가상환경 생성 및 실행`

  ```zsh
  python -m venv venv
  source venv/bin/activate
  ```

- `Django 설치 및 기록`

  ```zsh
  pip install django==3.2.13
  pip freeze > requirements.txt
  ```





#### Project / App 생성 및 설정

- `Project 생성`

  ```zsh
  django-admin startproject [PJT name] .
  ```

- `App 생성`

  ```zsh
  python3 manage.py startapp [App name]
  ```

- `App 등록`

  - 생성한 `Project` ➡︎ `settongs.py` ➡︎ `INSTALLED_APPS` 에 `App name` 작성

  ```python
  INSTALLED_APPS = [
      '[PJT name]',
      ...
  ]
  ```
  
  - 생성한 `Project` ➡︎ `urls.py` 에 `App urls.py` 등록
  
  ```python
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('[App name]/', include('[App name].urls')),
  ]
  ```
  
  - `App` 디렉터리에 `urls.py` 생성 후 코드 추가
  
  ```python
  from django import views
  from django.urls import path
  from . import views
  
  app_name = 'practice'
  
  urlpatterns = [
      path('', views.index, name='index'),
  ]
  ```







#### Model(DB) 설계

- `class 정의`

  ```python
  class Article(models.Model):
      title = models.CharField(max_length=20)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      update_at = models.DateTimeField(auto_now=True)
  ```

- `migration`

  ```zsh
  python manage.py makemigrations
  python manage.py migrate
  ```

- `확인하기`

  ```zsh
  python manage.py showmigrations
  ```

  >articles
  >
  >[X] 0001_initial
  >
  >목록이 보인다면 DB에 반영된 것









#### Static files

- `.html` 파일에 이미지를 넣고 싶을 때 사용

- `app` 디렉터리 ➡︎ `static` 디렉터리 ➡︎ `static` 디렉터리 ➡︎ `images`, `css` 디렉터리 생성

- `코드 확인`

  ```python
  # [PJT]/setting.py
  
  ...
  
  INSTALLED_APPS = [
      'articles',
      ...
      'django.contrib.staticfiles',
  ]
  
  ...
  
  STATIC_URL = '/static/'
  
  ...
  ```

- `templates HTML 코드 추가`

  ```html
  <!-- [app]/templates/articles/index.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
  {% load static %}
  
  <h1>index page</h1>
  <img src="{% static 'images/chicken.png' %}" alt="chicken">
  <a href="{% url 'articles:create' %}">작성</a>
  {% for article in articles %}
  <a href="{% url 'articles:detail' article.pk %}">
      <h4>{{ article.title }}</h4>
  </a>
  <p>{{ article.created_at }}</p>
  <p>{{ article.updated_at }}</p>
  {% endfor %}
  
  {% endblock %}
  ```







#### Django Bootstrap5

- `app 등록`

  ```python
  # [PJT]/setting.py
  
  INSTALLED_APPS = [
      'articles',
      'django_bootstrap5',
  		...
  ]
  ```

- `HTML 적용`

  - `{% extends 'base.html' %}`, `{% block content %}`, `{% endblock %}` 코드 삭제
  - `Bootstrap5` 코드 추가

  ```html
  {% load django_bootstrap5 %}
  {% bootstrap_css %}
  {% bootstrap_javascript %}
  
  <h1>create page</h1>
  <form action="" method="POST">
      {% csrf_token %}
      {% bootstrap_form article_form %}
      <!-- {{ article_form.as_p }} -->
      <input type="submit" value="등록">
  </form>
  ```

  





#### CRUD 기능 구현

- `ModelForm 선언`
  
  - 선언된 모델에 따른 필드 구성
  
  ```python
  from django import forms
  from .models import Article
  
  class ArticleForm(forms.ModelForm):
    class Meta:
      model = Article
      fields = ['title', 'content']
  ```
  
- `create`

  - `form`으로 입력 받아 DB에 반영
    - 사용자에게 `form`을 제공하고, 입력 받은 데이터를 처리

  ```html
  <!-- [app]/templates/articles/index.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
  
  <h1>index page</h1>
  <a href="{% url 'articles:create' %}">작성</a>
  
  {% endblock %}
  ```

  ```html
  <!-- [app]/templates/articles/create.html -->
  
  {% load django_bootstrap5 %}
  {% bootstrap_css %}
  {% bootstrap_javascript %}
  
  <h1>create page</h1>
  <form action="" method="POST">
      {% csrf_token %}
      {% bootstrap_form article_form %}
      <!-- {{ article_form.as_p }} -->
      <input type="submit" value="등록">
  </form>
  ```

  ```python
  # [app]/urls.py
  
  from django.urls import path
  from . import views
  
  app_name = 'articles'
  
  urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
  ]
  ```

  ```python
  # [app]/views.py
  
  def index(request):
      return render(request, 'articles/index.html', context)
  
  def create(request):
      if request.method == 'POST':
          article_form = ArticleForm(request.POST)
  
          if article_form.is_valid():
              article_form.save()
              return redirect('articles:index')
  
      else:
          article_form = ArticleForm()
      context = {
          'article_form' : article_form
      }
  
      return render(request, 'articles/create.html', context=context)
  ```

- `read`

  ```python
  # [app]/views.py
  
  def index(request):
      articles = Article.objects.order_by('-pk')
      context = {
          'articles' : articles
      }
  
      return render(request, 'articles/index.html', context)
  ```

  ```html
  <!-- [app]/templates/articles/index.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
  
  <h1>index page</h1>
  <a href="{% url 'articles:create' %}">작성</a>
  {% for article in articles %}
  <h4>{{ article.title }}</h4>
  <p>{{ article.created_at }}</p>
  <p>{{ article.updated_at }}</p>
  {% endfor %}
  
  {% endblock %}
  ```

  - `detail`

  ```python
  # [app]/urls.py
  
  urlpatterns = [
      path('', views.index, name='index'),
      path('create/', views.create, name='create'),
      path('<int:pk>', views.deatail, name='detail'),
  ]
  ```

  ```python
  # [app]/views.py
  
  def deatail(request, pk):
      article = Article.objects.get(pk=pk)
      context = {
          'article' : article
      }
  
      return render(request, 'articles/detail.html', context)
  ```

  ```html
  <!-- [app]/templates/articles/detail.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
  
  <h1>detail page</h1>
  <h4>{{ article.title }}</h4>
  <p>{{ article.content }}</p>
  <p>{{ article.created_at }}</p>
  <p>{{ article.updated_at }}</p>
  
  {% endblock %}
  ```

  ```html
  <!-- [app]/templates/articles/index.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
  
  <h1>index page</h1>
  <a href="{% url 'articles:create' %}">작성</a>
  {% for article in articles %}
  <a href="{% url 'articles:detail' article.pk %}">
      <h4>{{ article.title }}</h4>
  </a>
  <p>{{ article.created_at }}</p>
  <p>{{ article.updated_at }}</p>
  {% endfor %}
  
  {% endblock %}
  ```

- `update`

  ```html
  <!-- [app]/templates/articles/detail.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
  
  <h1>detail page</h1>
  <h4>{{ article.title }}</h4>
  <p>{{ article.content }}</p>
  <a href="{% url 'articles:update' article.pk %}">수정</a>
  <p>{{ article.created_at }}</p>
  <p>{{ article.updated_at }}</p>
  
  {% endblock %}
  ```

  ```python
  # [app]/urls.py
  
  urlpatterns = [
      path('', views.index, name='index'),
      path('create/', views.create, name='create'),
      path('<int:pk>', views.deatail, name='detail'),
      path('<int:pk>/update/', views.update, name='update'),
  ]
  ```

  ```python
  # [app]/views.py
  
  def update(request, pk):
      article = Article.objects.get(pk=pk)
  
      if request.method == 'POST':
          article_form = ArticleForm(request.POST, instance=article)
  
          if article_form.is_valid():
              article_form.save()
              return redirect('articles:detail', article.pk)
      
      else:
          article_form = ArticleForm(instance=article)
      
      context = {
          'article_form' : article_form
      }
  
      return render(request, 'articles/update.html', context)
  ```

- `delete`

  ```python
  # [app]/urls.py
  
  from django.urls import path
  from . import views
  
  app_name = 'articles'
  
  urlpatterns = [
      path('', views.index, name='index'),
      path('create/', views.create, name='create'),
      path('<int:pk>', views.deatail, name='detail'),
      path('<int:pk>/update/', views.update, name='update'),
      path('<int:pk>/delete/', views.delete, name='delete'),
  ]
  ```

  ```python
  # [app]/view.py
  
  def delete(request, pk):
      Article.objects.get(pk=pk).delete()
      return redirect('articles:index')
  ```

  ```html
  <!-- [app]/templates/articles/detail.html -->
  
  {% extends 'base.html' %}
  
  {% block content %}
  
  <h1>detail page</h1>
  <h4>{{ article.title }}</h4>
  <p>{{ article.content }}</p>
  <a href="{% url 'articles:update' article.pk %}">수정</a>
  <a href="{% url 'articles:delete' article.pk %}">삭제</a>
  <p>{{ article.created_at }}</p>
  <p>{{ article.updated_at }}</p>
  
  {% endblock %}
  ```







#### admin site

- 서버의 관리자가 사용하는 페이지

- `계정 생성`

  ```zsh
  python manage.py createsperuser
  ```

  - `username`. `password`를 입력해 계정 생성
  - `email`은 선택 사항이기 때문에 건너뛸 수 있음

  ```python
  # [app]/admin.py
  
  from django.contrib import admin
  from .models import Article
  
  admin.site.register(Article)
  ```

- 서버를 실행하고 `http://localhost:8000/admin/`에 접속해 로그인하면 지금까지 작성된 DB를 확인할 수 있고, 삭제/수정/조회 할 수 있음








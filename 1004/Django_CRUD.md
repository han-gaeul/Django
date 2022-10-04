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
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
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







#### CRUD 기능 구현

- 게시글 생성
  - 사용자에게 form을 제공하고 입력 받은 데이터를 저장
  - 저장한 데이터를 index 페이지에 보냄(redirect)
- 게시글 목록
  - DB에서 데이터를 가져와 template에 전달
- 글 내용 보기
  - 특정한 pk 값의 글 내용을 보기 위해 pk 값을 넘겨줌
- 글 수정/삭제 하기
  - 특정한 pk 값의 글을 수정/삭제 하기 위해 사용자에게 form(예:버튼, 페이지, 모달 등)을 보여줌


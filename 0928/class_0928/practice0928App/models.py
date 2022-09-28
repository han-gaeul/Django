from email.policy import default
from django.db import models

# Create your models here.

class Todo(models.Model):
    # django에서 pk(id)는 자동으로 만들어짐
    # 즉 id를 정의해줄 필요가 없음
    content = models.CharField(max_length=80)

    # defalut : 데이터를 생성할 때 값을 넣지 않으면
    # 자동으로 값을 채워서 데이터를 생성 하겠다는 의미
    completed = models.BooleanField(default=False)
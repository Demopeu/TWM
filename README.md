# TWM

## Commit message 규칙

1. 구조

```
type:title

ex. git commit -m "docs: README 내용 수정"
```

- type

![type](https://github.com/Demopeu/TWM/assets/156268475/c31f78f6-67bb-46f2-a830-58590515a02e)

- title : 제목

```
docs: README 내용 수정
fix: article/views.py create함수 오류 수정
```

## 소프트웨어 도구

- Python

- JS

- HTML

- CSS

- Bootstrap

- Vue3

- Django

- VS code

- Kakao Oven

- Jira

- GitHub

## ERD(Entity Relationship Diagram)

![erd](https://github.com/Demopeu/TWM/assets/156268475/38229d0a-5c6d-4433-9cd6-2273f261b07d)

## Mock-up

1. indexView

![indexView](https://github.com/Demopeu/TWM/assets/156268475/b508dac5-02d5-4335-9985-e8b91c14da33)

2. movieView

![MovieView](https://github.com/Demopeu/TWM/assets/156268475/efd14562-4a4c-4601-8e05-d3e76a4d74f6)

3. articleView

![articlesView](https://github.com/Demopeu/TWM/assets/156268475/43b4ff35-1c58-4c21-8bad-69dac4dd9b3d)

4. profileView

![profile](https://github.com/Demopeu/TWM/assets/156268475/0ca2eb02-4d8e-4063-bdd6-a88b180464da)

## Omissions 작성법

1. 대주제 선택(ex. front, back)

2. 직접적으로 문제가 있거나, 누락된 부분이 있는 페이지 작성

    ```
    1. Login.vue

    - username, password 이모티콘 누락
    ```

    - 구동이 안될 정도의 큰 문제가 있을 경우, 대주제 바로 아래에 "##"를 이용하여 즉시 작성후 **!important**를 어미에 작성

    - 구동은 되나, 전체에 걸쳐서 오류가 있을 경우, 대주제 바로 아래에 "##"를 이용하여 즉시 작성

3. "##" 에 작성한 내용은 merge 설명에 기입 후, MM혹은 카카오톡을 이용하여 즉시 알림

4. 완료되거나 해결 된 이슈는 삭제하지 말고 취소선을 그은 이후, 대주제 completed로 이동
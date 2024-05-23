# 영화 추천 프로젝트 - TWM(Travel With Movies)

## 목차

- [프로젝트 소개](#프로젝트-소개)
    - [프로젝트 설명](#프로젝트-설명)
        - [프로젝트 로고](#프로젝트-로고)
        - [프로젝트 이름](#프로젝트-이름)
        - [프로젝트 개요](#프로젝트-개요)
        - [프로젝트 기간](#프로젝트-기간)
        - [프로젝트 상세 설명](#프로젝트-상세-설명)
        - [주요 기능 및 목표](#주요-기능-및-목표)
    - [개발 스택 및 개발 툴](#개발-스택-및-개발-툴)
    - [팀원 구성 및 역할 분담](#팀원-구성-및-역할-분담)
        - [팀장 소개](#팀장-소개)
        - [팀원 소개](#팀원-소개)
- [프로젝트 정보](#프로젝트-정보)
    - [프로젝트 구조](#프로젝트-구조)
        - [Component Structure](#component-structure)
        - [ERD(Entity Relationship Diagram)](#erdentity-relationship-diagram)
        - [Mock-up](#mock-up)
    - [시작 가이드](#시작-가이드)
        - [요구 사항](#요구-사항)
        - [설치 및 실행](#설치-및-실행)
- [프로젝트 결과물](#프로젝트-결과물)
    - [핵심 알고리즘 소개](#핵심-알고리즘-소개)
    - [실제 구현 page 및 각 page 별 기능](#실제-구현-page-및-각-page-별-기능)
        - [로그인 page](#로그인-page)
        - [회원가입 page](#회원가입-page)
        - [나라 선택 page](#나라-선택-page)
        - [영화 추천 page](#영화-추천-page)
        - [영화 디테일 page](#영화-디테일-page)
        - [커뮤니티 page](#커뮤니티-page)
        - [게시글 작성 page](#게시글-작성-page)
        - [게시글 디테일 page](#게시글-디테일-page)
        - [프로필 page](#프로필-page)
- [추후 개발 계획](#추후-개발-계획)
- [프로젝트 규칙](#프로젝트-규칙)
    - [commit message](#commit-message)
    - [omissions message](#omissions-message)
    - [pull request](#pull-request)
- [License](#license)

## 프로젝트 소개

### 1. 프로젝트 설명

**프로젝트 로고**:

![Logo_black](https://github.com/Demopeu/TWM/assets/156268475/47bc562f-f5db-42b7-992d-27c5fdc3f784)

**프로젝트 이름**: TWM(Travel With Movies)

**프로젝트 개요**:
TWM(Travel With Movies)은 사용자가 다양한 나라의 영화를 감상하면서 각 나라의 문화와 감성을 경험 할 수 있도록 알맞은 영화를 추천하는 프로젝트입니다. 

**프로젝트 기간**: 2024.05.08 ~ 2024.05.23

![jara](https://github.com/Demopeu/TWM/assets/156268475/58875e41-ad55-4dce-a6c3-e8805770af3b)

**프로젝트 상세 설명**:
TWM(Travel With Movies)은 자체 개발한 알고리즘을 통해 사용자에게 다양한 나라의 영화를 추천합니다. 이 프로젝트는 단순한 영화 감상을 넘어, 영화를 통해 각 나라의 문화, 역사, 사회적 배경 등을 이해할 수 있는 기회를 제공합니다.

**주요 기능 및 목표:**

- **다양한 영화 추천**: 세계 각국의 영화를 추천하여 사용자에게 다양한 문화적 경험을 선사합니다.

- **문화 이해 증진**: 추천된 영화를 통해 사용자는 각 나라의 고유한 문화와 감성을 배울 수 있습니다.

- **여행 욕구 자극**: 영화를 통해 각국의 아름다운 풍경과 문화를 접하면서, 해당 나라로의 여행을 꿈꾸게 만듭니다.

- **맞춤형 알고리즘**: 사용자의 선호도를 분석하여 개인화된 영화 추천을 제공합니다. 

TWM 프로젝트는 사용자에게 문화적 다양성을 경험하게 하고, 영화라는 매개체를 통해 세계 여러 나라의 문화를 더욱 깊이 이해하고 느낄 수 있도록 하는 것을 목표로 합니다.

---

### 2. 개발 스텍 및 개발 툴

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=node.js&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![Vue.js](https://img.shields.io/badge/Vue.js-4FC08D?style=for-the-badge&logo=vue.js&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Figma](https://img.shields.io/badge/Figma-F24E1E?style=for-the-badge&logo=figma&logoColor=white)
![ERDCloud](https://img.shields.io/badge/ERDCloud-527FFF?style=for-the-badge&logoColor=white)
![draw.io](https://img.shields.io/badge/diagrams.net-F08705?style=for-the-badge&logo=diagrams.net&logoColor=white)
![Jira](https://img.shields.io/badge/Jira-0052CC?style=for-the-badge&logo=jira&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

---

### 3. 팀원 구성 및 역할 분담

![김동현](https://github.com/Demopeu/TWM/assets/156268475/8b1dcea5-ef7d-40fa-8419-c6a2d799444c)

- **팀장**: 김동현

  - 전체 프로젝트 관리 및 팀 조율
  - 주요 기술 결정 및 코드 리뷰
  - 프론트엔드 개발 및 UI/UX 디자인
  - Vue.js 및 Bootstrap을 활용한 인터페이스 구현
  - Figma를 이용한 디자인 작업 및 사용자 경험 개선
  - CSS를 통한 전체적인 페이지 디자인 구현
  - JavaScript를 이용한 동적 페이지 기능 구현

![노재훈](https://github.com/Demopeu/TWM/assets/156268475/b012f620-630c-45ed-9d2c-4177186f3684)

- **팀원**: 노재훈

  - Django 및 백엔드 개발 담당
  - Vue.js와 Django 간의 통신 구현
  - CSS를 통한 프로필 페이지 디자인 구현
  - 영화 추천 알고리즘 개발
  - 데이터베이스 모델 설계 및 최적화
  - API 설계 및 구현
  - 사용자 인증 및 권한 관리 시스템 구축

<div align="right">
  
[목차로](#목차)

</div>

## 프로젝트 정보

### 1. 프로젝트 구조

- **Component Structure**

![ComponetStructure](https://github.com/Demopeu/TWM/assets/156268475/df501d1c-6563-4a02-9f6a-689e6ecf580e)

---

- **ERD(Entity Relationship Diagram)**

![erd](https://github.com/Demopeu/TWM/assets/156268475/38229d0a-5c6d-4433-9cd6-2273f261b07d)

---

- **Mock-up**

![mokeup](https://github.com/Demopeu/TWM/assets/156268475/7238c8ab-3026-4279-a57c-d46a635a497c)

---

### 2. 시작 가이드

#### 요구 사항

- Node.js 12 이상
- Vue.js 3.4.21 이상
- axios 1.6.8 이상
- bootstrap 5.3.3 이상
- pinia 2.1.7 이상
- Python 3.9 이상
- Django 4.2.8 이상
- 기타 필요한 패키지 및 라이브러리

---

#### 설치 및 실행

1. 저장소를 클론합니다:

    ```bash
    git clone https://github.com/Demopeu/TWM.git
    ```

2. 백엔드 폴더로 이동합니다:

    ```bash
    cd ../final_pjt_back/
    ```

3. 가상 환경을 설정하고 필요한 패키지를 설치합니다:

    ```bash
    python -m venv venv
    venv\Scripts\activate  # 윈도우의 경우
    pip install -r requirements.txt
    ```

4. 백엔드 프로젝트 루트에 `.env` 파일을 생성하고 필요한 환경 변수를 설정합니다.:

    ```
    SECRET_KEY=your_secret_key_here
    DATABASE_URL=your_database_url_here
    ```
 
5. 데이터베이스 마이그레이션을 수행합니다:

    ```bash
    python manage.py migrate
    ```

6. 초기 데이터를 로드합니다:

    ```bash
    python manage.py loaddata users.json movies.json articles.json comments.json
    ```

7. 백엔드 서버를 실행합니다:

    ```bash
    python manage.py runserver
    ```

8. 프론트엔드 폴더로 이동합니다:

    ```bash
    cd ../final_pjt_front/
    ```

7. 필요한 패키지를 설치합니다:

    ```bash
    npm install
    ```

8. 프론트엔드 서버를 실행합니다:

    ```bash
    npm run dev
    ```

9. 웹 브라우저에서 `http://localhost:8080`을 열고 애플리케이션을 확인합니다.

<div align="right">
  
[목차로](#목차)

</div>

## 프로젝트 결과물

### 1. 핵심 알고리즘 소개

#### **PPAP 알고리즘(Pre Processing and After Processing Algorithm)**

1. **사용자 입력 및 데이터베이스 조회**:
   - 사용자가 대륙 또는 국가를 선택합니다.
   - 선택한 국가에서 제작된 영화 목록을 데이터베이스에서 가져옵니다.
   - 사용자의 위시리스트를 데이터베이스에서 가져옵니다.

2. **선호 장르 데이터 수집**:
   - 사용자의 위시리스트 및 시청 목록을 기반으로 각 장르의 선호도를 계산합니다.
   - 예를 들어, 사용자가 시청한 영화들의 장르를 기반으로 선호 장르를 추출하고, 해당 장르들의 빈도수를 세어 선호도를 파악합니다.

3. **PPP (Pre Processing Products)**:
   - 가져온 영화 목록을 선호 장르에 따라 필터링합니다.
   - 사용자가 이미 시청한 영화나 위시리스트에 있는 영화는 제외합니다.

4. **장르 가중치 부여**:
   - 사용자의 선호 장르를 바탕으로 영화에 장르 가중치를 부여합니다.
   - 선호 장르의 순위에 따라 가중치를 할당합니다.
   - 예를 들어, 선호 장르가 로맨스 > 액션 > 호러일 때, 로맨스는 가중치 3, 액션은 가중치 2, 호러는 가중치 1을 부여합니다.

5. **APP (After Processing Products)**:
   - 가중치가 부여된 영화 목록을 가중치에 따라 분류합니다.
   - 각 가중치 그룹에 따라 영화를 적절히 분배합니다.
   - 각 가중치 그룹에서는 무작위로 추천될 수 있도록 리스트를 섞어줍니다.

6. **추천 영화 제공**:
   - 최종적으로 사용자에게 영화를 추천합니다.
   - 사용자가 선호하는 장르가 충분히 많다면, 가중치가 높은 그룹부터 영화를 추천합니다.
   - 영화 추천은 각 가중치 그룹에서 설정된 개수만큼 제공됩니다. 단, 총 추천 영화 수는 최대 50개입니다.

### 2. 실제 구현 page 및 각 page 별 기능

- **로그인 page**

![로그인페이지](https://github.com/Demopeu/TWM/assets/156268475/7de41540-16f1-48ad-a122-a419a807107e)
  
    - 로그인 page 아이디와 비밀번호를 입력 후 Login 버튼을 클릭하면 로그인이 됩니다.
    - 만일 미가입 유저라면 Login 아래에 Register! 버튼을 누를 시 회원가입 page로 이동됩니다.
    - 로그인 아이디를 잘못 입력하거나, 비밀번호를 잘못 입력 시 경고창이 뜹니다.

- **회원가입 page**

![회원가입페이지](https://github.com/Demopeu/TWM/assets/156268475/f9026a52-46cd-463b-b2c8-1b9a8fa1c610)

    - 유저 네임과 비밀번호, 비밀번호 확인, 이메일 모두 작성 후 SIGN UP 버튼을 누를 시 회원가입이 완료됩니다.
    - Django의 기초 보안부터, 비밀번호와 비밀번호 확인창이 서로 다를 경우, 이미 있는 아이디인 경우, 이메일 작성 방식이 정상적이지 않을 경우, 혹은 비밀번호와 이메일이 너무 비슷한 경우 등 보안 조건을 만족하지 못하면 경고창이 뜨고 회원가입이 되지 않습니다.
    - 보안 차원에서 회원가입 시 자동으로 로그인이 되지 않고, 다시 로그인 page로 돌아갑니다.

- **나라 선택 page**

![나라선택페이지](https://github.com/Demopeu/TWM/assets/156268475/6c275077-c155-4d7f-bd5a-d2e8b79e7c1b)

    - 로그인이 성공했다면 나라를 선택할 수 있는 page로 이동합니다.
    - 나라 선택 page는 N.America, S.America, Europe, India, China, Korea, Japan 총 7개의 선택지를 제공합니다. 차례대로 북아메리카, 남아메리카, 유럽, 인도, 중국, 한국, 일본입니다. 나라가 아닌 대륙의 경우 해당 대륙의 대표적인 나라 3~5가지가 포함되어 있습니다.
    - 원하는 선택지를 고를 경우 사용자는 선택한 나라가 배경인, 혹은 선택한 나라가 제작한 영화들을 추천받는 page로 이동합니다.
    - 만약 N.America를 선택했다면 캐나다, 미국, 멕시코 세 나라의 영화 모두 추천됩니다.

- **영화 추천 page**

![영화추천페이지](https://github.com/Demopeu/TWM/assets/156268475/9c040084-8335-4cb3-b55f-0d3b7020e881)

    - 영화 추천 알고리즘이 적용된 영화 추천 page입니다. 사용자의 위시리스트, 본 목록, 혹은 선호하는 장르에 따라서 가중치가 결정되고, 그에 따른 무작위 영화가 최대 50개 추천됩니다.
    - 해당 page에서는 나라를 다시 재선택하기 위하여 돌아갈 수도 있고, 게시글을 쓸 수 있는 커뮤니티 page로 이동이 가능합니다.
    - 원하는 영화를 선택 시 영화 디테일 page로 이동합니다.

- **영화 디테일 page**

![영화디테일페이지](https://github.com/Demopeu/TWM/assets/156268475/66738d14-56eb-45b8-bc1c-25b7cd401456)
  
    - 영화 디테일 page에서는 영화 포스터, 제목, 개봉일, 관람등급 등등 다양한 정보를 얻을 수 있습니다.
    - 버튼 소개
        - 예고편 보러가기 버튼 : 누를 시 영화 공식 트레일러 영상이 있는 유튜브 새 창이 열립니다.
        - 위시리스트 : 위시리스트 버튼을 누를 시 위시리스트에 담깁니다. 만약 이미 위시리스트 항목에 해당 영화가 있다면, 위시리스트에 이미 담겼다는 경고창이 출력됩니다.
        - 게시판 이동 : 게시글을 쓸 수 있는 커뮤니티 page로 이동합니다.
        - 뒤로 가기 : 다양한 영화를 추천 받는 전 page로 돌아갑니다.

- **커뮤니티 page**

![게시판전체](https://github.com/Demopeu/TWM/assets/156268475/626582b7-86cf-44d8-88d3-0f1ec4593233)

![게시판전체-하단](https://github.com/Demopeu/TWM/assets/156268475/998e264f-aa13-4e49-9983-a6d9a0cb8fef)

    - 유저들이 작성한 글을 볼 수 있고, 글도 쓸 수 있는 커뮤니티 page입니다. 게시글 목록 상단에 태그를 선택할 수 있으며, Global은 전체 글 page, 각 나라 이름을 클릭하면 해당 나라에 소속된 영화 리뷰들만 볼 수 있습니다.
    - 하단의 글쓰기 버튼을 통해 직접 게시글을 작성할 수 있습니다.

- **게시글 작성 page**

![글쓰기 페이지](https://github.com/Demopeu/TWM/assets/156268475/d59bcd88-5f33-4bd5-9412-2c1150398f2d)

    - 본 사이트에서 게시글은 리뷰만을 허락하고 있습니다. 사이트에서 추천 받은 영화를 본 후 그에 해당하는 리뷰 제목, 영화가 소속된 국가, 리뷰 내용을 작성할 수 있습니다. 모두 작성 후 하단의 글쓰기 버튼을 클릭할 시 게시글이 작성됩니다.
    - 만일 어떠한 요소라도 누락됐을 경우 경고창이 출력됩니다.
    - 좌측의 빈 공간에서는 광고가 삽입될 수 있습니다.

- **게시글 디테일 page**

![게시판 상세 페이지](https://github.com/Demopeu/TWM/assets/156268475/456dcc0b-1162-4d42-b8e4-898bb9b9f55b)

    - 커뮤니티 page에서 다른 사람들이 작성한 리뷰를 클릭하면 게시글 디테일 page로 이동합니다.
    - 해당 page에서는 좋아요 버튼을 누를 시 게시글의 좋아요 개수가 올라갑니다. 단 좋아요를 한 번 더 누르면 좋아요가 취소됩니다.
    - 하단의 입력창에 글을 작성 후 제출을 눌러서 댓글을 작성할 수 있습니다.
    - 디테일 page에서 작성자 아이디를 클릭 시 작성자의 프로필 page로 이동이 가능합니다.

- **프로필 page**

![프로펠 페이지](https://github.com/Demopeu/TWM/assets/156268475/bec6c343-1066-4da1-aa28-0fe15156466f)

![프로펠 페이지-하단](https://github.com/Demopeu/TWM/assets/156268475/3fdb90df-323a-48a6-b9d6-ac9b14b4fb37)

    - 회원의 이메일, 최근 접속, 인증서, 위시리스트 영화 목록, 본 목록 등을 확인할 수 있는 page입니다.
    - 자신의 프로필 page의 경우 회원 탈퇴 버튼이 자신의 아이디 옆에 나타납니다. 회원 탈퇴 버튼을 클릭 시 되묻는 modal창이 2번에 걸쳐서 나오고, 모두 확인 버튼을 누르면 회원 탈퇴가 완료됩니다.
    - 해당 프로필 페이지 유저가 작성한 리뷰가 좋아요를 많이 받으면 관리자의 검수를 통해 인증서를 받을 수 있고, 인증서들은 프로필 page의 인증서 항목에 표시됩니다. 인증서 항목에서 받은 인증서들 위에 마우스를 올릴 경우 강조 표시와 함께 이모티콘이 보여집니다.
    - 위시리스트 영화 목록은 사용자가 영화 디테일 page에서 담은 위시리스트들이 표시됩니다. 위시리스트 영화 목록에 있는 영화를 클릭하면 본 영화로 옮겨집니다.

<div align="right">
  
[목차로](#목차)

</div>

## 추후 개발 계획

- **비밀번호 재설정 기능 추가**: 사용자가 비밀번호를 잊어버릴 경우, 비밀번호 재설정 기능을 추가하여 비밀번호를 재설정할 수 있도록 기능 추가 예정

- **좋아요 순으로 나열 기능 추가**: 영화 목록을 좋아요 개수 순으로 게시글을 나열하는 기능 추가 예정

- **검색 기능 추가**: 영화 목록을 검색할 수 있는 기능 추가 예정

- **나라 확대 및 영화 데이터 추가**: 다양한 나라의 영화를 추가하여 나라의 범위를 확대하고, 더 많은 영화 데이터를 추가하여 사용자에게 다양한 선택지를 제공 예정

- **UI/UX 개선**: 사용자 경험을 고려하여 인터페이스로 개선, 애플리케이션을 더욱 효과적으로 활용할 수 있도록 애플리케이션 디자인을 개선 예정.

<div align="right">
  
[목차로](#목차)

</div>

## 프로젝트 규칙

### 1. commit message

-**Commit message 구조 :**

```
type:title
ex. git commit -m "docs: README 내용 수정"
```

-**Commit message type 종류 :**

![type](https://github.com/Demopeu/TWM/assets/156268475/c31f78f6-67bb-46f2-a830-58590515a02e)

### 2. ommisions message

-**ommisions message 작성법 :**

1. **대주제 선택(ex. front, back)**

2. **직접적으로 문제가 있거나, 누락된 부분이 있는 페이지 작성**

    ```
    1. Login.vue
    - username, password 이모티콘 누락
    ```

    - 구동이 안될 정도의 큰 문제가 있을 경우, 대주제 바로 아래에 "##"를 이용하여 즉시 작성후 **!important**를 어미에 작성

    - 구동은 되나, 전체에 걸쳐서 오류가 있을 경우, 대주제 바로 아래에 "##"를 이용하여 즉시 작성

3. **"##" 에 작성한 내용은 merge 설명에 기입 후, MM혹은 카카오톡을 이용하여 즉시 알림**

4. **완료되거나 해결 된 이슈는 삭제하지 말고 취소선을 그은 이후, 대주제 completed로 이동**

### 3. pull request

1. **로컬에서 변경 사항 커밋**

    - 새로운 기능이나 수정한 내용을 로컬에서 커밋, 이 때, 각자의 branch 이용

    ```bash
    git add .
    git commit -m "docs: README 내용 수정"
    ```

2. **원격 저장소로 브랜치 push**

    - 로컬에서 변경한 내용을 원격 저장소로 push

    ```bash
    git push branchname
    ```

3. **Pull Request 생성**

    - GitHub 또는 GitLab 등의 원격 저장소에서 Pull Request를 생성
    - Pull Request에는 작업한 내용을 간결하게 요약하여 작성

4. **팀장의 승인 대기**

    - Pull Request를 작성한 후, 팀장에게 리뷰를 요청
    - 팀장은 변경 내용을 확인하고 필요한 경우 코멘트를 남기거나 승인을 진행

5. **Merge 충돌 없을 경우**

    - 변경 내용에 충돌이 없는 경우, 팀장이 승인하고 바로 Merge

6. **Merge 충돌 발생 시 중재**

    - 변경 내용에 충돌이 발생한 경우, 팀장이 충돌을 해결하고 Merge를 진행
    - 충돌을 해결한 후, 다시 승인을 요청하거나 직접 Merge

8. **Pull Request 완료**

    - Pull Request가 완료되면 해당 작업은 원격 저장소의 메인 브랜치에 반영

<div align="right">
  
[목차로](#목차)

</div>

## License

# 영화 추천 프로젝트 - TWM(Travel With Movies)

## 프로젝트 소개

### 1. 프로젝트 설명

**프로젝트 이름**: TWM(Travel With Movies)

**프로젝트 소개**:
TWM(Travel With Movies)은 사용자가 다양한 나라의 영화를 감상하면서 각 나라의 문화와 감성을 경험 할 수 있도록 알맞은 영화를 추천하는 프로젝트입니다. 

**프로젝트 기간**: 2024.05.16 ~ 2024.05.23

**프로젝트 설명**:
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

- **팀장**: 김동현

  - 전체 프로젝트 관리 및 팀 조율
  - 주요 기술 결정 및 코드 리뷰
  - 프론트엔드 개발 및 UI/UX 디자인
  - Vue.js 및 Bootstrap을 활용한 인터페이스 구현
  - Figma를 이용한 디자인 작업 및 사용자 경험 개선
  - CSS를 통한 전체적인 페이지 디자인 구현
  - JavaScript를 이용한 동적 페이지 기능 구현

- **팀원**: 노재훈

  - Django 및 백엔드 개발 담당
  - Vue.js와 Django 간의 통신 구현
  - CSS를 통한 프로필 페이지 디자인 구현
  - 영화 추천 알고리즘 개발
  - 데이터베이스 모델 설계 및 최적화
  - API 설계 및 구현
  - 사용자 인증 및 권한 관리 시스템 구축

  ---

## 프로젝트 정보

### 1. 프로젝트 구조

- **Component Structure**

![erd](https://github.com/Demopeu/TWM/assets/156268475/38229d0a-5c6d-4433-9cd6-2273f261b07d)

---

- **ERD(Entity Relationship Diagram)**

![erd](https://github.com/Demopeu/TWM/assets/156268475/38229d0a-5c6d-4433-9cd6-2273f261b07d)

---

- **Mock-up**

![erd](https://github.com/Demopeu/TWM/assets/156268475/38229d0a-5c6d-4433-9cd6-2273f261b07d)

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

---

## 프로젝트 결과물

### 1. 핵심 알고리즘 소개

### 2. 실제 구현 페이지 및 각 페이지 별 기능

## 추후 개발 계획

- **비밀번호 재설정 기능 추가**: 사용자가 비밀번호를 잊어버릴 경우, 비밀번호 재설정 기능을 추가하여 비밀번호를 재설정할 수 있도록 기능 추가 예정

- **좋아요 순으로 나열 기능 추가**: 영화 목록을 좋아요 갯수 순으로 게시글을 나열하는 기능 추가 예정

- **검색 기능 추가**: 영화 목록을 검색할 수 있는 기능 추가 예정

- **나라 확대 및 영화 데이터 추가**: 다양한 나라의 영화를 추가하여 나라의 범위를 확대하고, 더 많은 영화 데이터를 추가하여 사용자에게 다양한 선택지를 제공 예정

- **UI/UX 개선**: 사용자 경험을 고려하여 인터페이스로 개선, 애플리케이션을 더욱 효과적으로 활용할 수 있도록 애플리케이션 디자인을 개선 예정.

## 프로젝트 규칙

### 1. commit message

### 2. ommisions message

### 3. pull request

## License
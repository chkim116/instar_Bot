# instar bot ver 1.1

-   헤드리스를 지원합니다.

## 사용법

```
git clone https://github.com/chkim116/instar_Bot.git
```

instarbot.py 실행.
<br />

사용하는 크롬의 브라우저 버전 확인 및 드라이버 다운 필수.
현재 드라이버는 93버전
[크롬 드라이버 설치는 이곳에서](https://chromedriver.chromium.org/downloads)

<br />

---

## 기본 설정

1. id.txt에 아이디 적기.
2. pw.txt에 비번 적기.
3. tag.txt에 해시태그 적기. (규칙 --> " , " 로 해시태그 구분, 띄어쓰기는 없어야함.)

<br />

### GUI 툴에서의 설정

<br />

-   기본 세팅으로 입력이 되있다. 모두 수정이 가능하니 커스텀화 하길.

<br />

0. 아이디, 비밀번호는 기본적으로 id, pw 텍스트 파일에 입력된 걸 따라감.

<br />

1. 태그당 좋아요 개수

    - 기본은 10개
    - 태그 당 몇 개의 좋아요를 누를지 정함.

<br />

2. 좋아요 제한 개수

    - 기본은 200개
    - 총 좋아요 개수를 몇 개까지 할지 정함.

<br />

3. 딜레이 설정

    - 기본은 80초
    - 좋아요를 누른 뒤 있을 고정 딜레이 설정

<br />

4. 랜덤 딜레이 설정

    - 기본은 1-30초
    - 위에는 최소, 아래는 최대 값 지정

<br />

5. 시행할 태그 목록 설정
    - tag.txt에 있는 텍스트들을 따라감.
    - 수정할 시 tag.txt를 수정하는 걸 추천

## 추후 업뎃 예정 사항

-   팔로우 검열
-   댓글 기능 or 팔로우 기능
-   자기 팔로워 좋아요

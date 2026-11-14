# Views — 표현과 조판

원고와 표현을 분리합니다. 문학적 내용은 `contents/<작품명>/publish/`에, 독서 화면의 디자인과 동작은 `views/page_style/`에 둡니다.

- `page_style/book.css`: 사륙판(128 × 188mm) 책 모양, 본문 크기, 행간, 여백, 문단 간격, 반전 버튼
- `page_style/reader.js`: 본문 페이지 분할, 화면 확대, 반전 버튼 동작
- `page_style/story.css`: 집필 중 원고의 연속형 독서 화면
- `contents/*/publish/*.html`: 작품 내용과 최소한의 HTML 구조. CSS/JS는 상대경로로 참조
- 루트 `index.html`: 게시판 형태의 작품 목록

## 디자인 바꾸기

책의 외형은 `page_style/book.css`만 수정하면 됩니다. 페이지 전환이나 인터랙션은 `page_style/reader.js`를 수정합니다. MD 원고와 HTML 속 본문은 디자인 변경 때 건드리지 않습니다.

GitHub Pages에서 사용하므로 모든 경로는 각 HTML 파일 기준의 상대경로입니다.

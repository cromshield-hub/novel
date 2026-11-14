# novel

개인 창작 소설 원고와 집필 자료를 관리하는 저장소입니다.

## 저장소 구조

```text
index.html                       # GitHub Pages 작품 목록
contents/
  불치병/
    publish/                    # 독자 공개용 MD와 HTML
    recipe/                     # 설정, 메모, 창작 재료
  morning coffee/
    publish/
    recipe/
  future_train/
    publish/                    # 원고와 DOCX
    recipe/                     # 세계관, 집필 지침, 변환 스크립트
views/                          # 공통 화면과 조판 규칙
```

`publish`는 독자가 읽을 작품의 결과물, `recipe`는 집필 과정에서 사용하는 자료입니다. 원고 내용과 창작 자료를 구분해 관리합니다.

## 작품

- [불치병](contents/불치병/publish/불치병.md) — [46판 독서용 HTML](contents/불치병/publish/불치병.html)
- [morning coffee](contents/morning%20coffee/publish/manuscript.md) — [초고 HTML](contents/morning%20coffee/publish/manuscript.html), 집필 중
- [미래로 가는 기차](contents/future_train/README.md) — [초고 HTML](contents/future_train/publish/manuscript_rewrite.html), 시간의 흐름이 서로 다른 우주 테라리움들과 어머니를 살리려는 정원사의 이야기.

## Codex에서 이어 쓰기

1. 저장소를 Codex 작업 환경에 연결합니다.
2. 먼저 이 저장소의 `AGENTS.md`와 `contents/future_train/AGENTS.md`를 확인합니다.
3. `contents/future_train/recipe/characters_timeline.md`와 `contents/future_train/recipe/worldbuilding.md`에서 최신 설계와 미정 사항을 확인합니다.
4. 본문 수정이 요청되면 `contents/future_train/publish/manuscript_rewrite.md`를 수정하고 `python3 contents/future_train/recipe/build_story_doc.py`로 Word 파일을 갱신합니다.

원고와 부록은 창작 중인 자료입니다. 집필자가 확정한 최신 결정을 유지하며, 새로운 제안은 확정 사항과 구별해서 기록합니다.

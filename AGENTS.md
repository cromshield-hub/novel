# Codex 집필 지침 — novel 저장소

이 저장소는 코드보다 **소설 원고의 일관성과 문학적 완성도**를 우선합니다.

## 작업 시작

1. `future_train/AGENTS.md`를 읽고, 해당 작품의 설정과 작업 규칙을 따르세요.
2. `future_train/manuscript_rewrite.md`가 본문 및 부록의 **원본(source of truth)**입니다.
3. `future_train/characters_timeline.md`와 `future_train/worldbuilding.md`는 설정 검토용 문서입니다. 서로 불일치하면 본문을 임의로 고치지 말고 사용자에게 알려주세요.

## 편집 규칙

- 독자에게 노출되는 문장은 한국어로 작성합니다.
- 사용자가 요청한 범위에서 수정하고 다른 장면이나 설정을 불필요하게 재해석하지 마세요.
- 사실적 오류, 시간·나이 모순, 인물의 동기·행동 충돌을 점검하세요.
- `future_train/build_story_doc.py`는 Markdown에서 DOCX를 만듭니다. 원고를 바꾸면 DOCX도 함께 갱신하세요.
- 부록의 쿠키 장면은 본편과 독립적으로 취급하고, 요청 없이는 본편 결말에 섞지 마세요.

이 지침보다 해당 작품 폴더의 `AGENTS.md`가 더 구체적이면 폴더 지침을 따릅니다.

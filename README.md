# 자동화 도구 모음 (https://caaaaat0408.github.io/)

PM 업무 자동화 도구들을 한 페이지에서 열고, 도구마다 **지금 버전**과 **버전별 수정사항**을 보는 페이지입니다.

- 판관비 예산안 자동작성 · 지출계획서 자동작성 · 사업관리비 실적계획 자동작성 (저장소 pangwanbi-budget)
- 분양개요 자동작성 (bunyang-overview) · 계약서 자동작성 (contract-builder) · 지식산업센터 시세현황 업데이터 (KIC-monthly-report)

## 처음 한 번: GitHub 에 올리기
1. GitHub(CAAAAAT0408 계정)에서 **New repository** → 이름 `CAAAAAT0408.github.io` (Public) 로 빈 저장소를 만든다.
   (이 이름이어야 https://caaaaat0408.github.io/ 로 열린다. README·.gitignore 는 만들지 않는다.)
2. 이 폴더의 `깃허브 올리기.bat` 을 실행한다. 1~2분 뒤 https://caaaaat0408.github.io/ 가 열린다.
3. Pages 가 자동으로 켜지지 않으면 저장소 Settings → Pages → Branch `main` / `(root)` 로 지정한다.

## 버전과 수정 이력
- 각 도구 저장소의 `version.json`(페이지별 `version`·`changelog`)을 `raw.githubusercontent.com` 에서 읽어 보여준다.
  → 도구를 고친 뒤 그 저장소에서 `python bump_version.py <페이지키> "수정 내용"` 을 돌리고 push 하면 이 페이지에 반영된다.
- 이 페이지 자체도 같은 규칙(최초 1.0, 수정 1회 +0.1): `python bump_version.py hub "수정 내용"`.

## 로컬에서 열기
`자동화 페이지 열기.bat` — 인터넷이 되면 버전·이력도 보이고, PC 판 링크는 이 PC 의 서버가 켜져 있을 때 열린다.

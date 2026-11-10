# -*- coding: utf-8 -*-
"""각 도구 저장소의 version.json 을 읽어 자동화 모음 페이지(index.html)에 버전·업데이트 이력을 넣는다.
   도구 버전을 올린 뒤:  python update_hub.py   → 바뀐 index.html 을 깃허브 올리기.bat 으로 올리면 모음 페이지에 반영된다.
   (페이지는 인터넷이 되면 올라가 있는 version.json 도 읽어 더 새 버전이면 그것을 보여준다)"""
import io
import json
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.dirname(HERE)                      # ...\1. 본사업무\AI자동화 (도구 저장소들이 같은 층에 있다)
SRC = {
    "budget": os.path.join(BASE, "☆ 예산안 자동작성", "version.json"),
    "jichul": os.path.join(BASE, "☆ 예산안 자동작성", "version.json"),
    "siljeok": os.path.join(BASE, "☆ 예산안 자동작성", "version.json"),
    "overview": os.path.join(BASE, "☆ 분양개요 자동작성", "version.json"),
    "contract": os.path.join(BASE, "☆ 공급계약서 자동작성", "version.json"),
    # "notice": os.path.join(BASE, "☆ 입주자모집공고 자동작성", "version.json"),   # 완성 전 — 모음 페이지에서 뺌(2026-11-06), 완성되면 되살림
    "hub": os.path.join(HERE, "version.json"),
}
pages = {}
for key, path in SRC.items():
    try:
        p = json.load(io.open(path, encoding="utf-8"))["pages"][key]
        pages[key] = dict(name=p.get("name"), version=p.get("version"), changelog=p.get("changelog") or [], history=p.get("history") or [])
        print(f"  {key:9s} v{p.get('version')}  {p.get('name')}")
    except Exception as e:   # noqa: BLE001
        print(f"  {key:9s} 읽지 못함: {e}")
html_path = os.path.join(HERE, "index.html")
s = io.open(html_path, encoding="utf-8", newline="").read()
blob = json.dumps({"pages": pages}, ensure_ascii=False)
s2, n = re.subn(r'(<script id="versions" type="application/json">).*?(</script>)', lambda m: m.group(1) + blob + m.group(2), s, count=1, flags=re.S)
if n != 1:
    sys.exit("index.html 에 버전 자리(<script id=\"versions\">)가 없습니다.")
io.open(html_path, "w", encoding="utf-8", newline="").write(s2)
print("index.html 갱신:", len(pages), "개 페이지")

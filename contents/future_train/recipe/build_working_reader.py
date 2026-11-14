#!/usr/bin/env python3
"""Render the independent working manuscript with the shared book design.

Run from any directory: python3 contents/future_train/recipe/build_working_reader.py
Requires pandoc. Never changes the first, second, or current manuscript.
"""

from pathlib import Path
import shutil
import subprocess


def main():
    story = Path(__file__).resolve().parents[1]
    root = story.parents[1]
    manuscript = story / "publish" / "working.md"
    output = manuscript.with_suffix(".html")
    if not manuscript.is_file():
        raise SystemExit(f"Working 원고가 없습니다: {manuscript}")
    pandoc = shutil.which("pandoc")
    if not pandoc:
        raise SystemExit("HTML 변환을 위해 pandoc이 필요합니다.")
    variables = {
        "root": "../../..",
        "version": "Working · 진행형 초고",
        "choicehref": "./index.html",
        "firsthref": "./versions/1차.html",
        "secondhref": "./versions/2차.html",
        "currenthref": "./manuscript_rewrite.html",
        "workinghref": "./working.html",
        "working": "true",
    }
    command = [pandoc, str(manuscript), "--from=markdown", "--to=html5",
               "--metadata", "title=미래로 가는 기차 · Working",
               "--standalone", "--template", str(root / "views/page_style/version-reader.html"),
               "--output", str(output)]
    for key, value in variables.items():
        command.extend(["--variable", f"{key}={value}"])
    subprocess.run(command, check=True)
    print(f"독서용 HTML 생성: {output}")


if __name__ == "__main__":
    main()

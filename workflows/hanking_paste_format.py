#!/usr/bin/env python3

"""
이 스크립트는 한글킹제임스성경 앱에서 복사한 텍스트 형식을 정리해주는 스크립트입니다.
- 입력: 한글킹제임스성경 앱에서 복사한 텍스트
- 출력: 성경 구절 번호를 앞에 붙인 텍스트 & 노션에 붙여넣기 하기 좋은 형식


Example
-------
Input:
○ 그러자 왕이 보내어 유다와 예루살렘의 모든 장로들을 함께 모으고
왕과 유다의 모든 사람과 예루살렘의 거민과 제사장들과 레위인들과 크고 작은 모든  백성이 주의 전으로 올라갔으며, 그가 주의 전에서 발견한 언약책의 모든 말씀을 그들의 귀에 읽어 주니라.
왕이 자기 자리에 서서, 주를 따라 행하며 그의 마음을 다하고 그의 혼을 다하여 그분의 계명들과 증거들과 규례들을 지키고 이 책에 기록된 언약의 말씀들을 이행하기로  주 앞에서 언약을 세웠으며
예루살렘과 베냐민에 참여한 모든 자들로 이를 지지하도록 하니 예루살렘의 거민이 하나님, 즉 그들 조상의 하나님의 언약에 따라 행하였더라.
요시야가 이스라엘 자손에게 속한 모든 나라에서 모든 가증한 것을 제거하고, 이스라 엘에 참여한 모든 사람들로 섬기게 하였으니 즉 주 그들의 하나님을 섬기게 하니라.  그의 평생 동안 백성들이 주 그들 조상의 하나님을 따르는 데서 떠나지 아니하였더라.
역대기하 34:29~33

Output:
- 역대기하 34:29-33
    
    *29 ○ 그러자 왕이 보내어 유다와 예루살렘의 모든 장로들을 함께 모으고
    30 왕과 유다의 모든 사람과 예루살렘의 거민과 제사장들과 레위인들과 크고 작은 모든  백성이 주의 전으로 올라갔으며, 그가 주의 전에서 발견한 언약책의 모든 말씀을 그들의 귀에 읽어 주니라.
    31 왕이 자기 자리에 서서, 주를 따라 행하며 그의 마음을 다하고 그의 혼을 다하여 그분의 계명들과 증거들과 규례들을 지키고 이 책에 기록된 언약의 말씀들을 이행하기로  주 앞에서 언약을 세웠으며
    32 예루살렘과 베냐민에 참여한 모든 자들로 이를 지지하도록 하니 예루살렘의 거민이 하나님, 즉 그들 조상의 하나님의 언약에 따라 행하였더라.
    33 요시야가 이스라엘 자손에게 속한 모든 나라에서 모든 가증한 것을 제거하고, 이스라 엘에 참여한 모든 사람들로 섬기게 하였으니 즉 주 그들의 하나님을 섬기게 하니라.  그의 평생 동안 백성들이 주 그들 조상의 하나님을 따르는 데서 떠나지 아니하였더라.*


Usage
-----
1. Use in terminal with input string
>>> python workflows/hanking_paste_format.py $'○ 그러자 왕이 보내어 유다와 예루살렘의 모든 장로들을 함께 모으고
왕과 유다의 모든 사람과 예루살렘의 거민과 제사장들과 레위인들과 크고 작은 모든  백성이 주의 전으로 올라갔으며, 그가 주의 전에서 발견한 언약책의 모든 말씀을 그들의 귀에 읽어 주니라.
왕이 자기 자리에 서서, 주를 따라 행하며 그의 마음을 다하고 그의 혼을 다하여 그분의 계명들과 증거들과 규례들을 지키고 이 책에 기록된 언약의 말씀들을 이행하기로  주 앞에서 언약을 세웠으며
예루살렘과 베냐민에 참여한 모든 자들로 이를 지지하도록 하니 예루살렘의 거민이 하나님, 즉 그들 조상의 하나님의 언약에 따라 행하였더라.
요시야가 이스라엘 자손에게 속한 모든 나라에서 모든 가증한 것을 제거하고, 이스라 엘에 참여한 모든 사람들로 섬기게 하였으니 즉 주 그들의 하나님을 섬기게 하니라.  그의 평생 동안 백성들이 주 그들 조상의 하나님을 따르는 데서 떠나지 아니하였더라.
역대기하 34:29~33'

2. Use in terminal with clipboard
  - Copy the input string to clipboard
  - Run the script without any arguments
    >>> python workflows/hanking_paste_format.py
  - The formatted string will be copied to clipboard
"""

import argparse
import re
import subprocess


def parse_input():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", nargs="?", default=None, help="Input string to print")
    args = parser.parse_args()
    return args.input


def get_input_from_clipboard():
    process = subprocess.Popen(
        "pbpaste",
        env={"LANG": "en_US.UTF-8"},
        stdout=subprocess.PIPE,
    )
    output, _ = process.communicate()
    return output.decode("utf-8")


def print_input(input_string):
    lines = input_string.split("\n")
    verse_coordinate = lines.pop()
    match = re.search(r":(\d+)~?(\d+)?", verse_coordinate)
    start = int(match.group(1))
    end = int(match.group(2)) if match.group(2) else start

    # Add tab space, verse number, and italic style
    tab = " " * 4
    for i, n in enumerate(range(start, end + 1)):
        lines[i] = (
            f"{tab}{'*' if n == start else ''}{n} "
            f"{lines[i]}{'*' if n == end else ''}"
        )

    # Bullet point
    verse_coordinate = f"- {verse_coordinate.replace('~', '-')}"

    formatted_input = "\n".join([verse_coordinate, tab] + lines)

    copy_to_clipboard(formatted_input)


def copy_to_clipboard(text):
    process = subprocess.Popen(
        "pbcopy",
        env={"LANG": "en_US.UTF-8"},
        stdin=subprocess.PIPE,
    )
    process.communicate(input=text.encode("utf-8"))


if __name__ == "__main__":
    input_string = parse_input() or get_input_from_clipboard()
    print_input(input_string)

# Tools to Make Life More Beneficial and Enriching

이 레포지토리는 삶을 더 유익하고 풍요롭게 만드는 도구들을 제공합니다. 여기에는 텍스트 포맷팅과 PDF 파일 잠금 해제를 도와주는 스크립트가 포함되어 있습니다.

## hanking_paste_format.py

이 스크립트는 한글 킹제임스 성경 앱에서 복사한 텍스트를 markdown 형식으로 붙여넣기 위해 사용됩니다.

### 사용법

1. Use in terminal with input string
    ```bash
    >>> python workflows/hanking_paste_format.py $'○ 그러자 왕이 보내어 유다와 예루살렘의 모든 장로들을 함께 모으고
    왕과 유다의 모든 사람과 예루살렘의 거민과 제사장들과 레위인들과 크고 작은 모든  백성이 주의 전으로 올라갔으며, 그가 주의 전에서 발견한 언약책의 모든 말씀을 그들의 귀에 읽어 주니라.
    왕이 자기 자리에 서서, 주를 따라 행하며 그의 마음을 다하고 그의 혼을 다하여 그분의 계명들과 증거들과 규례들을 지키고 이 책에 기록된 언약의 말씀들을 이행하기로  주 앞에서 언약을 세웠으며
    예루살렘과 베냐민에 참여한 모든 자들로 이를 지지하도록 하니 예루살렘의 거민이 하나님, 즉 그들 조상의 하나님의 언약에 따라 행하였더라.
    요시야가 이스라엘 자손에게 속한 모든 나라에서 모든 가증한 것을 제거하고, 이스라 엘에 참여한 모든 사람들로 섬기게 하였으니 즉 주 그들의 하나님을 섬기게 하니라.  그의 평생 동안 백성들이 주 그들 조상의 하나님을 따르는 데서 떠나지 아니하였더라.
    역대기하 34:29~33'
    ```

2. Use in terminal with clipboard
  - Copy the input string to clipboard
  - Run the script without any arguments
    `>>> python workflows/hanking_paste_format.py`
  - The formatted string will be copied to clipboard

## unlock_pdf.py

이 스크립트는 잠긴 PDF 파일의 잠금을 해제하는 데 사용됩니다.

### 사용법

```bash
> poetry install
> python unlock_pdf.py /path/to/locked.pdf password
```
# Opensource_team6

## 1. What it does

- 입력 이미지를 불러와 처리 가능한 이미지 데이터 객체로 변환합니다.
- 색각 이상 유형(`protanopia`, `deuteranopia`, `tritanopia`)에 따른 시각 환경을 시뮬레이션합니다.
- 구분하기 어려운 색상 영역을 인지 가능한 색 영역으로 재배치하고 원본 이미지의 디테일을 보존합니다.
- 시뮬레이션 및 색상 보정이 완료된 이미지를 결과 파일로 저장합니다.

## 2. Installation

### Install from TestPyPI

You can install the package from TestPyPI for testing purposes.

```bash
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ seeallcolors
```

### Install from PyPI

After the package is officially released, you can install it from PyPI.

```bash
pip install seeallcolors
```

## 3. Quick Start

SeeAllColors allows users to simulate how an image appears to people with different types of color vision deficiency.

### Example

Prepare an image file named `sample.png` in your working directory.

```python
from seeallcolors.core import load_image, simulate_colorblindness

image = load_image("sample.png")
result = simulate_colorblindness(image, "protanopia")
```

### Input
- An image file (JPG or PNG).
- A color vision deficiency type: `protanopia`, `deuteranopia`, or `tritanopia`.

### Output
- Image data processed to simulate the selected type of color vision deficiency.

## 4. Dependencies

Python 3.10 이상이 필요합니다. 아래 패키지는 pip로 설치할 때 자동으로 함께 설치됩니다.

| 패키지 | import 이름 | 버전 | 라이선스 | 용도 |
|---|---|---|---|---|
| [NumPy](https://pypi.org/project/numpy/) | `numpy` | >=1.26 | BSD-3-Clause | 픽셀 배열 처리 및 색 공간 계산 |
| [Pillow](https://pypi.org/project/Pillow/) | `PIL` | >=10 | MIT-CMU | JPG / PNG 이미지 읽기 및 저장 |

표준 라이브러리 모듈은 목록에 포함하지 않았습니다.
모든 의존성은 permissive 라이선스로, 이 프로젝트의 MIT 라이선스와 호환됩니다.

## 5. Tests

TODO (이후 수업에서 작성)

## 6. Documentation

전체 문서는 `src/seeallcolors/core.py`의 docstring을 바탕으로 MkDocs로 생성됩니다.

- 문서 사이트: https://anhayeon.github.io/Opensource_team6/
- API 레퍼런스: https://anhayeon.github.io/Opensource_team6/api/
- 프로젝트 제안서: [docs/proposal.md](docs/proposal.md)
- 팀 규칙: [docs/team-rules.md](docs/team-rules.md)

`main` 브랜치에 push될 때마다 GitHub Actions가 문서 사이트를 자동으로 다시 빌드하고 배포합니다.

## 7. Release

TODO (이후 수업에서 작성)

## 8. Team

SeeAllColors는 색각 이상 사용자가 이미지의 색상을 더 쉽게 구별할 수 있도록 돕는 Team 6 프로젝트입니다.

### Team Members

- 신율 ([shin-yul](https://github.com/shin-yul))
- 안하연 ([anhayeon](https://github.com/anhayeon))
- 김진서 ([kimjs1127](https://github.com/kimjs1127))
- 안세로 ([sero-an](https://github.com/sero-an))
- 이미혜 ([Leemihye07](https://github.com/Leemihye07))

### Team Rules

프로젝트의 협업 및 PR 규칙은 [Team Rules](docs/team-rules.md)를 참고

### AI Use

- README의 Team 및 License 항목 작성과 Markdown 형식을 보조받았습니다.
- 팀 규칙과 LICENSE 파일을 직접 확인했습니다.

## 9. License

This project is licensed under the MIT License.

Copyright (c) 2026 Opensource_team6

See [LICENSE](LICENSE) for the full license text.

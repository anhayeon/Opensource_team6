def simulate_colorblindness(image_data: object, colorblind_type: str) -> object:
    """선택한 색각 이상 유형(적색맹, 녹색맹, 청색맹)에서 어떻게 보이는지 시뮬레이션합니다.

    Args:
        image_data (object): 원본 이미지 데이터 객체.
        colorblind_type (str): 색각 이상 종류 ('protanopia', 'deuteranopia','tritanopia').

    Returns:
        object: 선택한 색각 이상 시각조건으로 렌더링된 시뮬레이션 이미지 데이터.

    Raises:
        ValueError: 올바르지 않은 색각이상 종류가 입력되었을 때 발생.

    Examples:
        >>> sim_img = simulate_colorblindness(img, "protanopia")
    """
    raise NotImplementedError


def load_image(image_path: str):
    """입력 이미지 파일(JPG, PNG)을 읽어 색상 처리용 배열 데이터로 변환합니다.

    Args:
        image_path (str): 읽어올 이미지 파일의 경로.

    Returns:
        object: RGB 색상 정보가 포함된 이미지 데이터 객체 (NumPy Array 등).

    Raises:
        FileNotFoundError: 지정한 경로에 이미지 파일이 없을 때 발생.
        ValueError: 지원하지 않는 파일 형식(JPG, PNG 외)일 때 발생.

    Examples:
        >>> img = load_image("sample.png")
        >>> img is not None
        True
    """
    raise NotImplementedError
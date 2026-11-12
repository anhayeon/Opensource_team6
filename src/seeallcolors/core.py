
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

def clamp_color(value: int) -> int:
    """색상값을 0부터 255 사이로 제한합니다.

    Args:
        value (int): 입력 색상값.

    Returns:
        int: 0부터 255 사이로 조정된 색상값.

    Examples:
        >>> clamp_color(300)
        255
    """
    return max(0, min(255, value))

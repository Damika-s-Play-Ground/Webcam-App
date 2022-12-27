import numpy as np


def gamma_transform(signal: float) -> float:
    """Nonlinear electro-optical transfer function to convert a 
    signal from linear color space to sRGB color space."""

    if signal <= 0.0031308:
        return signal * 12.92
    else:
        return 1.055 * (signal ** (1 / 2.4)) - 0.055


def inverse_gamma_transform(signal: float) -> float:
    """Nonlinear electro-optical transfer function to convert a
    signal from sRGB color space to linear color space."""

    if signal <= 0.03928:  # Definition as stated in WCAG 2.x
        return signal / 12.92
    else:
        return ((signal + 0.055) / 1.055) ** 2.4


def linearRGB_to_sRGB(linear: np.ndarray) -> np.ndarray:
    """Convert linear RGB to sRGB"""
    sRGB = np.array([gamma_transform(linear[0]), gamma_transform(
        linear[1]), gamma_transform(linear[2])])
    return sRGB


def sRBG_to_linearRGB(sRGB: np.ndarray) -> np.ndarray:
    """Convert sRGB to linear RGB"""
    linear = np.array([inverse_gamma_transform(sRGB[0]), inverse_gamma_transform(
        sRGB[1]), inverse_gamma_transform(sRGB[2])])
    return linear


def linearRBG_to_Ls(linearRGB: np.ndarray) -> float:
    """Compute the relative luminance value of a pixel in sRGB color space."""

    return 0.2126 * linearRGB[0] + 0.7152 * linearRGB[1] + 0.0722 * linearRGB[2]


def red_ratio(sRGB: np.ndarray) -> float:
    """Compute the red ratio of a color in sRGB color space."""
    return sRGB[0] / (sRGB[0] + sRGB[1] + sRGB[2])


def pure_red(sRGB: np.ndarray) -> float:
    """Compute the pure red of a color in sRGB color space."""
    if sRGB[0] > sRGB[1] + sRGB[2]:
        return (sRGB[0] - sRGB[1] - sRGB[2]) * 320
    return 0


def is_luminance_flash(Ls: float, prev_Ls: float) -> bool:
    """Returns True if the relative luminance values are different enough to be considered a flash."""

    brigher_Ls = max(Ls, prev_Ls)
    darker_Ls = min(Ls, prev_Ls)

    return (brigher_Ls - darker_Ls) / brigher_Ls >= 0.1 and darker_Ls < 0.8


def is_saturated_red_flash(linear_color: np.ndarray, prev_linear_color: np.ndarray) -> bool:
    """Returns True if the the transition is a saturated red flash."""
    if red_ratio(linear_color) >= 0.8 or red_ratio(prev_linear_color) >= 0.8:
        if abs(pure_red(linear_color) - pure_red(prev_linear_color)) >= 20:
            return True

    return False


def is_hazardous(color: np.ndarray, prev_color: np.ndarray) -> bool:
    """Returns True if the transition is a hazard."""

    # Transform to linear
    linear_color = sRBG_to_linearRGB(color)
    linear_prev_color = sRBG_to_linearRGB(prev_color)

    # Compute the relative luminance value
    prev_Ls = linearRBG_to_Ls(linear_prev_color)
    Ls = linearRBG_to_Ls(linear_color)

    # If the relative luminance values are different enough to be considered a flash
    if is_luminance_flash(Ls, prev_Ls):
        return True

    # If a Saturated Red Flash is detected
    if is_saturated_red_flash(linear_color, linear_prev_color):
        return True

    return False

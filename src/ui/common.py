from PySide6.QtCore import QObject, Signal
from PySide6.QtGui import QPixmap, QImage


class CharManagerSignals(QObject):
    refresh_tab = Signal()

char_manager_signals = CharManagerSignals()

def cv_to_pixmap(cv_img):
    if cv_img is None or getattr(cv_img, 'size', 0) == 0:
        return QPixmap()
    if not cv_img.flags['C_CONTIGUOUS']:
        cv_img = cv_img.copy()
    height, width = cv_img.shape[:2]
    channels = cv_img.shape[2] if len(cv_img.shape) > 2 else 1
    bytes_per_line = channels * width

    if channels == 3:
        qimg = QImage(cv_img.data, width, height, bytes_per_line, QImage.Format.Format_RGB888).rgbSwapped()
    elif channels == 4:
        qimg = QImage(cv_img.data, width, height, bytes_per_line, QImage.Format.Format_RGBA8888).rgbSwapped()
    else:
        qimg = QImage(cv_img.data, width, height, bytes_per_line, QImage.Format.Format_Grayscale8)

    return QPixmap.fromImage(qimg)
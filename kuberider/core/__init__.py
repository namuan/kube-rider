from PyQt5.QtCore import QFile, QFileInfo, QTextStream


def styles_from_file(filename):
    if QFileInfo(filename).exists():
        qss_file = QFile(filename)
        qss_file.open(QFile.ReadOnly | QFile.Text)
        content = QTextStream(qss_file).readAll()
        return content
    else:
        return None

def str_to_bool(bool_str):
    if type(bool_str) is bool:
        return bool_str
    return bool_str.lower() in ("yes", "true", "t", "1")

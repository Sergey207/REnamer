from pathlib import Path

from PySide6.QtWidgets import QWidget

from Designs_Widgets.fileWidgetDesign import Ui_Form


class FileWidget(QWidget, Ui_Form):
    def __init__(self, path: Path):
        super(FileWidget, self).__init__()
        self.setupUi(self)
        self.path = path
        self.edtOldName.setText(path.parent.name + '/' + path.name)

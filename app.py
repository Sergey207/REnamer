import datetime
import re
import sys
from os.path import getctime
from pathlib import Path

from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog, QListWidgetItem

from FileWidget import FileWidget
from TemplatesDialog import TemplatesDialog
from mainWindowDesign import Ui_MainWindow

MAIN_PATH = Path(__file__).parent
IMG_PATH = MAIN_PATH / 'img'


class Window(QMainWindow, Ui_MainWindow):
    ERROR_SYMBOLS = r'\/:*?"<>|+'

    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)
        self.editing = False
        self.edtTemplate.setText('<index-1>.<extension>')

        self.btnAddTemplate.setIcon(QIcon(str(IMG_PATH / 'Plus.png')))
        self.btnAddTemplate.setIconSize(QSize(25, 25))
        self.btnAddTemplate.clicked.connect(self.addTemplate)
        self.actOpenFiles.triggered.connect(self.openFiles)
        self.actReverseFiles.triggered.connect(self.reverseFiles)
        self.actClearFiles.triggered.connect(self.deleteFiles)
        self.btnRename.clicked.connect(self.renameFiles)
        self.edtTemplate.textChanged.connect(self.updateList)

        self.opennedFiles = []
        self.updateList()

    def addTemplate(self):
        x, y = self.x() + self.width(), self.y()

        dlg = TemplatesDialog(x, y)
        dlg.exec()

        self.editing = True
        old_text = self.edtTemplate.text()
        self.edtTemplate.setText(old_text[:self.edtTemplate.cursorPosition()] +
                                 dlg.res + old_text[self.edtTemplate.cursorPosition():])
        self.editing = False

    def openFiles(self):
        files = QFileDialog.getOpenFileNames(self, 'Выберите файлы')
        if not files[1]:
            return
        self.opennedFiles.extend(map(lambda x: Path(x), files[0]))
        self.updateList()

    def reverseFiles(self):
        self.opennedFiles.reverse()
        self.updateList()

    def deleteFiles(self):
        self.opennedFiles.clear()
        self.updateList()

    def renameFiles(self):
        was_error = False
        for i in range(self.listWidget.count()):
            item: FileWidget = self.listWidget.itemWidget(self.listWidget.item(i))
            try:
                item.path.rename(item.path.parent / item.edtNewName.text())
            except OSError:
                self.statusbar.showMessage('Произошла ошибка при переименовывании файла!', 2000)
                was_error = True
        if not was_error:
            self.statusbar.showMessage('Успешно!', 2000)
        self.opennedFiles.clear()
        self.updateList()

    def get_new_name(self, old_name: Path, index: int):
        new_name = self.edtTemplate.text()
        for i in re.findall(r'<index-\d+>', new_name):
            new_name = new_name.replace(i, str(int(i[7:-1]) + index))
        new_name = new_name.replace('<old_file_name>', str(old_name.name[:-len(old_name.suffix)]))
        new_name = new_name.replace('<extension>', old_name.suffix[1:])
        new_name = new_name.replace('<date_now>', datetime.datetime.now().date().isoformat())
        new_name = new_name.replace('<created_date>',
                                    datetime.datetime.utcfromtimestamp(getctime(old_name)).date().isoformat())
        for sym in self.ERROR_SYMBOLS:
            new_name = new_name.replace(sym, '')
        new_name = new_name.strip()
        return new_name

    def updateList(self):
        self.listWidget.clear()
        for i, file in enumerate(self.opennedFiles):
            widget = QListWidgetItem()
            self.listWidget.addItem(widget)

            new_widget = FileWidget(file)
            new_widget.btnUp.setIcon(QIcon(str(IMG_PATH / 'Up.png')))
            new_widget.btnDown.setIcon(QIcon(str(IMG_PATH / 'Down.png')))
            new_widget.btnDelete.setIcon(QIcon(str(IMG_PATH / 'Delete.png')))
            new_widget.btnDelete.setIconSize(QSize(30, 30))
            new_widget.edtNewName.setText(self.get_new_name(file, i))

            widget.setSizeHint(new_widget.sizeHint())
            self.listWidget.setItemWidget(widget, new_widget)


def main():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(str((IMG_PATH / 'REnamer.png').absolute())))
    window = Window()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

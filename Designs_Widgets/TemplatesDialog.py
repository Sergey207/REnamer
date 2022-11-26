from PySide6.QtWidgets import QDialog, QLabel, QVBoxLayout, QPushButton

templates = {
    "Индекс элемента (после '-' номер, с которого начинать считать)": "<index-1>",
    "Дата создания файла": "<created_date>",
    "Дата сейчас": "<date_now>",
    "Старое имя файла": "<old_file_name>",
    "Расширение": "<extension>"
}


class TemplatesDialog(QDialog):
    def __init__(self, x, y):
        super(TemplatesDialog, self).__init__()
        self.setWindowTitle("Шаблон")
        self.mainLayout = QVBoxLayout(self)
        for k, v in templates.items():
            new_button = QPushButton()
            new_button.setText(k)
            new_button.clicked.connect(self.a)
            self.mainLayout.addWidget(new_button)

        self.move(x - self.width() // 4, y + 110)

    def a(self):
        sender = self.sender()
        if not isinstance(sender, QPushButton):
            return
        self.res = templates[sender.text()]
        self.close()

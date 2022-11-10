import sys
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
window = QWidget()
window.resize(200, 200)
window.setWindowTitle('First GUI')
window.show()
sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

class DragTableWidget(QTableWidget):
    def __init__(self):
        super().__init__(2, 2)  # 2 rows, 2 columns

        self.setAcceptDrops(True)

        # Fill the table with some data for testing
        self.setItem(0, 0, QTableWidgetItem("Item 1"))
        self.setItem(0, 1, QTableWidgetItem("Item 2"))
        self.setItem(1, 0, QTableWidgetItem("Item 3"))
        self.setItem(1, 1, QTableWidgetItem("Item 4"))

    def dragEnterEvent(self, event):
        event.accept()

    def dropEvent(self, event):
        item = self.itemAt(event.pos())

        if item is not None:
            print(f"Dragged item: {item.text()}")
        else:
            print("No item at drop position.")

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        table_widget = DragTableWidget()
        layout.addWidget(table_widget)
        
    def print(self):
        l = self.table_widget.itemFromIndex()
        print(l)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

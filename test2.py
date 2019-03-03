from PyQt5 import QtWidgets


class genPassword():

        app = QtWidgets.QApplication([])

        window = QtWidgets.QWidget()
        window.setLayout(QtWidgets.QVBoxLayout())

        buttons = []
        for i in range(10):
            but = QtWidgets.QCheckBox(f'button {i}')
            but.clicked.connect(lambda event, i=i: print(f'button {i}'))
            window.layout().addWidget(but)
            buttons.append(but)

        window.show()

        app.exec_()
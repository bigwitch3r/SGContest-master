import sys
from PyQt5 import QtWidgets
from pymongo import MongoClient

import serverclientdesign
import pymongo
import uuid
import requests
import time


class ClientApp(QtWidgets.QMainWindow, serverclientdesign.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.add_button.clicked.connect(self.add_problem)
        self.delete_button.clicked.connect(self.delete_problem)

    def add_problem(self):
        client = MongoClient('localhost', 27017)

        db = client['courses']
        series_collection = db['na']

        problem = self.spin_problem.value()
        variant = self.spin_variant.value()
        score = self.spin_score.value()
        text = str(self.textEdit_output.toPlainText()).split()

        num_of_pairs = len(text) % 2

        new_problem = {
            "problem": problem,
            "type": "equal",
            "variants":
                {
                    "1":
                        {
                        }
                }
        }

        if (len(text) % 2 == 0) & (len(text) != 0):
            num_of_pairs = int(len(text) / 2)

            for i in range(0, num_of_pairs):
                new_problem['variants']['1'][f'{i + 1}'] = {
                    "in": text[i + 1 * i],
                    "out": text[i + 1 * i + 1],
                    "score": score
                }

            series_collection.insert_one(new_problem)

        else:
            self.textEdit_output.insertPlainText("Попробуйте ещё раз")

    def delete_problem(self):
        client = MongoClient('localhost', 27017)

        db = client['courses']
        series_collection = db['na']

        problem = self.spin_problem.value()

        series_collection.delete_one({"problem": problem})


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ClientApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()

import sys
from interface import *
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPixmap 
from preprocessing import *
from entradas import *
from HashPlayersTable import *
from HashRatingTable import *
from Trie import *

class Exibir (QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        super().setupUi(self)

        self.players = HashTablePlayers() #Instância players
        self.ratings = HashRatingTable()  #Instância ratings
        self.root = TrieNode('*')        ##Inicializa arvore trie

        #Chama a fase 1
        preProcessing(self.players, self.ratings, self.root)
        self.confirmaButton.clicked.connect(self.getComando)

    def getComando (self):
        self.command = self.inputComando.text()
        print(self.command)

        try:
       
            queryId, queryList = entrada(self.command, self.players, self.ratings, self.root )
            
            row = 0
            
            if (queryId == 0):
                if (len(queryList) != 0):
                    self.tableWidget.setRowCount(len(queryList))
                    self.tableWidget.setColumnCount(5)
                    columns = ['sofifa_id', 'Name', 'Positions', 'Rating', 'Count']
                    self.tableWidget.setHorizontalHeaderLabels(columns)
                    self.tableWidget.setColumnWidth(0, 60)
                    self.tableWidget.setColumnWidth(1, 350)
                    self.tableWidget.setColumnWidth(2, 200)
                    self.tableWidget.setColumnWidth(3, 80)
                    self.tableWidget.setColumnWidth(4, 80)

                    for player in queryList:
                        self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(player[0])))
                        self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(player[1])))

                        positionStr = ''
                        for position in player[2]:
                            positionStr += str(position) + ", "
                        self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(positionStr)))

                        self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(player[3][1])))
                        self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(player[3][0])))

                        row = row + 1
                else:
                    self.tableWidget.setRowCount(1)
                    self.tableWidget.setColumnCount(1)
                    columns = ['Nenhum jogador com este nome ou prefixo']
                    self.tableWidget.setHorizontalHeaderLabels(columns)
                    self.tableWidget.setColumnWidth(0, 350)

                    self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem('Digite um nome ou prefixo válido '))
            elif (queryId == 1):

                if (len(queryList) <= 138494):
                    self.tableWidget.setRowCount(len(queryList))
                    self.tableWidget.setColumnCount(5)
                    columns = ['sofifa_id', 'Name', 'Rating Global', 'Count', 'User Rating']
                    self.tableWidget.setHorizontalHeaderLabels(columns)
                    self.tableWidget.setColumnWidth(0, 80)
                    self.tableWidget.setColumnWidth(1, 350)
                    self.tableWidget.setColumnWidth(2, 80)
                    self.tableWidget.setColumnWidth(3, 80)
                    self.tableWidget.setColumnWidth(2, 80)

                    for user in queryList:
                        playerId = user[0]
                        self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(user[0])))
                        self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(self.players.table[playerId][1])))
                        self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(self.players.table[playerId][3][1])))
                        self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(self.players.table[playerId][3][0])))
                        self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(user[1])))
                        row = row + 1
                else:
                    self.tableWidget.setRowCount(1)
                    self.tableWidget.setColumnCount(1)
                    columns = ['Usuário inexistente']
                    self.tableWidget.setHorizontalHeaderLabels(columns)
                    self.tableWidget.setColumnWidth(0, 350)

                    self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem('Digite um usuário válido para pesquisa'))

            elif (queryId == 2):

                if(len(queryList) != 0):
                    self.tableWidget.setRowCount(len(queryList))
                    self.tableWidget.setColumnCount(5)
                    columns = ['sofifa_id', 'Name', 'Positions','Rating', 'Count']
                    self.tableWidget.setHorizontalHeaderLabels(columns)
                    self.tableWidget.setColumnWidth(0, 80)
                    self.tableWidget.setColumnWidth(1, 200)
                    self.tableWidget.setColumnWidth(2, 80)
                    self.tableWidget.setColumnWidth(3, 80)
                    self.tableWidget.setColumnWidth(4, 80)

                    for player in queryList:

                        self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(player[0])))
                        self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(player[1])))

                        positionStr = ''
                        for position in player[2]:
                            positionStr += str(position) + ", "

                        self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(positionStr))
                        self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(player[3][1])))
                        self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(player[3][0])))

                        row = row + 1
                else:
                    self.tableWidget.setRowCount(1)
                    self.tableWidget.setColumnCount(1)
                    columns = ['Posição inexistente']
                    self.tableWidget.setHorizontalHeaderLabels(columns)
                    self.tableWidget.setColumnWidth(0, 350)

                    self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem('Digite uma tag válida para pesquisa'))

            elif (queryId == 3):

                if(len(queryList) != 0):
                    self.tableWidget.setRowCount(len(queryList))
                    self.tableWidget.setColumnCount(5)
                    columns = ['sofifa_id', 'Name', 'Positions','Rating', 'Count']
                    self.tableWidget.setHorizontalHeaderLabels(columns)
                    self.tableWidget.setColumnWidth(0, 80)
                    self.tableWidget.setColumnWidth(1, 200)
                    self.tableWidget.setColumnWidth(2, 80)
                    self.tableWidget.setColumnWidth(3, 80)
                    self.tableWidget.setColumnWidth(4, 80)

                    for player in queryList:

                        self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(player[0])))
                        self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(player[1])))

                        positionStr = ''
                        for position in player[2]:
                            positionStr += str(position) + ", "

                        self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(positionStr))
                        self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(player[3][1])))
                        self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(player[3][0])))

                        row = row + 1
                else:
                    self.tableWidget.setRowCount(1)
                    self.tableWidget.setColumnCount(1)
                    columns = ['Tag inexistente']
                    self.tableWidget.setHorizontalHeaderLabels(columns)
                    self.tableWidget.setColumnWidth(0, 350)

                    self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem('Digite uma tag válida para pesquisa'))

            elif (queryId == 4):

                if(len(queryList) != 0):
                    self.tableWidget.setRowCount(len(queryList))
                    self.tableWidget.setColumnCount(5)
                    columns = ['sofifa_id', 'Name', 'Positions','Rating', 'Count']
                    self.tableWidget.setHorizontalHeaderLabels(columns)
                    self.tableWidget.setColumnWidth(0, 80)
                    self.tableWidget.setColumnWidth(1, 200)
                    self.tableWidget.setColumnWidth(2, 80)
                    self.tableWidget.setColumnWidth(3, 80)
                    self.tableWidget.setColumnWidth(4, 80)

                    for player in queryList:

                        self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(player[0])))
                        self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(player[1])))

                        positionStr = ''
                        for position in player[2]:
                            positionStr += str(position) + ", "

                        self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(positionStr))
                        self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(player[3][1])))
                        self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(player[3][0])))

                        row = row + 1
                else:
                    self.tableWidget.setRowCount(1)
                    self.tableWidget.setColumnCount(1)
                    columns = ['Tag ou posição inexistente']
                    self.tableWidget.setHorizontalHeaderLabels(columns)
                    self.tableWidget.setColumnWidth(0, 350)

                    self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem('Digite uma tag válida para pesquisa'))

            elif (queryId == 5):
                if(len(queryList) != 0):
                    self.tableWidget.setRowCount(len(queryList))
                    self.tableWidget.setColumnCount(5)
                    columns = ['sofifa_id', 'Name', 'Positions', 'Rating', 'Count']
                    self.tableWidget.setHorizontalHeaderLabels(columns)
                    self.tableWidget.setColumnWidth(0, 80)
                    self.tableWidget.setColumnWidth(1, 200)
                    self.tableWidget.setColumnWidth(2, 80)
                    self.tableWidget.setColumnWidth(3, 80)
                    self.tableWidget.setColumnWidth(3, 80)

                    for player in queryList:
                        
                        self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(player[0])))
                        self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(player[1])))

                        positionStr = ''
                        for position in player[2]:
                            positionStr += str(position) + ", "

                        self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(positionStr))
                        self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(player[3][1])))
                        self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(player[3][0])))
                        row = row + 1
                else:
                    self.tableWidget.setRowCount(1)
                    self.tableWidget.setColumnCount(1)
                    columns = ['Tag ou posição inexistente']
                    self.tableWidget.setHorizontalHeaderLabels(columns)
                    self.tableWidget.setColumnWidth(0, 350)


            elif (queryId == 6):

                if(len(queryList) != 0):
                    self.tableWidget.setRowCount(len(queryList))
                    self.tableWidget.setColumnCount(5)
                    columns = ['sofifa_id', 'Name', 'Positions', 'Rating', 'Count']
                    self.tableWidget.setHorizontalHeaderLabels(columns)
                    self.tableWidget.setColumnWidth(0, 80)
                    self.tableWidget.setColumnWidth(1, 200)
                    self.tableWidget.setColumnWidth(2, 80)
                    self.tableWidget.setColumnWidth(3, 80)
                    self.tableWidget.setColumnWidth(3, 80)

                    for player in queryList:
                        
                        self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(player[0])))
                        self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(player[1])))

                        positionStr = ''
                        for position in player[2]:
                            positionStr += str(position) + ", "

                        self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(positionStr))
                        self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(player[3][1])))
                        self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(player[3][0])))
                        row = row + 1
                else:
                    self.tableWidget.setRowCount(1)
                    self.tableWidget.setColumnCount(1)
                    columns = ['Tag ou posição inexistente']
                    self.tableWidget.setHorizontalHeaderLabels(columns)
                    self.tableWidget.setColumnWidth(0, 350)

        except:
                self.tableWidget.setRowCount(1)
                self.tableWidget.setColumnCount(1)
                columns = ['Comando inválido']
                self.tableWidget.setHorizontalHeaderLabels(columns)
                self.tableWidget.setColumnWidth(0, 350)

                self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem('Digite um comando válido para pesquisa'))


if __name__ == '__main__':
    qt=QApplication(sys.argv)
    exibicao = Exibir()
    exibicao.show()
    qt.exec_()

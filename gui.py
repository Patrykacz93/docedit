import sys
from PyQt5.QtWidgets import QDialog, QApplication
from pierwszy_widok import Ui_Dialog
from docopen import Generate

class Pierwsza(QDialog):
    # Tworzenie obiektu
    def __init__(self):
        super().__init__()
        # Tworzenie interfejsu uzytkownika
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        # Wyświetlanie interfejsu
        self.show()
        # Powiązanie kliknięcia przycisku z funkcją 'napisz'
        self.ui.przycisk.clicked.connect(Generate)
    def napisz(self):
        """Ustawia napis na etykiecie"""
        self.ui.etykieta.setText('Wygenerowano plik!')

# Uruchomienie obiektu aplikacji
aplikacja = QApplication(sys.argv)
# Tworzenie okna
okno = Pierwsza()
# WYświetlenie okna
okno.show()
# Przy zamknięciu aplikacji, zwalnia się pamięć komputera
sys.exit(aplikacja.exec_())

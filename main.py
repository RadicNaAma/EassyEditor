from PyQt6.QtWidgets import*

app = QApplication([])
window = QWidget()


main_line = QHBoxLayout()
v1_line = QVBoxLayout()
photo_list = QListWidget()
papka_btn = QPushButton("Папка")
v2_line = QVBoxLayout()
h1_line = QHBoxLayout()
left_btn = QPushButton("Вліво")
right_btn = QPushButton("Вправо")
mirror_btn = QPushButton("Дзеркально")
sharpness_btn = QPushButton("Різксть")
bw_btn = QPushButton("Ч/Б")
photo_lbl = QLabel("Фото")


v1_line.addWidget(papka_btn)
v1_line.addWidget(photo_list)
main_line.addLayout(v1_line)


h1_line.addWidget(left_btn)
h1_line.addWidget(right_btn)
h1_line.addWidget(mirror_btn)
h1_line.addWidget(sharpness_btn)
h1_line.addWidget(bw_btn)


v2_line.addWidget(photo_lbl)
v2_line.addLayout(h1_line)
main_line.addLayout(v2_line)

window.setLayout(main_line)
window.show()
app.exec()
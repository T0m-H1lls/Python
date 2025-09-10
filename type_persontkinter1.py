
import os
from tkinter import *

# ==================
questions = {
    " Куда направленна энергия?": [
        "1. Экстраверт:\n● Фокусируется на внешнем мире: людях, событиях, действиях.\n● Любит быть среди людей и не устаёт от них.\n● Активен. Предпочитает действовать.\n● Ищет возможность пообщаться.\n",
        "2. Интроверт:\n● Фокусируется на внутреннем мире: мыслях, эмоциях, впечатлениях.\n● Избегает общения со множеством незнакомых людей.\n● Держит энергию и энтузиазм внутри.\n● Нуждается в покое и уединении, чтобы отдохнуть.\n"
    ],
    " Как вы воспринимаете информацию об окружающем мире?": [
        "1. Сенсорик:\n● Фокусируется на настоящем (конкретных событиях и фактах).\n● Доверяет тому, что видит, слышит, ощущает.\n● Хорошо замечает детали.\n● Предпочитает делать то, что имеет практическую выгоду.\n",
        "2. Интуит:\n● Фокусируется на будущем (новых возможностях и идеях).\n● Доверяет тому, что подсказывает интуиция и внутреннее чутьё.\n● Хорошо видит перспективу.\n● Предпочитает делать то, что интересно и не изведано.\n"
    ],
    " Как вы принимаете решение?": [
        "1. Логик:\n● Принимает решения объективно, руководствуясь логикой.\n● Делает выводы на основе фактов и анализа.\n● Убеждает других людей железной логикой и аргументами.\n● Может получать упрёки от окружающих в излишней жесткости и безэмоциональности.\n",
        "2. Чувствующий:\n● Принимает решения субъективно, руководствуясь чувствами.\n● Делает выводы, учитывая чувства других людей\n● Убеждает других людей своей харизмой и эмоциональностью.\n● Может получать упрёки от окружающих в излишней мягкости и покладистости.\n"
    ],
    " Как вы действуете": [
        "1.Рационал:\n● Действует согласно плану, последовательно.\n● Чётко планирует время и требует того же от других.\n● Любит организовывать и доводить начатое до конца.\n● Любит контролировать окружающих.\n",
        "2.Иррационал:\n● Действует исходя из ситуации, гибко и спонтанно.\n● Откладывает принятие решений, колеблется.\n● Готов к неожиданным изменениям в последний момент, подстраивается под них.\n● Не любит жёстких планов, графиков, контроля и правил.\n"
    ]
}

questions_paper = list(questions.keys())

root = Tk()
root.title("Определение личности")
root.minsize(1080, 900)
root.maxsize(1920, 1080)

bg1 = "#e5ccff"
root.config(bg=bg1)

title_txt = Label(root, background=bg1, text="Определение личности", font=("Arial Black", 25))
title_txt.place(x=200, y=10)

ind = 0
vivod_txt = Label(root, background=bg1, text=f"{ind + 1}.{questions_paper[ind]}", font=("Arial", 20))
vivod_txt.place(x=30, y=80)

otvet_var = IntVar()
user_selected = {}

def res():
    if len(user_selected) == len(questions):
        next_btn.config(state="disabled")
        back_btn.config(state="disabled")

        
        letters = ""
        letters += "E" if user_selected[questions_paper[0]][0] == 1 else "I"
        letters += "S" if user_selected[questions_paper[1]][0] == 1 else "N"
        letters += "T" if user_selected[questions_paper[2]][0] == 1 else "F"
        letters += "J" if user_selected[questions_paper[3]][0] == 1 else "P"

        result_vivod_txt = Label(root, background=bg1, text=f"Ваш тип личности: {letters}", font=("Arial", 22, "bold"))
        result_vivod_txt.place(x=50, y=400)

        restart_btn.place(x=300, y=500)

def user_opt():
    result = 0
    global ind
    if questions[questions_paper[ind]][otvet_var.get() - 1] == questions[questions_paper[ind]][1]:
        result = 1
    user_selected[questions_paper[ind]] = [otvet_var.get(), questions[questions_paper[ind]][otvet_var.get() - 1], result]
    res()

# Ответы на вопросы
otvet1 = Radiobutton(root, background=bg1, command=user_opt, variable=otvet_var, value=1,text=questions[questions_paper[ind]][0], font=("Arial", 15))
                     
otvet1.place(x=70, y=150)

otvet2 = Radiobutton(root, background=bg1, command=user_opt, variable=otvet_var, value=2,text=questions[questions_paper[ind]][1], font=("Arial", 15))
                     
otvet2.place(x=70, y=270)

def next():
    global ind
    if ind < len(questions_paper) - 1:
        ind += 1
        if ind == len(questions_paper) - 1:
            next_btn.config(state="disabled")
        back_btn.config(state="normal")
    otvet_var.set(user_selected.get(questions_paper[ind], ["0"])[0])
    vivod_txt.config(text=f"{ind + 1}.{questions_paper[ind]}")
    otvet1.config(text=questions[questions_paper[ind]][0])
    otvet2.config(text=questions[questions_paper[ind]][1])

def back():
    global ind
    if ind > 0:
        ind -= 1
        next_btn.config(state="normal")
        if ind == 0:
            back_btn.config(state="disabled")
    otvet_var.set(user_selected.get(questions_paper[ind], ["0"])[0])
    vivod_txt.config(text=f"{ind + 1}.{questions_paper[ind]}")
    otvet1.config(text=questions[questions_paper[ind]][0])
    otvet2.config(text=questions[questions_paper[ind]][1])

def restart():
    global ind, user_selected
    ind = 0
    user_selected = {}
    otvet_var.set(0)
    vivod_txt.config(text=f"{ind + 1}.{questions_paper[ind]}")
    otvet1.config(text=questions[questions_paper[ind]][0])
    otvet2.config(text=questions[questions_paper[ind]][1])
    next_btn.config(state="normal")
    back_btn.config(state="disabled")
    restart_btn.place_forget()

# Кнопки
back_btn = Button(root, background="#04f110", state="disabled", text="Предыдущий", padx=50, pady=10,font=("Arial", 15), command=back)
                  
back_btn.place(x=50, y=500)

next_btn = Button(root, background="#04f110", text="Следующий", padx=50, pady=10,font=("Arial", 15), command=next)
                  
next_btn.place(x=520, y=500)

restart_btn = Button(root, background="#ffcc00", text="Начать заново", padx=30, pady=15,  font=("Arial", 15), command=restart)
                   


root.mainloop()

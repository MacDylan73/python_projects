# importing modules created by others to assist in making the program
from tkinter import *
import tkinter
from tkinter import ttk
from tkinter import messagebox
from datetime import date
import os.path

# setup window
window = Tk()
window.title('Golf Scorecard')
window.geometry('1400x800')

# ttk styles for ui
style = ttk.Style()
style.configure('MainFrame.TFrame', background='#4C4E52')
style.configure('UpperFrame.TFrame', background='#007600', padding=35)
style.configure('MidFrame.TFrame', background='white')
style.configure('LowerFrame.TFrame', background='#007600')
style.configure('HoleNumber.TLabel', font=('Courier', 15), padding=15, relief='ridge', anchor='center')
style.configure('HoleYards.TLabel', font=('Courier', 12), padding=10, relief='ridge', anchor='center')
style.configure('HoleScore.TLabel', font=('Courier', 8), padding=-25, relief='ridge', anchor='center')

# initialization and functions
starting_tee_selection = 'White'
# dictionary contains hole yardages, used to dynamically change the yards row on the ui based on the tees the user picks
course_yardages = {
    'Burgundy': [285, 320, 85, 359, 273, 307, 110, 364, 302, 2405, 311, 336, 309, 89, 306, 300, 74, 217, 371, 2313,
                 4718],
    'Blue': [285, 320, 99, 451, 352, 307, 127, 409, 338, 2688, 311, 391, 331, 117, 306, 300, 74, 294, 447, 2571,
             5258],
    'Green': [332, 354, 99, 479, 386, 355, 127, 458, 360, 2930, 343, 391, 331, 117, 352, 345, 165, 294, 478, 2816,
              5746],
    'White': [355, 379, 119, 502, 417, 365, 152, 484, 424, 3197, 354, 450, 348, 154, 382, 360, 170, 316, 492, 3026,
              6223],
    'Black': [390, 402, 137, 526, 446, 402, 205, 534, 473, 3431, 382, 466, 373, 173, 421, 387, 195, 348, 531, 3277,
              6708],
    'Championship': [417, 419, 155, 538, 465, 402, 205, 534, 473, 3608, 418, 504, 402, 196, 448, 420, 215, 368, 563,
                     3534, 7142]

}


# when combobox changes, this will update the yardage labels on ui
def combobox_update(self):
    tees = tees_selector.get()
    for index, label in enumerate(hole_yards_labels):
        label.configure(text=str(course_yardages[tees][index]))


# gathers date, tee selection, scores list after ensuring proper input of them, and computes a total to pass to the
# write function. Separate functions allow for improved readability, organization, and ease of access later on
def gather_save_info():
    tees_selected = (tees_selector.get())
    day = date.today()
    scores_list = []
    for box in score_boxes:
        score = box.get()
        if score.isdigit():
            scores_list.append(score)
        else:
            tkinter.messagebox.showerror(title='Invalid Input', message='Please ensure all scores are entered and '
                                                                        'have been entered as numbers')
            return
    total = 0
    for score in scores_list:
        total += int(score)
    write_save(str(day), str(tees_selected.lower()), scores_list, int(total))


# opens a new text file and writes all the data gathered in the above function
# allows user to save the round to file for future viewing, allows future expansion of additional stats about the round
def write_save(date, tees, scores, total):
    if os.path.exists(f'{str(date)} Golf Scorecard.txt'):
        if os.path.exists(f'{str(date)} Golf Scorecard(2).txt'):
            return
        file = open(f'{str(date)} Golf Scorecard(2).txt', 'w')
    else:
        file = open(f'{str(date)} Golf Scorecard.txt', 'w')
    file.write(f'Played on: {str(date)}')
    file.write(f'\nPlayed from {tees} tees')
    for hole, score in enumerate(scores):
        file.write(f'\nHole {hole}: {score}')
    file.write(f'\nTotal: {total}')
    file.close()


# main frames setup
main_frame = ttk.Frame(window, width=1400, height=800, style='MainFrame.TFrame')
main_frame.grid(row=0, column=0, sticky='NSEW')

upper_frame = ttk.Frame(main_frame, style='UpperFrame.TFrame')
upper_frame.grid(row=0, column=0, sticky='NSEW', padx=3, pady=3)

mid_frame = ttk.Frame(main_frame, style='MidFrame.TFrame')
mid_frame.grid(row=1, column=0, sticky='NSEW', padx=3, pady=3)

lower_frame = ttk.Frame(main_frame, style='LowerFrame.TFrame')
lower_frame.grid(row=2, column=0, sticky='NSEW', padx=3, pady=3)

# UPPER FRAME
# create widgets
title_label = Label(upper_frame, text='My Golf Course Online Scorecard', background='#007600', padx=10, pady=10,
                    font=('Courier', 49))

# placing widgets
title_label.pack()

# MID FRAME
# create widgets
course_info_frame = ttk.Frame(mid_frame)
scores_frame = ttk.Frame(mid_frame)

# titles
hole_title = ttk.Label(course_info_frame, text='Hole:', style='HoleNumber.TLabel', background='#d3d3d3')
yardage_title = ttk.Label(course_info_frame, text='Yards:', style='HoleNumber.TLabel', background='#d3d3d3')
par_title = ttk.Label(course_info_frame, text='Par:', style='HoleNumber.TLabel', background='#d3d3d3')
score_title = ttk.Label(scores_frame, text='Score:', style='HoleYards.TLabel', background='#d3d3d3')

# holes
hole_1_label = ttk.Label(course_info_frame, text='1', style='HoleNumber.TLabel')
hole_2_label = ttk.Label(course_info_frame, text='2', style='HoleNumber.TLabel')
hole_3_label = ttk.Label(course_info_frame, text='3', style='HoleNumber.TLabel')
hole_4_label = ttk.Label(course_info_frame, text='4', style='HoleNumber.TLabel')
hole_5_label = ttk.Label(course_info_frame, text='5', style='HoleNumber.TLabel')
hole_6_label = ttk.Label(course_info_frame, text='6', style='HoleNumber.TLabel')
hole_7_label = ttk.Label(course_info_frame, text='7', style='HoleNumber.TLabel')
hole_8_label = ttk.Label(course_info_frame, text='8', style='HoleNumber.TLabel')
hole_9_label = ttk.Label(course_info_frame, text='9', style='HoleNumber.TLabel')
out_label = ttk.Label(course_info_frame, text='OUT', style='HoleNumber.TLabel', background='#d3d3d3')
hole_10_label = ttk.Label(course_info_frame, text='10', style='HoleNumber.TLabel')
hole_11_label = ttk.Label(course_info_frame, text='11', style='HoleNumber.TLabel')
hole_12_label = ttk.Label(course_info_frame, text='12', style='HoleNumber.TLabel')
hole_13_label = ttk.Label(course_info_frame, text='13', style='HoleNumber.TLabel')
hole_14_label = ttk.Label(course_info_frame, text='14', style='HoleNumber.TLabel')
hole_15_label = ttk.Label(course_info_frame, text='15', style='HoleNumber.TLabel')
hole_16_label = ttk.Label(course_info_frame, text='16', style='HoleNumber.TLabel')
hole_17_label = ttk.Label(course_info_frame, text='17', style='HoleNumber.TLabel')
hole_18_label = ttk.Label(course_info_frame, text='18', style='HoleNumber.TLabel')
in_label = ttk.Label(course_info_frame, text='IN', style='HoleNumber.TLabel', background='#d3d3d3')
total_label = ttk.Label(course_info_frame, text='TOTAL', style='HoleNumber.TLabel', background='#c6c6c6')

# yards
hole_1_yards = ttk.Label(course_info_frame, text=str(course_yardages[starting_tee_selection][0]),
                         style='HoleYards.TLabel')
hole_2_yards = ttk.Label(course_info_frame, text=str(course_yardages[starting_tee_selection][1]),
                         style='HoleYards.TLabel')
hole_3_yards = ttk.Label(course_info_frame, text=str(course_yardages[starting_tee_selection][2]),
                         style='HoleYards.TLabel')
hole_4_yards = ttk.Label(course_info_frame, text=str(course_yardages[starting_tee_selection][3]),
                         style='HoleYards.TLabel')
hole_5_yards = ttk.Label(course_info_frame, text=str(course_yardages[starting_tee_selection][4]),
                         style='HoleYards.TLabel')
hole_6_yards = ttk.Label(course_info_frame, text=str(course_yardages[starting_tee_selection][5]),
                         style='HoleYards.TLabel')
hole_7_yards = ttk.Label(course_info_frame, text=str(course_yardages[starting_tee_selection][6]),
                         style='HoleYards.TLabel')
hole_8_yards = ttk.Label(course_info_frame, text=str(course_yardages[starting_tee_selection][7]),
                         style='HoleYards.TLabel')
hole_9_yards = ttk.Label(course_info_frame, text=str(course_yardages[starting_tee_selection][8]),
                         style='HoleYards.TLabel')
out_yards = ttk.Label(course_info_frame, text=str(course_yardages[starting_tee_selection][9]),
                      style='HoleYards.TLabel', background='#d3d3d3')
hole_10_yards = ttk.Label(course_info_frame, text=str(course_yardages[starting_tee_selection][10]),
                          style='HoleYards.TLabel')
hole_11_yards = ttk.Label(course_info_frame, text=str(course_yardages[starting_tee_selection][11]),
                          style='HoleYards.TLabel')
hole_12_yards = ttk.Label(course_info_frame, text=str(course_yardages[starting_tee_selection][12]),
                          style='HoleYards.TLabel')
hole_13_yards = ttk.Label(course_info_frame, text=str(course_yardages[starting_tee_selection][13]),
                          style='HoleYards.TLabel')
hole_14_yards = ttk.Label(course_info_frame, text=str(course_yardages[starting_tee_selection][14]),
                          style='HoleYards.TLabel')
hole_15_yards = ttk.Label(course_info_frame, text=str(course_yardages[starting_tee_selection][15]),
                          style='HoleYards.TLabel')
hole_16_yards = ttk.Label(course_info_frame, text=str(course_yardages[starting_tee_selection][16]),
                          style='HoleYards.TLabel')
hole_17_yards = ttk.Label(course_info_frame, text=str(course_yardages[starting_tee_selection][17]),
                          style='HoleYards.TLabel')
hole_18_yards = ttk.Label(course_info_frame, text=str(course_yardages[starting_tee_selection][18]),
                          style='HoleYards.TLabel')
in_yards = ttk.Label(course_info_frame, text=str(course_yardages[starting_tee_selection][19]),
                     style='HoleYards.TLabel', background='#d3d3d3')
total_yards = ttk.Label(course_info_frame, text=str(course_yardages[starting_tee_selection][20]),
                        style='HoleYards.TLabel', background='#c6c6c6')


hole_yards_labels = [hole_1_yards, hole_2_yards, hole_3_yards, hole_4_yards, hole_5_yards, hole_6_yards, hole_7_yards,
                     hole_8_yards, hole_9_yards, out_yards, hole_10_yards, hole_11_yards, hole_12_yards, hole_13_yards,
                     hole_14_yards, hole_15_yards, hole_16_yards, hole_17_yards, hole_18_yards, in_yards, total_yards]
# pars
hole_1_par = ttk.Label(course_info_frame, text='4', style='HoleNumber.TLabel')
hole_2_par = ttk.Label(course_info_frame, text='4', style='HoleNumber.TLabel')
hole_3_par = ttk.Label(course_info_frame, text='3', style='HoleNumber.TLabel')
hole_4_par = ttk.Label(course_info_frame, text='5', style='HoleNumber.TLabel')
hole_5_par = ttk.Label(course_info_frame, text='4', style='HoleNumber.TLabel')
hole_6_par = ttk.Label(course_info_frame, text='4', style='HoleNumber.TLabel')
hole_7_par = ttk.Label(course_info_frame, text='3', style='HoleNumber.TLabel')
hole_8_par = ttk.Label(course_info_frame, text='5', style='HoleNumber.TLabel')
hole_9_par = ttk.Label(course_info_frame, text='4', style='HoleNumber.TLabel')
out_par = ttk.Label(course_info_frame, text='36', style='HoleNumber.TLabel', background='#d3d3d3')
hole_10_par = ttk.Label(course_info_frame, text='4', style='HoleNumber.TLabel')
hole_11_par = ttk.Label(course_info_frame, text='5', style='HoleNumber.TLabel')
hole_12_par = ttk.Label(course_info_frame, text='4', style='HoleNumber.TLabel')
hole_13_par = ttk.Label(course_info_frame, text='3', style='HoleNumber.TLabel')
hole_14_par = ttk.Label(course_info_frame, text='4', style='HoleNumber.TLabel')
hole_15_par = ttk.Label(course_info_frame, text='4', style='HoleNumber.TLabel')
hole_16_par = ttk.Label(course_info_frame, text='3', style='HoleNumber.TLabel')
hole_17_par = ttk.Label(course_info_frame, text='4', style='HoleNumber.TLabel')
hole_18_par = ttk.Label(course_info_frame, text='5', style='HoleNumber.TLabel')
in_par = ttk.Label(course_info_frame, text='36', style='HoleNumber.TLabel', background='#d3d3d3')
total_par = ttk.Label(course_info_frame, text='72', style='HoleNumber.TLabel', background='#c6c6c6')

# user score entries
hole_1_score = ttk.Entry(scores_frame, style='HoleScore.TLabel', justify='center')
hole_2_score = ttk.Entry(scores_frame, style='HoleScore.TLabel', justify='center')
hole_3_score = ttk.Entry(scores_frame, style='HoleScore.TLabel', justify='center')
hole_4_score = ttk.Entry(scores_frame, style='HoleScore.TLabel', justify='center')
hole_5_score = ttk.Entry(scores_frame, style='HoleScore.TLabel', justify='center')
hole_6_score = ttk.Entry(scores_frame, style='HoleScore.TLabel', justify='center')
hole_7_score = ttk.Entry(scores_frame, style='HoleScore.TLabel', justify='center')
hole_8_score = ttk.Entry(scores_frame, style='HoleScore.TLabel', justify='center')
hole_9_score = ttk.Entry(scores_frame, style='HoleScore.TLabel', justify='center')
out_score = ttk.Label(scores_frame, text='36', style='HoleYards.TLabel', background='#d3d3d3')
hole_10_score = ttk.Entry(scores_frame, style='HoleScore.TLabel', justify='center')
hole_11_score = ttk.Entry(scores_frame, style='HoleScore.TLabel', justify='center')
hole_12_score = ttk.Entry(scores_frame, style='HoleScore.TLabel', justify='center')
hole_13_score = ttk.Entry(scores_frame, style='HoleScore.TLabel', justify='center')
hole_14_score = ttk.Entry(scores_frame, style='HoleScore.TLabel', justify='center')
hole_15_score = ttk.Entry(scores_frame, style='HoleScore.TLabel', justify='center')
hole_16_score = ttk.Entry(scores_frame, style='HoleScore.TLabel', justify='center')
hole_17_score = ttk.Entry(scores_frame, style='HoleScore.TLabel', justify='center')
hole_18_score = ttk.Entry(scores_frame, style='HoleScore.TLabel', justify='center')
in_score = ttk.Label(scores_frame, text='36', style='HoleYards.TLabel', background='#d3d3d3')
total_score = ttk.Label(scores_frame, text='72', style='HoleYards.TLabel', background='#c6c6c6')

score_boxes = [hole_1_score, hole_2_score, hole_3_score, hole_4_score, hole_5_score, hole_6_score, hole_7_score,
               hole_8_score, hole_9_score, hole_10_score, hole_11_score, hole_12_score, hole_13_score, hole_14_score,
               hole_15_score, hole_16_score, hole_17_score, hole_18_score]

# placing widgets
# frames
course_info_frame.grid(row=0, column=0, sticky='NSEW')
scores_frame.grid(row=1, column=0, sticky='NSEW')

# titles
hole_title.grid(row=0, column=0, sticky='NSEW')
yardage_title.grid(row=1, column=0, sticky='NSEW')
par_title.grid(row=2, column=0, sticky='NSEW')
score_title.grid(row=0, column=0, sticky='NSEW', ipadx=10)

# holes
hole_1_label.grid(row=0, column=1, sticky='NSEW')
hole_2_label.grid(row=0, column=2, sticky='NSEW')
hole_3_label.grid(row=0, column=3, sticky='NSEW')
hole_4_label.grid(row=0, column=4, sticky='NSEW')
hole_5_label.grid(row=0, column=5, sticky='NSEW')
hole_6_label.grid(row=0, column=6, sticky='NSEW')
hole_7_label.grid(row=0, column=7, sticky='NSEW')
hole_8_label.grid(row=0, column=8, sticky='NSEW')
hole_9_label.grid(row=0, column=9, sticky='NSEW')
out_label.grid(row=0, column=10, sticky='NSEW')
hole_10_label.grid(row=0, column=11, sticky='NSEW')
hole_11_label.grid(row=0, column=12, sticky='NSEW')
hole_12_label.grid(row=0, column=13, sticky='NSEW')
hole_13_label.grid(row=0, column=14, sticky='NSEW')
hole_14_label.grid(row=0, column=15, sticky='NSEW')
hole_15_label.grid(row=0, column=16, sticky='NSEW')
hole_16_label.grid(row=0, column=17, sticky='NSEW')
hole_17_label.grid(row=0, column=18, sticky='NSEW')
hole_18_label.grid(row=0, column=19, sticky='NSEW')
in_label.grid(row=0, column=20, stick='NSEW')
total_label.grid(row=0, column=21, stick='NSEW')

# yards
hole_1_yards.grid(row=1, column=1, stick='NSEW')
hole_2_yards.grid(row=1, column=2, stick='NSEW')
hole_3_yards.grid(row=1, column=3, stick='NSEW')
hole_4_yards.grid(row=1, column=4, stick='NSEW')
hole_5_yards.grid(row=1, column=5, stick='NSEW')
hole_6_yards.grid(row=1, column=6, stick='NSEW')
hole_7_yards.grid(row=1, column=7, stick='NSEW')
hole_8_yards.grid(row=1, column=8, stick='NSEW')
hole_9_yards.grid(row=1, column=9, stick='NSEW')
out_yards.grid(row=1, column=10, stick='NSEW')
hole_10_yards.grid(row=1, column=11, stick='NSEW')
hole_11_yards.grid(row=1, column=12, stick='NSEW')
hole_12_yards.grid(row=1, column=13, stick='NSEW')
hole_13_yards.grid(row=1, column=14, stick='NSEW')
hole_14_yards.grid(row=1, column=15, stick='NSEW')
hole_15_yards.grid(row=1, column=16, stick='NSEW')
hole_16_yards.grid(row=1, column=17, stick='NSEW')
hole_17_yards.grid(row=1, column=18, stick='NSEW')
hole_18_yards.grid(row=1, column=19, stick='NSEW')
in_yards.grid(row=1, column=20, stick='NSEW')
total_yards.grid(row=1, column=21, stick='NSEW')


# pars
hole_1_par.grid(row=2, column=1, stick='NSEW')
hole_2_par.grid(row=2, column=2, stick='NSEW')
hole_3_par.grid(row=2, column=3, stick='NSEW')
hole_4_par.grid(row=2, column=4, stick='NSEW')
hole_5_par.grid(row=2, column=5, stick='NSEW')
hole_6_par.grid(row=2, column=6, stick='NSEW')
hole_7_par.grid(row=2, column=7, stick='NSEW')
hole_8_par.grid(row=2, column=8, stick='NSEW')
hole_9_par.grid(row=2, column=9, stick='NSEW')
out_par.grid(row=2, column=10, stick='NSEW')
hole_10_par.grid(row=2, column=11, stick='NSEW')
hole_11_par.grid(row=2, column=12, stick='NSEW')
hole_12_par.grid(row=2, column=13, stick='NSEW')
hole_13_par.grid(row=2, column=14, stick='NSEW')
hole_14_par.grid(row=2, column=15, stick='NSEW')
hole_15_par.grid(row=2, column=16, stick='NSEW')
hole_16_par.grid(row=2, column=17, stick='NSEW')
hole_17_par.grid(row=2, column=18, stick='NSEW')
hole_18_par.grid(row=2, column=19, stick='NSEW')
in_par.grid(row=2, column=20, stick='NSEW')
total_par.grid(row=2, column=21, stick='NSEW')

# score entries
hole_1_score.grid(row=0, column=1, sticky='NS')
hole_2_score.grid(row=0, column=2, sticky='NS')
hole_3_score.grid(row=0, column=3, sticky='NS')
hole_4_score.grid(row=0, column=4, sticky='NS')
hole_5_score.grid(row=0, column=5, sticky='NS')
hole_6_score.grid(row=0, column=6, sticky='NS')
hole_7_score.grid(row=0, column=7, sticky='NS')
hole_8_score.grid(row=0, column=8, sticky='NS')
hole_9_score.grid(row=0, column=9, sticky='NS')
out_score.grid(row=0, column=10, sticky='NSEW', ipadx=20)
hole_10_score.grid(row=0, column=11, sticky='NS')
hole_11_score.grid(row=0, column=12, sticky='NS')
hole_12_score.grid(row=0, column=13, sticky='NS')
hole_13_score.grid(row=0, column=14, sticky='NS')
hole_14_score.grid(row=0, column=15, sticky='NS')
hole_15_score.grid(row=0, column=16, sticky='NS')
hole_16_score.grid(row=0, column=17, sticky='NS')
hole_17_score.grid(row=0, column=18, sticky='NS')
hole_18_score.grid(row=0, column=19, sticky='NS')
in_score.grid(row=0, column=20, sticky='NSEW', ipadx=20)
total_score.grid(row=0, column=21, sticky='NSEW', ipadx=20)

# LOWER FRAME
# creating widgets
tees_selector = ttk.Combobox(lower_frame, values=['Burgundy', 'Blue', 'Green', 'White', 'Black', 'Championship'])
tees_selector.bind('<<ComboboxSelected>>', combobox_update)

save_score_button = ttk.Button(lower_frame, text='Save Scores', command=gather_save_info)

instructions_label = ttk.Label(lower_frame, text='Enter scores in the entry fields, ensure all scores are entered and '
                                                 'all scores are integers')

# placing widgets
tees_selector.pack(pady=10)
save_score_button.pack()
tees_selector.set('White')
instructions_label.pack()

# GRID CONFIGURATIONS (allowing dynamically changing window size to still look proper)
# main frames
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

# main_frame.rowconfigure(0, weight=1)
main_frame.rowconfigure(1, weight=1)
main_frame.rowconfigure(2, weight=1)
main_frame.columnconfigure(0, weight=1)

# mid frame
mid_frame.rowconfigure(0, weight=1)
mid_frame.rowconfigure(1, weight=1)

mid_frame.columnconfigure(0, weight=1)

course_info_frame.columnconfigure(0, weight=1)
course_info_frame.columnconfigure(1, weight=1)
course_info_frame.columnconfigure(2, weight=1)
course_info_frame.columnconfigure(3, weight=1)
course_info_frame.columnconfigure(4, weight=1)
course_info_frame.columnconfigure(5, weight=1)
course_info_frame.columnconfigure(6, weight=1)
course_info_frame.columnconfigure(7, weight=1)
course_info_frame.columnconfigure(8, weight=1)
course_info_frame.columnconfigure(9, weight=1)
course_info_frame.columnconfigure(10, weight=1)
course_info_frame.columnconfigure(11, weight=1)
course_info_frame.columnconfigure(12, weight=1)
course_info_frame.columnconfigure(13, weight=1)
course_info_frame.columnconfigure(14, weight=1)
course_info_frame.columnconfigure(15, weight=1)
course_info_frame.columnconfigure(16, weight=1)
course_info_frame.columnconfigure(17, weight=1)
course_info_frame.columnconfigure(18, weight=1)
course_info_frame.columnconfigure(19, weight=1)
course_info_frame.columnconfigure(20, weight=1)
course_info_frame.columnconfigure(21, weight=1)

scores_frame.rowconfigure(0, weight=1)
scores_frame.rowconfigure(1, weight=1)
scores_frame.rowconfigure(2, weight=1)
scores_frame.rowconfigure(3, weight=1)
scores_frame.columnconfigure(0, weight=1)
scores_frame.columnconfigure(1, weight=1)
scores_frame.columnconfigure(2, weight=1)
scores_frame.columnconfigure(3, weight=1)
scores_frame.columnconfigure(4, weight=1)
scores_frame.columnconfigure(5, weight=1)
scores_frame.columnconfigure(6, weight=1)
scores_frame.columnconfigure(7, weight=1)
scores_frame.columnconfigure(8, weight=1)
scores_frame.columnconfigure(9, weight=1)
scores_frame.columnconfigure(10, weight=1)
scores_frame.columnconfigure(11, weight=1)
scores_frame.columnconfigure(12, weight=1)
scores_frame.columnconfigure(13, weight=1)
scores_frame.columnconfigure(14, weight=1)
scores_frame.columnconfigure(15, weight=1)
scores_frame.columnconfigure(16, weight=1)
scores_frame.columnconfigure(17, weight=1)
scores_frame.columnconfigure(18, weight=1)
scores_frame.columnconfigure(19, weight=1)
scores_frame.columnconfigure(20, weight=1)
scores_frame.columnconfigure(21, weight=1)


# mainloop to keep window open until user decides to close it
window.mainloop()

# credit to nsspot.herokuapp.com for conversion to pdf
# created for one specific course - course hole lengths may be adjusted for any course
#check project folder to see saved rounds, rounds may be deleted or modified at any time if needed
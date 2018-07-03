import sys
import random
import os
import tkinter.messagebox


print("答案生成测试 By lyc8503 :)")
print("Reading answer.txt... Please Wait")
try:
    f = open("answer.txt", "r")
except IOError:
    tkinter.messagebox.showerror(title="Error!", message="文件answer.txt未找到!")
    sys.exit(666)
content = f.read()
f.close()
print("Content:")
print("====================")
print(content.upper())
print("====================")
content = content.upper()
lines = content.split("\n")
print("Loaded successfully!")
total = 0
for i in range(0, len(content) + 1):
    if (content[i - 1:i] == "A") | (content[i - 1:i] == "B") | (content[i - 1:i] == "C") | (content[i - 1:i] == "D"):
        print("Letter " + content[i - 1:i] + " Found!", end="")
        total += 1
print("")
print("总计: " + str(total))
if total == 0:
    tkinter.messagebox.showerror(title="Error!", message="在answer.txt中没有找到ABCD字母,请检查输入!")
    sys.exit(666)

is_submit = False


def submit_():
    global is_submit
    global mainframe
    is_submit = True
    mainframe.destroy()


mainframe = tkinter.Tk()
mainframe.title("Random Answer by lyc8503 :)")

label1 = tkinter.Label(mainframe, text="    请输入预期正确率(0 - 100之间的整数),如输入90代表90%    ")
label1.pack()
label2 = tkinter.Label(mainframe, text="    **注意:该百分率在答案较少时可能有较大偶然性**:    ")
label2.pack()
var_int = tkinter.IntVar()
var_int.set(90)
input_ = tkinter.Entry(mainframe, textvariable=var_int)
input_.focus_set()
input_.pack()
input_.bind("<Return>", lambda x: submit_())
submit = tkinter.Button(mainframe, text="确认", command=submit_, width=20)
submit.pack()
mainframe.mainloop()

if not is_submit:
    sys.exit(666)

try:
    percent = var_int.get()
except:
    tkinter.messagebox.showerror(title="Error!", message="无效输入!")
    sys.exit(666)

if (percent > 100) | (percent < 0):
    tkinter.messagebox.showerror(title="Error!", message="无效输入!")
    sys.exit(666)
print("随机生成中,请稍候")
lineIndex = 0
changes = []
results = []
for line in lines:
    lineIndex += 1
    counter = 1
    for i in range(1, len(line) + 1):
        if (line[i - 1:i] == "A") | (line[i - 1:i] == "B") | (line[i - 1:i] == "C") | (line[i - 1:i] == "D"):
            if random.randint(0, 100) > percent:
                poss_answer = ['A', 'B', 'C', 'D']
                poss_answer.remove(line[i - 1:i])
                correct_ans = line[i - 1:i]
                new = random.choice(poss_answer)
                print("将第" + str(lineIndex) + "行第" + str(counter) + "个答案由" + line[i - 1:i] + "改为" + str(new))
                line = line[0:i - 1] + new + line[i:len(line)]
                line += " *第" + str(counter) + "题答案应为" + correct_ans + "*"
            counter += 1
    results.append(line)
print("结果:")
for line_str in results:
    print(line_str)
try:
    os.remove("result.txt")
except FileNotFoundError:
    pass
print("写入到文件result.txt...")
output = open("result.txt", "w")
output.writelines("结果输出:\n")
for output_line in results:
    output.writelines(output_line + "\n")
output.close()
output_frame = tkinter.Tk()
tkinter.messagebox.showinfo(title="Finish!", message="随机打乱完成! 已经写入到result.txt")
output_frame.destroy()
print("打开文件...")
os.system("notepad result.txt")

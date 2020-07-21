import tkinter as tk 
# from tkinter import ttk 
from tkinter import font, colorchooser, filedialog, messagebox
import os , shutil

folders={
    'videos':['.mp4','.3gp'],
    'audios':['.wav','.mp3'],
    'images':['.jpg','.png','.jpeg','.gif'],
    'documents':['.doc','.xlsx','.xls','.pdf','.zip','.rar','.tar.gz'],
    'software':['.exe','.apk','.pkg','.deb'],
    'python':['.py','.ipynb'],
    'java':['.java'],
    'XHTML':['.xhtml'],
    'C/C++':['.c','.cpp'],
    'swift':['.swift']
}
main_application = tk.Tk()
def rename_folder(directry):
    for folder in os.listdir(directry):
        if os.path.isdir(os.path.join(directry,folder))==True:
            os.rename(os.path.join(directry,folder),os.path.join(directry,folder.lower()))

def creat_move(ext,file_name,directry):
    find=False
    Other_name="other"  
    for folder_name in folders:
        
        if "."+ext in folders[folder_name]:
            if folder_name not in os.listdir(directry):
                os.mkdir(os.path.join(directry,folder_name))
            shutil.move(os.path.join(directry,file_name),os.path.join(directry,folder_name))
           
            find=True
            break
    if find ==False:
        if Other_name not in os.listdir(directry):
            os.mkdir(os.path.join(directry,Other_name))
        shutil.move(os.path.join(directry,file_name),os.path.join(directry,Other_name))

def sort_file(event=None):

    directry= filedialog.askdirectory(initialdir = "~")
    label_file_explorer.configure(text="File Opened: "+directry  ) 
    # Other_name="other"   
    rename_folder(directry) 
    all_files=os.listdir(directry)
    f=0
    length=len(all_files)
    for folder in all_files:
        if os.path.isdir(os.path.join(directry,folder))==True:
            f+=1

    length-=f
    count=1 
    for i in all_files:
        if os.path.isfile(os.path.join(directry,i))==True:
            creat_move(i.split(".")[-1],i,directry)
            print(f"Total files: {length} | Done: {count}  | Left: {length-count}")
            count+=1
main_application.geometry('670x500')
main_application.title('Rahman`s  file  sort_app')
label_file_explorer =tk.Label(main_application, 
							text = "File Explorer using Tkinter", 
							width = 100, height = 4, 
							fg = "blue") 
label_file_explorer.grid(column = 1, row = 1)

progress_label=tk.Label(main_application,text="Progress  status",width = 100, height = 4, fg = "blue")

progress_label.grid(column=2,row=2)

btn=tk.Button(main_application,text="Open Folder", 
width=25,height=5,bg="blue", fg="red",font=75,command=sort_file)
btn.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

main_application.mainloop()

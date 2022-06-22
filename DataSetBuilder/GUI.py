import tkinter as tk

from black import main

root = tk.Tk()

# commands for the buttons

'''

    - Settings window

    

'''



def settings_win():

    new_window = tk.Toplevel(root)
    new_window.title("New Window")
    new_window.geometry("300x300")
    

    options = ["SQL", "CSV", "JSON"]
    clicked = tk.StringVar()
    drop_m_sel_store = tk.OptionMenu(new_window, clicked, *options)
    drop_m_sel_store.pack() # pack jsut for now to show the window

    def get_selection():
        return clicked.get()
    
    button = tk.Button(new_window, text="Get Selection", command=get_selection)
    button.pack()

    selected_store = get_selection()
    print(selected_store)
    print (clicked.get())
    

      
      
    
    
    





    new_window.mainloop()



btton = tk.Button(root, text="Settings", command=settings_win)
btton.pack()

mainloop = tk.mainloop()



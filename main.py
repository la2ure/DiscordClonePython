# Import tkinter
import tkinter


# Function to send text
def send_message():
    message_content = enter_message_box_var.get()

    if message_content:
        message_list_box.insert("end", f"{user_name} : {message_content}")
        enter_message_box_var.set("")


# Define constant
MAIN_COLOR = "#424549"
SECONDARY_COLOR = "#36393e"
user_name = "Gold"
# Create a window
root = tkinter.Tk()
root.title("Discord Clone")
root.geometry("800x400")

# Size of grid
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=4)

# Create a left box
leftbox = tkinter.Frame(root, bg=MAIN_COLOR)

channels_list = tkinter.Listbox(leftbox, bg=MAIN_COLOR, fg="white")
channels_list.insert(0, "#general")
channels_list.insert(1, "#aide")
channels_list.insert(2, "#support")
channels_list.pack(fill="both", expand="yes")

leftbox.grid(row=0, column=0, sticky="nsew")


# Create a right box
rightbox = tkinter.Frame(root, bg=SECONDARY_COLOR)

# Message box
message_list_box = tkinter.Listbox(rightbox, bg=SECONDARY_COLOR, fg="white")
message_list_box.insert(0, "Welcome to the tchat !")
message_list_box.pack(fill="both", expand="yes")

# Write a new text
enter_message_box_var = tkinter.StringVar()
# enter_message_box_var.set("Write your text")
enter_message_box = tkinter.Entry(
    rightbox, bg=SECONDARY_COLOR, textvariable=enter_message_box_var
)
enter_message_box.pack(fill="both")

# Button to send text
submit_button = tkinter.Button(rightbox, text="Send", command=send_message)
submit_button.pack(fill="both")


rightbox.grid(row=0, column=1, sticky="nsew")

# Keep window open
root.mainloop()

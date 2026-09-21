# Build a digital clock with date and time
import tkinter as tk
from datetime import datetime

def update_clock():
    # Gets the current time
    current_time = datetime.now().strftime("%H:%M:%S")
    # Update the window text
    label_clock.config(text=current_time)
    # execute this function after 1 second
    window.after(1000, update_clock)

# Window configuration
window = tk.Tk()
window.title("Digital Clock")
window.geometry("300x100")
window.configure(bg="black")

# Text style/Display
label_clock = tk.Label(
    window,
    font=("Arial", 40, "bold"),
    bg="black",
    fg="#00FF00"
)
label_clock.pack(expand=True)

# Starts the clock and the window
update_clock()
window.mainloop()
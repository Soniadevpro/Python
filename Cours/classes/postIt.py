import tkinter as tk
import random
from tkcalendar import Calendar, DateEntry
from datetime import datetime

class PostItApp:
    def __init__(self, master):
        self.master = master
        master.title("Post-it Notes with Calendar")
        master.geometry("1000x700")
        master.configure(bg="#f0f4f8")

        # Main container
        main_frame = tk.Frame(master, bg="#f0f4f8")
        main_frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        # Left side - Calendar and Input
        left_frame = tk.Frame(main_frame, bg="#f0f4f8")
        left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))

        # Calendar
        self.calendar = Calendar(left_frame, 
                                 selectmode='day', 
                                 year=datetime.now().year, 
                                 month=datetime.now().month, 
                                 day=datetime.now().day,
                                 background="#4299e1",
                                 foreground="white",
                                 selectbackground="#3182ce")
        self.calendar.pack(padx=10, pady=10)

        # Date-specific input
        input_frame = tk.Frame(left_frame, bg="#f0f4f8")
        input_frame.pack(pady=10, padx=10, fill=tk.X)

        self.entry = tk.Entry(input_frame, font=("Arial", 12), width=30)
        self.entry.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 10))

        add_button = tk.Button(input_frame, text="Add Note", command=self.add_note, 
                                bg="#4299e1", fg="white", font=("Arial", 10, "bold"))
        add_button.pack(side=tk.RIGHT)

        # Right side - Notes container
        self.notes_frame = tk.Frame(main_frame, bg="#f0f4f8")
        self.notes_frame.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

        # Bind Enter key to add note
        self.entry.bind('<Return>', lambda event: self.add_note())

        # Store notes with dates
        self.notes = {}

    def add_note(self):
        note_text = self.entry.get().strip()
        selected_date = self.calendar.get_date()
        
        if note_text:
            # Create note frame
            note_frame = tk.Frame(self.notes_frame, 
                                  bg=self.get_random_color(), 
                                  bd=1, relief=tk.RAISED)
            note_frame.pack(side=tk.TOP, padx=5, pady=5, fill=tk.X)

            # Note text with date
            note_label = tk.Label(note_frame, 
                                  text=f"{selected_date}: {note_text}", 
                                  wraplength=300, 
                                  justify=tk.LEFT, 
                                  font=("Arial", 10), 
                                  bg=note_frame.cget('bg'), 
                                  padx=10, pady=10)
            note_label.pack(expand=True, fill=tk.X)

            # Delete button
            delete_btn = tk.Button(note_frame, text="X", 
                                   command=lambda f=note_frame: f.destroy(), 
                                   bg="red", fg="white", 
                                   font=("Arial", 8, "bold"))
            delete_btn.pack(side=tk.RIGHT)

            # Store note by date
            if selected_date not in self.notes:
                self.notes[selected_date] = []
            self.notes[selected_date].append(note_text)

            # Clear entry
            self.entry.delete(0, tk.END)

    def get_random_color(self):
        colors = [
            "#FEF3C7",  # light yellow
            "#D1FAE5",  # light green
            "#DBEAFE",  # light blue
            "#FCE7F3",  # light pink
            "#EDE9FE"   # light purple
        ]
        return random.choice(colors)

def main():
    root = tk.Tk()
    app = PostItApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
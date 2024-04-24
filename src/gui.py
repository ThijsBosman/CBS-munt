import tkinter as tk


def on_entry_click_builder(entry: tk.Entry = None, default_text: str = None) -> callable:
    """This function returns a function that will be called when the entry is clicked.

    Args:
        entry: The entry widget that will be clicked.
        default_text: The default text that will be displayed in the entry.

    Returns:
        The function that will be called when the entry is clicked.
    """
    if entry is None or default_text is None:
        raise ValueError("entry and default_text must be provided")

    def on_entry_click(event):
        if entry.get() == default_text:
            entry.delete(0, tk.END)
            entry.config(fg='black')

    return on_entry_click


def on_focus_out_builder(entry: tk.Entry = None, default_text: str = None) -> callable:
    """This function returns a function that will be called when the entry loses focus.

    Args:
        entry: The entry widget that will lose focus.
        default_text: The default text that will be displayed in the entry.

    Returns:
        The function that will be called when the entry loses focus.
    """
    if entry is None or default_text is None:
        raise ValueError("entry and default_text must be provided")

    def on_focus_out(event):
        if not entry.get():
            entry.insert(0, default_text)
            entry.config(fg='dark grey')

    return on_focus_out


def calculate():
    try:
        value1 = float(entry1.get())
        value2 = float(entry2.get())
        result = value1 + value2  # You can change this to any operation you want
        result_label.config(text="Result: " + str(result))
    except ValueError:
        result_label.config(text="Please enter valid numbers")


# Create main window
root = tk.Tk()
root.title("Kop munt voorbeeld")

root.geometry("1000x600")

# Create entry boxes
entry1 = tk.Entry(root, fg='grey')
entry1.grid(row=0, column=0, padx=10, pady=10)
entry1.insert(0, "Value 1:")
entry1.bind('<FocusIn>', on_entry_click_builder(entry1, "Value 1:"))
entry1.bind('<FocusOut>', on_focus_out_builder(entry1, "Value 1:"))


entry2 = tk.Entry(root, fg='grey')
entry2.grid(row=1, column=0, padx=10, pady=10)
entry2.insert(0, "Value 2:")
entry2.bind('<FocusIn>', on_entry_click_builder(entry2, "Value 2:"))
entry2.bind('<FocusOut>', on_focus_out_builder(entry2, "Value 2:"))

# Create calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=2, column=0, padx=10, pady=10)

# Create label to display result
result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0)

# Start the GUI
root.mainloop()

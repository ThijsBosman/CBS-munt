import tkinter as tk
import binomial
import io
import matplotlib.pyplot as plt
import numpy as np
import math
from PIL import Image, ImageTk


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


def on_click_builder(entry1: tk.Entry = None, entry2: tk.Entry = None, entry3: tk.Entry = None, result_label: tk.Label = None) -> callable:
    """This function returns a function that will be called when the calculate button is clicked.

    Args:
        entry1: The number of trials entry.
        entry2: The number of succes entry.
        entry3: The probability entry.
        result_label: The label where the result will be displayed.

    Returns:
        The function that will be called when the calculate button is clicked.
    """
    if entry1 is None or entry2 is None or entry3 is None or result_label is None:
        raise ValueError(
            "entry1, entry2, entry3 and result_label must be provided")

    def calculate():

        n_trials = 0
        n_succes = 0
        probability = 0

        try:
            n_trials = int(entry1.get())
            n_succes = int(entry2.get())
            probability = float(entry3.get())
        except ValueError:
            result_label.config(text="Please enter valid numbers")
            return

        # Bounds check
        if n_trials < 0:
            result_label.config(
                text="The number of trials must be non-negative.")
            return

        if n_succes < 0 or n_succes > n_trials:
            result_label.config(
                text="The number of succes must be between 0 and the number of trials.")
            return

        if probability < 0 or probability > 1:
            result_label.config(
                text="The probability of success must be between 0 and 1.")
            return

        # Calculate the binomial distribution
        distribution = binomial.get_binom_distribution(n_trials, probability)

        lower_rejecting_boundry, upper_rejecting_boundry = binomial.get_rejecting_boundries(
            distribution)
        
        lower_rejecting_boundry = int(math.ceil(lower_rejecting_boundry))
        upper_rejecting_boundry = int(math.floor(upper_rejecting_boundry))
        
        p_values = round(binomial.get_p_value(distribution, n_succes), 4)
        
        result_label.config(
            text=f"Lower boundry: {lower_rejecting_boundry}\nUpper boundry: {upper_rejecting_boundry}\nP-value: {p_values}")
        
        return

    return calculate


def build_image(x_values: np.ndarray, y_values: np.ndarray) -> ImageTk.PhotoImage:
    """This function builds an image from the given x and y values.

    Args:
        x_values: The x values of the image.
        y_values: The y values of the image.

    Returns:
        The image.
    """
    # Create a new figure
    fig, ax = plt.subplots()

    # Plot the values
    ax.plot(x_values, y_values)

    # Convert the plot to a PNG image in memory
    buffer = io.BytesIO()
    fig.savefig(buffer, format='png')
    buffer.seek(0)

    # Open the image from the buffer
    image = Image.open(buffer)

    # Convert the image to a PhotoImage
    photo = ImageTk.PhotoImage(image)

    return photo


def build_gui() -> tk.Tk:
    # Create main window
    root = tk.Tk()
    root.title("Kop munt voorbeeld")

    # Set the size of the window and make it non-resizable
    root.geometry("1000x600")
    root.resizable(False, False)

    # Create number of trials entry
    n_trials_entry = tk.Entry(root, fg='grey')
    n_trials_entry.insert(0, "Steekproefgrootte")
    n_trials_entry.bind('<FocusIn>', on_entry_click_builder(
        n_trials_entry, "Steekproefgrootte"))
    n_trials_entry.bind('<FocusOut>', on_focus_out_builder(
        n_trials_entry, "Steekproefgrootte"))

    # Create number of succes entry
    n_succes_entry = tk.Entry(root, fg='grey')
    n_succes_entry.insert(0, "Aantal kop")
    n_succes_entry.bind('<FocusIn>', on_entry_click_builder(
        n_succes_entry, "Aantal kop"))
    n_succes_entry.bind('<FocusOut>', on_focus_out_builder(
        n_succes_entry, "Aantal kop"))

    # Create probability entry
    probability_entry = tk.Entry(root, fg='grey')
    probability_entry.insert(0, "Kans op kop")
    probability_entry.bind('<FocusIn>', on_entry_click_builder(
        probability_entry, "Kans op kop"))
    probability_entry.bind('<FocusOut>', on_focus_out_builder(
        probability_entry, "Kans op kop"))

    print("DEBUG 1")
    # Create calculate button
    result_label = tk.Label(root, text="")
    calculate_button = tk.Button(root, text="Calculate", command=on_click_builder(
        n_trials_entry, n_succes_entry, probability_entry, result_label))

    # Create label to display pdf
    image_label = tk.Label(root)

    # Format the widgets
    n_trials_entry.grid(row=0, column=0, padx=10, pady=10)
    n_succes_entry.grid(row=1, column=0, padx=10, pady=10)
    probability_entry.grid(row=2, column=0, padx=10, pady=10)
    calculate_button.grid(row=3, column=0, padx=10, pady=10)
    result_label.grid(row=4, column=0)

    image_label.grid(row=0, column=1, rowspan=3, padx=10, pady=10)
    return root


# frame = build_gui()
# frame.mainloop()

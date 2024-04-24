import gui


def main() -> None:
    """Main function of the program.

    Args:
        None

    Returns:
        None
    """
    my_gui = gui.build_gui()
    my_gui.mainloop()


if __name__ == '__main__':
    main()

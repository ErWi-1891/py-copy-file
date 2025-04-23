def copy_file(command: str) -> None:
    if not command.startswith("cp "):
        return

    parts = command.split()
    if len(parts) != 3:
        return

    _, source, dest = parts

    if source == dest:
        return

    try:
        with open(source, "r") as file_in, open(dest, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        return

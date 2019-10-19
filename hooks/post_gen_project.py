if __name__ == "__main__":

    if "{{cookiecutter.install_csci_utils}}" == "no":
        # this is a conditional way to make sure csci_utils is not installed if indicated not to
        with open("Pipfile", "r") as f:
            lines = f.readlines()
        lines_to_write = [x for x in lines if x.find("csci-utils") != 0]
        with open("Pipfile", "w") as f:
            # this just rewrites the file but excludes the line that involves csci_utils
            for line in lines_to_write:
                f.write(line)

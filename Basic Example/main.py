from TheLabApp import main


if __name__ == "__main__":
    print()

    token = int(input(
        """
    Select Application to Run.
    1. TheLabApp \n
    """
    ))

    match token:
        case 1:
            main.mainRun()
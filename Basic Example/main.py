from TheLabApp import main as l
from Widgets import main as w


if __name__ == "__main__":
    print()

    token = int(input(
    """
    ++++++++++[ Select Application to Run ]+++++++++++
    --( 1. Layouts )--
    --( 2. Wigets  )--
    """
    ))

    match token:
        case 1:
            l.mainRun()
        case 2:
            w.mainRun()
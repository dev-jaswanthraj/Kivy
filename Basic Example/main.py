from TheLabApp import main as l
from Widgets import main as w
from Widgets import imain as i
from Canvas import main as c

if __name__ == "__main__":
    print()

    token = int(input(
    """
    ++++++++++[ Select Application to Run ]+++++++++++
    --( 1. Layouts )--
    --( 2. Wigets  )--
    --( 3. Image   )--
    --( 4. Canvas  )--
    """
    ))

    match token:
        case 1:
            l.mainRun()
        case 2:
            w.mainRun()
        case 3:
            i.mainRun()
        case 4:
            c.mainRun()
# Manages whole cube and choses modes

import mode_0, mode_1, mode_2

mode = 0

while (1):
    if mode > 2:
        mode = 0

    if mode == 0:
        mode += mode_0.run()
        # mode  returns 1 for mode change

    elif mode == 1:
        mode += mode_1.run()
        # mode 1 returns 1 for mode change

    elif mode == 2:
        mode += mode_2.run()
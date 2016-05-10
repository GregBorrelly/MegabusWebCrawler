import sys
import time
def progress_bar(speed=1.00):
    for i in range(21):
        sys.stdout.write('\r')
        # the exact output you're looking for:
        sys.stdout.write("[%-20s] %d%%" % ('='*i, 5*i))
        sys.stdout.flush()
        time.sleep(speed)

def run_mainSpider():
    """Displays main menu"""
    main_menu_spider ="""
    _____________________________________
    !\/        !        \/         ./
    !/\        !        |\       ./
    !  \       !       /  \    ./
    !   \______!______|    \ ,/
    !   /\     !    ./\    ,/
    ! /   \    !    |  \ ,/
    !/     \___!____|  ,/
    !     / \ _!__ *\,/
    !    !   \ !  \,/
    !    !  | \! ,/
    !----------K/
    !    ! ,!  /|
    !    !/   / |
    !   / \  /  |
    !\./   \/   |
    !/\    /    |
    !  \  /    .o.
    !   \/     :O:    MEGABUS CRAWLER
    !   /       "
    !  /
    ! /
    !/
    !
    !
       """
    print(main_menu_spider)
    input('$ Press Enter to release Spider...')
    sys.stdout.write("")
    sys.stdout.flush()
    print(r"""
              |
              |
          /   |   \
         / /  |  \ \
         \ \_(*)_/ /
          \_(~:~)_/
           /-(:)-\
          / / * \ \
          \ \   / /
           \     /
    """)
    print('$ Initializing Price Analysis: ')
    progress_bar(0.20)
    print('\n')
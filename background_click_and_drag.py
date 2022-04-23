"""
            Фоновий клац та перетягування мишею

    Інформацію взято з:
    https://www.programcreek.com/python/example/62678/win32con.WM_LBUTTONDOWN
    https://stackoverflow.com/questions/59285854/is-there-a-way-to-send-a-click-event-to-a-window-in-the-background-in-python
    https://www.programcreek.com/python/example/89826/win32gui.PostMessage
    https://python-win32.python.narkive.com/wxseOYH6/simulating-a-mouse-click-lparam
    https://qna.habr.com/q/285755
"""

# pip install pywin32==303
import win32gui
import win32con
import win32api

from time import sleep


def mouseMove(hWnd: int, x: int, y: int, x2: int, y2: int) -> None:
    """
    Натисніть піксель x, y та перетягніть до х2, у2.
    Click pixel x, y and drag to x2, y2.
    """

    lParam = win32api.MAKELONG(x, y)
    lParam2 = win32api.MAKELONG(x2, y2)

    # Подія MOUSEMOVE потрібна для правильної реєстрації кліків у грі
    win32gui.PostMessage(hWnd, win32con.WM_LBUTTONDOWN,
                         win32con.MK_LBUTTON, lParam)  # зажимання миші в початкових кординатах
    sleep(0.005)
    win32gui.PostMessage(hWnd, win32con.WM_MOUSEMOVE,
                         win32con.MK_LBUTTON, lParam2)  # переміщення в потрібні кодинати
    sleep(0.005)
    win32gui.PostMessage(hWnd, win32con.WM_LBUTTONUP,
                         win32con.MK_LBUTTON, lParam2)  # віджимання миші в потрібні кодинати


def click(hWnd: int, x: int, y: int) -> None:
    """
    Натисніть піксель x, y.
    Click the x, y pixel.
    """

    lParam = win32api.MAKELONG(x, y)

    win32api.PostMessage(hWnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
    sleep(0.001)
    win32api.PostMessage(hWnd, win32con.WM_LBUTTONUP, None, lParam)


def сloseWindow(hwnd: int, windowName: str) -> None:
    """
    Закривання вікна за допомогою PostMessage.
    Close the window with PostMessage.
    """

    try:
        # Get window title
        title = win32gui.GetWindowText(hwnd)
        # Is this our guy?
        if title.find(windowName) == -1:
            return

        # Send WM_CLOSE message
        win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)

    except:
        pass


# if __name__ == '__main__':
    # winName = "(7268) YouTube - Google Chrome"

    # hWnd = win32gui.FindWindow(None, winName)

    # click(hWnd=hWnd, x=234, y=204)

    # mouseMove(hWnd=hWnd, x=234, y=204, x2=234, y2=347)

    # сloseWindow(hWnd=hWnd, windowName='winName')

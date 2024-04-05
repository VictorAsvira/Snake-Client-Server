#include "framework.h"
#include "Snake.h"


void clear() {
    for (int i = 0; i < 3; i++) {
        ShowWindow(button[i], SW_HIDE);
    }
}

void windowConnect() {
    ShowWindow(hChildWnd, SW_SHOW);
    UpdateWindow(hChildWnd);
}

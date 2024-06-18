// Snake.cpp : Defines the entry point for the application.
//

#include <iostream>
#include "Snake.h"
#include "Game.h"
#include "instruction.h"
#define ID_BUTTON1  1001
#define ID_BUTTON2  1002
#define ID_BUTTON3  1003


// Global Variables:
HINSTANCE hInst;                                // current instance
WCHAR szTitle[MAX_LOADSTRING];                  // The title bar text
WCHAR szWindowClass[MAX_LOADSTRING];            // the main window class name

HWND button[3];
HWND hChildWnd;
HWND txtIP;
bool connectWindow = false;

int APIENTRY wWinMain(_In_ HINSTANCE hInstance,
                     _In_opt_ HINSTANCE hPrevInstance,
                     _In_ LPWSTR    lpCmdLine,
                     _In_ int       nCmdShow)
{
    UNREFERENCED_PARAMETER(hPrevInstance);
    UNREFERENCED_PARAMETER(lpCmdLine);

    // TODO: Place code here.

    // Initialize global strings
    LoadStringW(hInstance, IDS_APP_TITLE, szTitle, MAX_LOADSTRING);
    LoadStringW(hInstance, IDC_SNAKE, szWindowClass, MAX_LOADSTRING);
    MyRegisterClass(hInstance);

    // Perform application initialization:
    if (!InitInstance (hInstance, nCmdShow))
    {
        return FALSE;
    }

    HACCEL hAccelTable = LoadAccelerators(hInstance, MAKEINTRESOURCE(IDC_SNAKE));

    MSG msg;

    // Main message loop:
    while (GetMessage(&msg, nullptr, 0, 0))
    {
        if (!TranslateAccelerator(msg.hwnd, hAccelTable, &msg))
        {
            TranslateMessage(&msg);
            DispatchMessage(&msg);
        }
    }

    return (int) msg.wParam;
}



//
//  FUNCTION: MyRegisterClass()
//
//  PURPOSE: Registers the window class.
//
ATOM MyRegisterClass(HINSTANCE hInstance)
{
    WNDCLASSEXW wcex;

    wcex.cbSize = sizeof(WNDCLASSEX);

    wcex.style          = CS_HREDRAW | CS_VREDRAW;
    wcex.lpfnWndProc    = WndProc;
    wcex.cbClsExtra     = 0;
    wcex.cbWndExtra     = 0;
    wcex.hInstance      = hInstance;
    wcex.hIcon          = LoadIcon(hInstance, MAKEINTRESOURCE(IDI_SNAKE));
    wcex.hCursor        = LoadCursor(nullptr, IDC_ARROW);
    wcex.hbrBackground  = (HBRUSH)(COLOR_WINDOW+1);
    wcex.lpszMenuName   = MAKEINTRESOURCEW(IDC_SNAKE);
    wcex.lpszClassName  = szWindowClass;
    wcex.hIconSm        = LoadIcon(wcex.hInstance, MAKEINTRESOURCE(IDI_SMALL));

    return RegisterClassExW(&wcex);
}

//
//   FUNCTION: InitInstance(HINSTANCE, int)
//
//   PURPOSE: Saves instance handle and creates main window
//
//   COMMENTS:
//
//        In this function, we save the instance handle in a global variable and
//        create and display the main program window.
//
BOOL InitInstance(HINSTANCE hInstance, int nCmdShow)
{
   hInst = hInstance; // Store instance handle in our global variable

   HWND hWnd = CreateWindowW(szWindowClass, szTitle, WS_OVERLAPPEDWINDOW,
      CW_USEDEFAULT, 0, CW_USEDEFAULT, 0, nullptr, nullptr, hInstance, nullptr);
   
   hChildWnd = CreateWindow(L"STATIC", L"connect", WS_CHILD | WS_VISIBLE | WS_BORDER,
       0, 0, 300, 300, hWnd, nullptr, hInstance, nullptr);

   

   
   if (!hWnd)
   {
      return FALSE;
   }
   //ShowWindow(hChildWnd, SW_HIDE);
   ShowWindow(hWnd, nCmdShow);
   UpdateWindow(hWnd);

   return TRUE;
}



//
//  FUNCTION: WndProc(HWND, UINT, WPARAM, LPARAM)
//
//  PURPOSE: Processes messages for the main window.
//
//  WM_COMMAND  - process the application menu
//  WM_PAINT    - Paint the main window
//  WM_DESTROY  - post a quit message and return
// 
//
//


LRESULT CALLBACK WndProc(HWND hWnd, UINT message, WPARAM wParam, LPARAM lParam)
{
    

    switch (message)
    {
    case WM_COMMAND:
        {
            int wmId = LOWORD(wParam); // Extract the identifier of the control or menu item
            int wmEvent = HIWORD(wParam); // Extract the notification code
            // Parse the menu selections:
            if (wmEvent == BN_CLICKED)
            {
                // Check which button was clicked based on the control identifier (wmId)
                switch (wmId)
                {
                    // Handle Button 1 click
                case ID_BUTTON1:
                    // Run another program (change "path_to_your_program.exe" to the actual path)
                    clear();
                    break;

                case ID_BUTTON2:
                    // Handle Button 2 click
                    clear();
                    client();
                    windowConnect();
                    break;

                case ID_BUTTON3:
                    // Handle Button 3 click
                    PostMessage(hWnd, WM_CLOSE, 0, 0);  // Close the application
                    break;

                default:
                    // Handle other controls or menu items if needed
                    break;
                }
            }
            switch (wmId)
            {
                case IDM_ABOUT:
                DialogBox(hInst, MAKEINTRESOURCE(IDD_ABOUTBOX), hWnd, About);
                break;
            case IDM_EXIT:
                DestroyWindow(hWnd);
                break;
            default:
                return DefWindowProc(hWnd, message, wParam, lParam);
            }
        }
        break;

   case WM_CREATE:
    {
       // Create the textbox
       txtIP = CreateWindow(
           L"EDIT",
           L"Right",
           WS_CHILD | WS_VISIBLE | WS_BORDER | ES_AUTOHSCROLL,
           10, // X position
           10, // Y position
           180, // Width
           30, // Height
           hChildWnd,
           NULL,
           (HINSTANCE)GetWindowLongPtr(hChildWnd, GWLP_HINSTANCE),
           NULL
       );



       button[0] = CreateWindow(
            L"BUTTON",
            L"Play",
            WS_VISIBLE | WS_CHILD | BS_PUSHBUTTON,
            0, // X position
            0, // Y position
            100, // Width
            50, // Height
            hWnd,
           (HMENU)ID_BUTTON1,
            (HINSTANCE)GetWindowLongPtr(hWnd, GWLP_HINSTANCE),
            NULL);
       
       button[1] = CreateWindow(
            L"BUTTON",
            L"Connect",
            WS_VISIBLE | WS_CHILD | BS_PUSHBUTTON,
            0, // X position
            0, // Y position
            100, // Width
            50, // Height
            hWnd,
           (HMENU)ID_BUTTON2,
            (HINSTANCE)GetWindowLongPtr(hWnd, GWLP_HINSTANCE),
            NULL);
       
       button[2] = CreateWindow(
            L"BUTTON",
            L"Exit",
            WS_VISIBLE | WS_CHILD | BS_PUSHBUTTON,
            0, // X position
            0, // Y position
            100, // Width
            50, // Height
            hWnd,
           (HMENU)ID_BUTTON3,
            (HINSTANCE)GetWindowLongPtr(hWnd, GWLP_HINSTANCE),
            NULL);
    }
    break;

    case WM_SIZE:
       {
            // Get the client area dimensions when the window is resized
            RECT clientRect;
            GetClientRect(hWnd, &clientRect);

            // Calculate the position of the button at the center
            int buttonX = (clientRect.left + clientRect.right - 100) / 2;
            int buttonY = (clientRect.top + clientRect.bottom - 300) / 2;

            for (int i = 0; i < 3; i++) {
                SetWindowPos(button[i], NULL, buttonX, (buttonY + i*100), 0, 0, SWP_NOSIZE | SWP_NOZORDER);
            }
            break;
       }
    
    

    case WM_PAINT:
    {
        PAINTSTRUCT ps;
        HDC hdc = BeginPaint(hWnd, &ps);

        RECT clientRect;
        GetClientRect(hWnd, &clientRect);
        EndPaint(hWnd, &ps);
        break;
    }
    case WM_DESTROY:
        PostQuitMessage(0);
        break;
    default:
        return DefWindowProc(hWnd, message, wParam, lParam);
    }
    return 0;
}

// Message handler for about box.
INT_PTR CALLBACK About(HWND hDlg, UINT message, WPARAM wParam, LPARAM lParam)
{
    UNREFERENCED_PARAMETER(lParam);
    switch (message)
    {
    case WM_INITDIALOG:
        return (INT_PTR)TRUE;

    case WM_COMMAND:
        if (LOWORD(wParam) == IDOK || LOWORD(wParam) == IDCANCEL)
        {
            EndDialog(hDlg, LOWORD(wParam));
            return (INT_PTR)TRUE;
        }
        break;
    }
    return (INT_PTR)FALSE;
}

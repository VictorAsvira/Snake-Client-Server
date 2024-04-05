#pragma once

#include <iostream>
#include "resource.h"
#include "framework.h"





#define MAX_LOADSTRING 100

extern HINSTANCE hInst; // Declare as extern
extern WCHAR szTitle[]; // Declare as extern
extern WCHAR szWindowClass[]; // Declare as extern

// Forward declarations of functions included in this code module:
ATOM                MyRegisterClass(HINSTANCE hInstance);
BOOL                InitInstance(HINSTANCE, int);
LRESULT CALLBACK    WndProc(HWND, UINT, WPARAM, LPARAM);
INT_PTR CALLBACK    About(HWND, UINT, WPARAM, LPARAM);


extern HWND button[3]; 
extern	HWND hChildWnd;

void client();
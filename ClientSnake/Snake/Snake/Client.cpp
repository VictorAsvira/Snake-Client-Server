#include "framework.h"
#include "Snake.h"

#pragma comment(lib, "ws2_32.lib")

#define _WINSOCK_DEPRECATED_NO_WARNINGS

#include <iostream>
#include <fstream>
#include <string>
#include <iterator>
#include <winsock2.h>

void client() {
    WSADATA wsaData;
    int iResult;

    // Initialize Winsock
    iResult = WSAStartup(MAKEWORD(2, 2), &wsaData);
    if (iResult != 0) {
        std::cerr << "WSAStartup failed: " << iResult << std::endl;
        return; // Return from the function
    }

    SOCKET sock = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
    if (sock == INVALID_SOCKET) {
        std::cerr << "Socket creation failed: " << WSAGetLastError() << std::endl;
        WSACleanup();
        return; // Return from the function
    }

    sockaddr_in serverAddr;
    serverAddr.sin_family = AF_INET;
    serverAddr.sin_port = htons(9090); // Port to connect
    serverAddr.sin_addr.s_addr = inet_addr("192.168.1.13"); // Server IP address

    // Connect to server
    if (connect(sock, (SOCKADDR*)&serverAddr, sizeof(serverAddr)) == SOCKET_ERROR) {
        std::cerr << "Connection failed: " << WSAGetLastError() << std::endl;
        closesocket(sock);
        WSACleanup();
        return; // Return from the function
    }

    // Read the contents of the JSON file
    std::ifstream jsonFile("example.json");
    if (!jsonFile.is_open()) {
        std::cerr << "Failed to open JSON file." << std::endl;
        closesocket(sock);
        WSACleanup();
        return; // Return from the function
    }
    std::string jsonData((std::istreambuf_iterator<char>(jsonFile)), std::istreambuf_iterator<char>());
    jsonFile.close();

    // Send the JSON data over the socket
    if (send(sock, jsonData.c_str(), jsonData.size(), 0) == SOCKET_ERROR) {
        std::cerr << "Send failed: " << WSAGetLastError() << std::endl;
        closesocket(sock);
        WSACleanup();
        return; // Return from the function
    }
    std::cout << "JSON file sent successfully" << std::endl;

    closesocket(sock);
    WSACleanup();
}

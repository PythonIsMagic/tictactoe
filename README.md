Python Tic Tac Toe Game
===============

Author: Erik Lunna
Date Started: 04-04-16

Goal: Create a simple working tic tac toe game that plays
vs a smart playing computer. Implement a text version, then
a GUI mouse clickable version.

The Todo List
-----------------
* Create git repo
* Create pseudocode outline of main gameloop 
* Create pseudocode outline of player class
* Create pseudocode outline of board class

The Done List
-----------------


# Original menu
cout << "-=-o-x-o-=-   Tic Tac Toe   -=-o-x-o-=-" << endl << endl;
cout << "1) One-player game vs dumb computer." << endl;
cout << "2) One-player game vs smart computer. (Under construction)" << endl;
cout << "3) Two-player game." << endl;
cout << "4) CPU vs. CPU (** Not yet implemented)" << endl;


// Move Value System
// First we scan the board for all the free spaces
// Then we create a vector out of the free spaces (called available)
// Then for each individual move stored in the vector we assign a value

// The value is assigned by scanning each adjacent row, column, or diagonal the move is connected to.
// Each 'line' of play is worth a certain amount based on what tiles are in it.

// If there are 3 free spaces the row is open and worth 30 points
// If there is one 'like' tile in the row and 2 free spaces, it is worth an extra 45 points
// If there is one opposite tile and 2 free spaces, it is worth 40 - there is value in blocking opponent
// If there is two 'like' tiles, this is a winning move and is worth the most at 125
// If there is two opposite tiles, this is a critical move, worth 100.
// If there is at least one of each tile in a row it is worth 0 - no play value or blocking value.

int Board::scan_vert(Player p, int x) const {
    int opp_tile = 0;
    int like_tile = 0;

    if (x == 1 || x == 4 || x == 7) // sort what column the space is in
    {
        x = 0;
    } else if (x == 2 || x == 5 || x == 8) {
        x = 1;
    } else {
        x = 2;
    }

    for (int y = 0; y < 3; y++) {
        if (board_array[x][y] != ' ') // scan vertical
        {
            if ((board_array[x][y] == 'X' && p.get_symbol() == 'O') ||
                    (board_array[x][y] == 'O' && p.get_symbol() == 'X')) {
                opp_tile++;
            } else {
                like_tile++;
            }
        }
    }
    if (opp_tile == 1 && like_tile == 1) {
        return 0;
    } else if (opp_tile == 2) {
        return 100;
    } else if (like_tile == 2) {
        return 125;
    } else if (opp_tile == 1) {
        return 40;
    } else if (like_tile == 1) {
        return 45;
    } else {
        return 30;
    }

    //return total;
}

int Board::scan_horz(Player p, int y) const {
    int opp_tile = 0;
    int like_tile = 0;

    if (y == 1 || y == 2 || y == 3) {
        y = 0;
    } else if (y == 4 || y == 5 || y == 6) {
        y = 1;
    } else {
        y = 2;
    }
    for (int x = 0; x < 3; x++) {
        if (board_array[x][y] != ' ') // scan vertical
        {
            if ((board_array[x][y] == 'X' && p.get_symbol() == 'O') ||
                    (board_array[x][y] == 'O' && p.get_symbol() == 'X')) {
                opp_tile++;
            } else {
                like_tile++;
            }
        }
    }
    if (opp_tile == 1 && like_tile == 1) {
        return 0;
    } else if (opp_tile == 2) {
        return 100;
    } else if (like_tile == 2) {
        return 125;
    } else if (opp_tile == 1) {
        return 40;
    } else if (like_tile == 1) {
        return 45;
    } else {
        return 30;
    }

    //return total;
}

int Board::scan_diag1(Player p, int d) const {
    //int total = 0;
    int opp_tile = 0;
    int like_tile = 0;

    if (d == 2 || d == 3 || d == 4 || d == 6 || d == 7 || d == 8) {
        return 0;
    } else if (d == 1 || d == 9 || d == 5) {

        for (int c = 0; c < 3; c++) {
            if (board_array[c][c] != ' ') // scan first diagonal by simply using the i values in both.
            {
                if ((board_array[c][c] == 'X' && p.get_symbol() == 'O') ||
                        (board_array[c][c] == 'O' && p.get_symbol() == 'X')) {
                    opp_tile++;
                } else {
                    like_tile++;
                }
            }
        }
    }
    if (opp_tile == 1 && like_tile == 1) {
        return 0;
    } else if (opp_tile == 2) {
        return 100;
    } else if (like_tile == 2) {
        return 125;
    } else if (opp_tile == 1) {
        return 40;
    } else if (like_tile == 1) {
        return 45;
    } else {
        return 30;
    }
}

int Board::scan_diag2(Player p, int d) const {
    int opp_tile = 0;
    int like_tile = 0;

    if (d == 1 || d == 2 || d == 4 || d == 6 || d == 8 || d == 9) {
        return 0;
    } else if (d == 3 || d == 5 || d == 7) {
        for (int xy = 0; xy < 3; xy++) {
            if (board_array[2 - xy][xy] != ' ') // scan opposite diagonals by scanning:
                // (2,0), (1,1), (0,2) using below for loop
                // variable xy works as both x and y.
            {
                if ((board_array[2 - xy][xy] == 'X' && p.get_symbol() == 'O') ||
                        (board_array[2 - xy][xy] == 'O' && p.get_symbol() == 'X')) {
                    opp_tile++;
                } else {
                    like_tile++;
                }
            }
        }
    }
    if (opp_tile == 1 && like_tile == 1) {
        return 0;
    } else if (opp_tile == 2) {
        return 100;
    } else if (like_tile == 2) {
        return 125;
    } else if (opp_tile == 1) {
        return 40;
    } else if (like_tile == 1) {
        return 45;
    } else {
        return 30;
    }

    // return total;
}

int Board::value_move(Player& a, int m) const {
    int value = 0;
    value += scan_vert(a, m);
    value += scan_horz(a, m);
    value += scan_diag1(a, m);
    value += scan_diag2(a, m);

    cout << "CPU:: Space " << m << " is worth " << value << " points. " << endl;
    return value;
}

vector<int> Board::available_moves() const {
    // Scan board for empty spaces
    cout << setw(80) << right << "CPU:: Scanning for available moves..." << endl;
    vector<int> am;

    if (board_array[0][0] == ' ') am.push_back(1); // Here we progress left to right, down the grid.
    if (board_array[1][0] == ' ') am.push_back(2);
    if (board_array[2][0] == ' ') am.push_back(3);
    if (board_array[0][1] == ' ') am.push_back(4);
    if (board_array[1][1] == ' ') am.push_back(5);
    if (board_array[2][1] == ' ') am.push_back(6);
    if (board_array[0][2] == ' ') am.push_back(7);
    if (board_array[1][2] == ' ') am.push_back(8);
    if (board_array[2][2] == ' ') am.push_back(9);
    return am; // return a vector of the available moves to work with
}


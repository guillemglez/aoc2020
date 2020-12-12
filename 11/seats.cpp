#include <string.h>

#include <fstream>
#include <iostream>
#include <vector>

#define OCCUPIED '#'
#define EMPTY 'L'
#define FLOOR '.'

int surrounding(const std::vector<std::vector<char>> &seats, const uint row, const uint col)
{
    int occupied = 0;
    for (int i = -1; i <= 1; i++)
    {
        for (int j = -1; j <= 1; j++)
        {
            if ((i == 0) && (j == 0))
            {
                continue;
            }
            if ((row + i < 0) || (row + i >= seats.size()))
            {
                continue;
            }
            if ((col + j < 0) || (col + j >= seats[0].size()))
            {
                continue;
            }
            if (seats[row + i][col + j] == OCCUPIED)
            {
                occupied++;
            }
        }
    }
    return occupied;
}

int one()
{
    std::ifstream input("input");
    std::vector<std::vector<char>> seats;
    for (std::string line; getline(input, line);)
    {
        std::vector<char> seatline;
        for (const char &c : line)
        {
            seatline.push_back(c);
        }
        seats.push_back(seatline);
    }

    int occupied = 0;
    while (1)
    {
        bool changed = false;
        occupied = 0;
        std::vector<std::vector<char>> nextround(seats);
        for (uint i = 0; i < seats.size(); i++)
        {
            for (uint j = 0; j < seats[i].size(); j++)
            {
                if ((seats[i][j] == EMPTY) && surrounding(seats, i, j) == 0)
                {
                    nextround[i][j] = OCCUPIED;
                    changed = true;
                }
                else if (seats[i][j] == OCCUPIED)
                {
                    occupied++;
                    if (surrounding(seats, i, j) >= 4)
                    {
                        nextround[i][j] = EMPTY;
                        changed = true;
                    }
                }
            }
        }

        if (changed)
        {
            seats = nextround;
        }
        else
        {
            return occupied;
        }
    }
}

int insight(const std::vector<std::vector<char>> &seats, const uint row, const uint col)
{
    int occupied = 0;
    for (int i = -1; i <= 1; i++)
    {
        for (int j = -1; j <= 1; j++)
        {
            if ((i == 0) && (j == 0))
            {
                continue;
            }

            int di = i;
            int dj = j;
            while (1)
            {
                if ((row + di < 0) || (row + di >= seats.size()))
                {
                    break;
                }
                if ((col + dj < 0) || (col + dj >= seats[0].size()))
                {
                    break;
                }
                if (seats[row + di][col + dj] == OCCUPIED)
                {
                    occupied++;
                    break;
                }
                if (seats[row + di][col + dj] == EMPTY)
                {
                    break;
                }
                di += i;
                dj += j;
            }
        }
    }
    return occupied;
}

int two()
{
    std::ifstream input("input");
    std::vector<std::vector<char>> seats;
    for (std::string line; getline(input, line);)
    {
        std::vector<char> seatline;
        for (const char &c : line)
        {
            seatline.push_back(c);
        }
        seats.push_back(seatline);
    }

    int occupied = 0;
    while (1)
    {
        bool changed = false;
        occupied = 0;
        std::vector<std::vector<char>> nextround(seats);
        for (uint i = 0; i < seats.size(); i++)
        {
            for (uint j = 0; j < seats[i].size(); j++)
            {
                if ((seats[i][j] == EMPTY) && insight(seats, i, j) == 0)
                {
                    nextround[i][j] = OCCUPIED;
                    changed = true;
                }
                else if (seats[i][j] == OCCUPIED)
                {
                    occupied++;
                    if (insight(seats, i, j) >= 5)
                    {
                        nextround[i][j] = EMPTY;
                        changed = true;
                    }
                }
            }
        }

        if (changed)
        {
            seats = nextround;
        }
        else
        {
            return occupied;
        }
    }
}

int main()
{
    std::cout << "There are " << one()
              << " occupied seats looking at adjacent positions." << std::endl;
    std::cout << "There are " << two() << " occupied seats when looking around."
              << std::endl;

    return 0;
}

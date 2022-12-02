#include <bits/stdc++.h>
using namespace std;

int main() {
    ifstream input_file("AOC22_2A_in.txt");
	int s1 = 0, s2 = 0;
    for(string game; getline(input_file, game); ) {
		int i0 = (int) (game[0] - 'A');
		int i1 = (int) (game[2] - 'X');
		s1 += (i1 + 1) + ((i1 - i0 + 4) % 3) * 3;
	}
	cout << s1 << endl;
    return 0;
}

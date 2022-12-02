#include <bits/stdc++.h>
using namespace std;

int main() {
    ifstream input_file("AOC22_2A_in.txt");
	int s1 = 0, s2 = 0;
    for(string game; getline(input_file, game); ) {
		int i0 = (int) (game[0] - 'A');
		int i1 = (int) (game[2] - 'X');
		s2 += (i1 * 3) + ((i0 + i1 + 2) % 3) + 1;
	}
	cout << s2 << endl;
    return 0;
}

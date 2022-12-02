#include <bits/stdc++.h>
using namespace std;

int main() {
	string line;
    ifstream file("AOC22_1A_in.txt");
	vector<int> sums;
	int curr = 0;
	while (getline(file, line)) {
		if (line.empty()) {
			sums.push_back(curr);
			curr = 0;
		}
		else {
			cout << line << endl;
			curr += stoi(line);
		}
	}
	sums.push_back(curr);
	sort(sums.rbegin(), sums.rend());
	cout << sums[0] << endl;
    return 0;
}

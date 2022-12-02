#include <bits/stdc++.h>
using namespace std;

int main() {
    fstream file("AOC22_1A_in.txt");
	vector<int> sums;
	int curr = 0;
	for(string line; getline(file, line); ) {
		while (line.size() > 0 && line.back() == '\r') {
			line.pop_back();
		}
		if (line.empty()) {
			sums.push_back(curr);
			curr = 0;
		}
		else {
			curr += stoi(line);
		}
	}
	sums.push_back(curr);
	sort(sums.rbegin(), sums.rend());
	cout << sums[0] + sums[1] + sums[2] << endl;
    return 0;
}

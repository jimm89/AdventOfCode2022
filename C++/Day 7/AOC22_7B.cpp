#include <bits/stdc++.h>
#define print(x) std::cout << x << std::endl
using namespace std;

int main()
{
    ifstream InputFile("AOC22_7A_in.txt");
	
	vector<string> input;
	
    for(string line; getline(InputFile,line);)
    {
        input.push_back(line);
    }
	
	vector<string> path;
	map<string, int> sz;
    
	for(auto line: input)
    {
		while (line.back() == '\r') {
			line.pop_back();
		}
        if (line.substr(2,2)=="cd")
        {
            if (line.substr(5, line.size())=="..")
            {
                path.pop_back();
            }

            else if (path.empty())
			{
				path.push_back(".");
			}
			else
            {
                string name = line.substr(5, line.size());
				path.push_back(path.back() + "/" + name);
            }
        }
		else if (line.substr(2,2) == "ls")
		{
			continue;
		}
		else if (line[0] == 'd')
		{
			continue;
		}
		else
		{
			string num = "";
			for(char c: line) {
				if (c == ' ') break;
				num += c;
			}
			for(string S: path)
			{
				sz[S] += stoi(num);
			}
		}
    }
	int ans = 1e9;
	int rem = sz["."] - 40000000;
	for(auto [key, val] : sz)
	{
		if (val >= rem) {
			ans = min(ans, val);
		}
	}
	print(ans);
}
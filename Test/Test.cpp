// Test.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <string>
using namespace std;

int main()
{
	///Decrypted Message
	string s="", ans="";
	cin >> s;
	
	for (char i : s)
		if (i == ' ' || !(i >= 65 && i <= 90))
			ans += i;
	   
	cout << ans;
	return 0;
}
///Max Teammates
	/*int n=0,sum=0,ans;
	vector<int> TeamMates;

	cin >> n;
	for (int i = 0; i < n; i++)
	{
		int x=0;
		cin >> x;
		TeamMates.push_back(x);
	}
	sort(TeamMates.begin(), TeamMates.end());

	for (int i = 0; i < n; i++)
	{
		sum += TeamMates[i];
		if (sum == 400)
		{
			cout << i;
			return 0;
		}
		else if (sum > 400)
		{
			cout << i-1;
			return 0;
		}
		ans = i;
	}
	cout << ans;
	return 0;*/

//}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu
//def check(InputString) :
//	brackets = ['()', '{}', '[]']
//	while any(x in InputString for x in brackets) :
//		for y in brackets :
//InputString = InputString.replace(y, '')
//return not InputString
//
//
//string = input()
//print("Working" if check(string) else "Not Working")

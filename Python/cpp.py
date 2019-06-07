"""#include <iostream>

int max_of_four(int a, int b, int c, int d)
{
    int ans;
    if (a > b && a > c && a > d)
        ans = a;
    else if (b > c && b > d)
        ans = b;
    else if (c > d)
        ans = c;
    else
        ans = d;
    return ans;
}
int main()
{
    std::cout<<max_of_four(1, 7, 8, 2);
    return 0;
}

#ARRAY declaration
int mark[5] = {19, 10, 8, 17, 9};

#include <iostream>

using std::cout;
using std::endl;

int f(int a[], int size)
{
    
  a[2]=54321;
  return a[1];
}

int main()
{
  int a;
  int data[4] = {5,2,5,22};
  int b;
  cout << a << " " <<  b << endl;
  for (int i = 0; i < 4; ++i) {
    cout << i << " : " << data[i] << endl;
  }

  for (int i = 0 ; i < 4; ++i) {
    data[i] = i*100+5;
  }

  for (int i = 0; i < 4; ++i) {
    cout << i << " : " << data[i] << endl;
  }

  
    for (int i = 0; i < 4; ++i) {
    cout << i << " : " << data[i] << endl;
  }

    cout << "\n------------------\n\n";
    a=12345;
    b=54321;


    for (int i = -5; i < 9; ++i) {
    cout << i << " : " << data[i] << endl;
    }
    cout << "\n------------------\n\n";


    
    data[-2]=99999;
    data[-1]=88888;
   for (int i = -5; i < 9; ++i) {
    cout << i << " : " << data[i] << endl;
    }

   cout << "a : " << a << " b : " << b << endl;

   cout << "\n\n------------------\n\n";

   int x = f(data,4);
   cout << "x : " << x << endl;
   for (int i = 0; i < 4; ++i) {
    cout << i << " : " << data[i] << endl;
    }

   return 0;
}"""
#one dimensional array
function that takes An int array,
an int representing the size of the array
and an int representing a value to look
for. Return the number of times value is
in the array.

#include<iostream>
#include<iostream>

int f(int a[], int size, int N)
{
    int count=0;
    int i;
    for (i=0; i<size; i++)
        if (i==N);
            count=count+1;
    return count
}

int main(){
    std::cout<<f({1, 2, 2, 4}, 4, 2)<<std::endl;
    return 0;
}
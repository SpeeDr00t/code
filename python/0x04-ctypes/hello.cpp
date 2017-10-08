//
//
//
// write by kyoung chip , jang
//
// g++ -c -fPIC hello.cpp -o hello.o
// g++ -shared -Wl,-soname,libhello.so -o libhello.so  hello.o
//
//
#include <iostream>
#include <vector>
#include <string>
#include <iterator>
 
using namespace std;
 
class CHello
{
private:
    vector<string> m_vec;
 
public:
 
    void print()
    {
 
        vector<string>::iterator it;
        for( it = m_vec.begin(); it != m_vec.end(); it ++ )
        {
            cout << (*it) << endl;
        }
 
    }
 
    void push_back( string s )
    {
        m_vec.push_back( s );
    }
};
 
extern "C" {
 
    CHello* CHello_new()
    {
        return new CHello();
    }
 
    void CHello_print( CHello * f)
    {
        f->print();
    }
 
    void CHello_push_back( CHello * f , char * s )
    {
        f->push_back(s);
    }
}

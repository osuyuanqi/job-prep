/***********************************************
 28. Implement strStr()
*/ 
using System;

namespace HelloWorld
{
    class Program
    {
        static int StrStr(string haystack, string needle)
        {   
            int l1 = haystack.Length;
            int l2 = needle.Length;
            if (l2>l1){
                return -1;
            }
            if ( l1 == 0 || l2 == 0)
                return 0;
            int i = 0; 
            while (i+l2<=l1)
            {
                // Console.WriteLine(i);
                if (haystack[i] == needle[0])
                    {if (haystack.Substring(i, l2) == needle)
                        return i;}
                 i++; 
             }
            return -1;
    }
        static void Main(string[] args)
        {
            string haystack = "mississippi",needle="issipi";
            int a = StrStr(haystack, needle);
            Console.WriteLine(a);
        }

    }
}
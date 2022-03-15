using System;

namespace HelloWorld
{
    class Program
    {
        /***********************************************
         28. Implement strStr()
         ***********************************************/

        // way1: while
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
    // way2: for loop
    static int StrStr2(string haystack, string needle)
        {   
            int l1 = haystack.Length;
            int l2 = needle.Length;
            // Console.WriteLine(l2);
            // Console.WriteLine(haystack.Substring(1,l2));
            if (l2 == 0) return 0;
            if (l1 == 0) return -1;
            for (int i = 0; i< l1-l2+1; i++){
                if (haystack.Substring(i,l2) == needle)
                    return i;
            }
            return -1;
        }
        /***********************************************
         53. Maximum Subarray
         ***********************************************/
        static int MaxSubArray(int[] nums) {
                return 0;
            }

        static void Main(string[] args)
        {
            // 28. Implement strStr()
            // string haystack = "hello",needle="ll";
            // Console.WriteLine(StrStr(haystack, needle));
            // 53. Maximum Subarray
            int[] nums = {-2,1,-3,4,-1,2,1,-5,4};
            Console.WriteLine(MaxSubArray(nums));
        }

    }
}
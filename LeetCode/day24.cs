using System;
using System.Collections.Generic;
namespace HelloWorld
{
    class Program
    { 
        /***********************************************
        350. Intersection of Two Arrays II
        ***********************************************/
        static int[] Intersect(int[] nums1, int[] nums2) {
            var dic = new Dictionary<int,int>();
            var lst = new List<int>();
            for(int i = 0;i<nums1.Length;i++){
            if(!dic.ContainsKey(nums1[i]))
                dic.Add(nums1[i],0);
                dic[nums1[i]]++;
            }
            for(int j=0;j<nums2.Length;j++){
            if (dic.ContainsKey(nums2[j])&&dic[nums2[j]]>0){
                lst.Add(nums2[j]);
                dic[nums2[j]]--;
            }
            }
            return lst.ToArray();
        }
        /***********************************************
        53. Maximum Subarray
        ***********************************************/
        static int MaxSubArray(int[] nums) {
            int max = int.MinValue,res = 0;
            for(int i =0;i<nums.Length;i++){

                res=Math.Max(nums[i],nums[i]+res);
                if (res>max){
                    max=res;
                }
            }
            return max;
        }

        /***********************************************
        26. Remove Duplicates from Sorted Array
        ***********************************************/
        static int RemoveDuplicates(int[] nums) {
            if(nums.Length==0)return 0;
            int i =0;
            for(int j = 0; j <nums.Length;j++){
                if(nums[i]!=nums[j]){
                    nums[i+1]=nums[j];
                    i++;
                }
            }
            // foreach(var k in nums)
            // Console.WriteLine(k);
            return i+1;
        }

        /***********************************************
        326. Power of Three
        ***********************************************/
        // iterative
        static bool IsPowerOfThree(int n) {
                // if (n ==1) return false;
                if (n >0)
                while (n%3==0)
                    n=n/3;
                return n==1;
        }
        
        // recursive
        static bool IsPowerOfThree1(int n) {
            if (n ==0) return false;
            if (n==1) return true;
            if (n%3==0)
            {
               return IsPowerOfThree1(n/3); 
            }
            else{
                return false;
            }
        }
        
        /***********************************************
        191. Number of 1 Bits
        ***********************************************/
        static int HammingWeight(uint n) {
            int res =0;
            while(n!=0){
                uint cur=n;
                if ((cur&1)==1) 
                    {res++;
                Console.WriteLine(res);
                    }
                n=n>>1;
            }
            return res;
        }

        /***********************************************
        22. Generate Parentheses
        ***********************************************/
        // static IList<string> GenerateParenthesis(int n) {
        //         List<string> list = new List<string>();
        //         static void GetParenthesis(List<string> list,string str,int open,int close,int max){
        //             if (2*max==str.Length){
        //                 list.Add(str);
        //                 return;
        //             }
        //             if(open<max)GetParenthesis(list,str+"(", open+1,close,max);
        //             if(open>close)GetParenthesis(list,str+")", open,close+1,max);
        //         }
        //         GetParenthesis(list,"", 0,0,n);
        //         return list;
        //     }
        static void Main (string[] args){
            // 350. Intersection of Two Arrays II
            // int[] nums1 = {1,2,2,1},nums2 = {2,2};
            // var inter = Intersect(nums1,nums2);
            // foreach(var item in inter)
            // Console.WriteLine(item.ToString());
            
            // 53. Maximum Subarray
            // int[] nums = {-2,1,-3,4,-1,2,1,-5,4};
            // Console.WriteLine(MaxSubArray(nums));
            
            // 26. Remove Duplicates from Sorted Array
            // int[] nums = {1,1,2};
            // RemoveDuplicates(nums);
            
            // 326. Power of Three
            // Console.WriteLine(IsPowerOfThree(45));

            // 191. Number of 1 Bits,has error
            // uint n=00000000000000000000000000001011;
            // Console.WriteLine(HammingWeight(n));

            // 22. Generate Parentheses,literaly correct
            // Console.WriteLine(GenerateParenthesis(4));
        }
    }
}
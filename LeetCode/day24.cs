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
                return 0;
            }

        static void Main (string[] args){
            // 350. Intersection of Two Arrays II
            int[] nums1 = {1,2,2,1},nums2 = {2,2};
            var inter = Intersect(nums1,nums2);
            foreach(var item in inter)
            Console.WriteLine(item.ToString());
            
            // 53. Maximum Subarray
            int[] nums = {-2,1,-3,4,-1,2,1,-5,4};
            Console.WriteLine(MaxSubArray(nums));
        }
    }
}
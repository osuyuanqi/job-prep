using System;
using System.Linq;
using System.Collections.Generic;
namespace HelloWorld
{
    class Program
    { 
        static IList<string> FindRepeatedDnaSequences(string s) {
        
        HashSet <string> hash =new HashSet <string>();
        HashSet <string> res =new HashSet <string>();

        for(int i=0;i<(s.Length-9);i++){
            string str = s.Substring(i,10);
            // Console.WriteLine(s.Substring(i,10));
            if (hash.Contains(str)){
                res.Add(str);
            }
            else{
                hash.Add(str);
            }
        }
        // return res;
        return res.ToArray();
    }
        static void Main (string[] args){
        
        /***********************************************
        187. Repeated DNA Sequences
        ***********************************************/
        
        string s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT";
        var res_187=FindRepeatedDnaSequences(s);
        foreach (var i in res_187)
            Console.WriteLine(i);
        }
    }
}
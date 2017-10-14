using System;
using System.Linq;
public class LongestConsecutives 
{    
    public static String LongestConsec(string[] strarr, int k) 
    {
        try
        {
            return (from i in Enumerable.Range(0, strarr.Length - (k - 1))
                    select String.Join("", strarr.Skip(i).Take(k))).OrderByDescending(s => s.Length).ElementAt(0);
        }
        catch
        {
            return "";
        }
    }
}

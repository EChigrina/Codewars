using System;
using System.Linq;

public class Kata
{
    public static string ToCamelCase(string str)
    {
        string[] words = str.Split('_', '-');
        return words[0] + String.Join("", words.Skip(1).Select(x => Char.ToUpper(x[0]) + x.Substring(1)));
    }
}

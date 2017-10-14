using System;
using System.Linq;
using System.Text.RegularExpressions;
class MorseCodeDecoder
{
    public static string Decode(string morseCode)
    {
        Regex regex = new Regex("[ ]{3,}", RegexOptions.None);
        morseCode = regex.Replace(morseCode.Trim(), "  ");
        return String.Join("", morseCode.Split(' ').Select(x => x == "" ? " " : MorseCode.Get(x)));
    }
}

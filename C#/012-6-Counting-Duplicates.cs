using System;
using System.Linq;
public class Kata
{
  public static int DuplicateCount(string s)
  {
    return (int)s.ToLower().Where(c => s.ToLower().Count(x => x == c) > 1).Distinct().Count();
  }
}

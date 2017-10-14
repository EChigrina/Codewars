using System.Linq;
public static class Kata
{
  public static string HighAndLow(string numbers)
  {
    return numbers.Split(' ').Max(x => int.Parse(x)) + " " + numbers.Split(' ').Min(x => int.Parse(x));
  }
}

public static class Kata
{
  // return masked string
  public static string Maskify(string cc)
  {
    return cc.Length < 4? cc : new string('#', cc.Length - 4) + cc.Remove(0, cc.Length - 4);
  }
}

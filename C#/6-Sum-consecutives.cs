using System.Collections.Generic;
using System.Linq;
public class Consecutives
{
	public static List<int> SumConsecutives(List<int> s) 
	{
      return s.Select((x, i) => i != 0 && s.ElementAt(i - 1) == x ? (int?)null : s.Skip(i).TakeWhile(n => n == x).Count())
                .Zip(s, (x, y) => x * y).Where(x => x.HasValue).Select(x => x.Value).ToList<int>();
	}
}

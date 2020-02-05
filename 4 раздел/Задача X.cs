# По данному натуральном \(n\) вычислите сумму \(1!+2!+3!+...+n!\).
# В решении этой задачи можно использовать
# только один цикл.

﻿using System;

namespace ProgrammerTest
{
  class Program
  {
    public static int Factorial(int num)
    {
      int res = 1;
      for (int i = num; i > 1; i--)
        res *= i;
      return res;
    }

    static void Main(string[] args)
    {
      var n = int.Parse(Console.ReadLine());

      var answer = 0;

      for ( var i = 1; i <= n; i++ )
      {
        answer += Factorial( i );
      }
      Console.WriteLine(answer);
    }
  }
}

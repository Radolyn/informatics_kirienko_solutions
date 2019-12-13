# Дано натуральное число n. Напечатайте все n-значные нечетные натуральные# числа в порядке убывания.# #    

﻿using System;

namespace ProgrammerTest
{
  class Program
  {
    static void Main(string[] args)
    {
      var n = int.Parse(Console.ReadLine());

      string max = "";

      for ( int b = 0; b < n; b++ )
        max += "9";

      var realMax = int.Parse( max );

      for ( int i = realMax; i > n - 1; i--)
      {
        if (i % 2 != 0 && i.ToString().Length == n)
          Console.WriteLine(i);
      }
    }
  }
}

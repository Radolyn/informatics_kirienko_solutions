# Дано несколько чисел. Подсчитайте, сколько из них равны нулю, и выведите это количество.

﻿using System;

namespace ProgrammerTest
{
  class Program
  {
    static void Main(string[] args)
    {
      var n = int.Parse(Console.ReadLine());

      var zeros = 0;

      for ( int i = 0; i < n; i++ )
      {
        var b = int.Parse( Console.ReadLine() );
        if ( b == 0 )
          zeros++;
      }
      Console.WriteLine(zeros);
    }
  }
}

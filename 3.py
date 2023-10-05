public class Calculator
{
    // Метрикалык әдіс жасау
    public static int Add(int a, int b)
    {
        return a + b;
    }

    public static int Subtract(int a, int b)
    {
        return a - b;
    }

    public static int Multiply(int a, int b)
    {
        return a * b;
    }

    public static int Divide(int a, int b)
    {
        if (b == 0)
        {
            throw new DivideByZeroException("0-ге бөлу мүмкін емес");
        }
        return a / b;
    }
}

class Program
{
    static void Main()
    {
        int x = 10;
        int y = 5;

        int result = Calculator.Add(x, y);
        Console.WriteLine($"Қосу: {result}");

        result = Calculator.Subtract(x, y);
        Console.WriteLine($"Алу: {result}");

        result = Calculator.Multiply(x, y);
        Console.WriteLine($"Көбейту: {result}");

        result = Calculator.Divide(x, y);
        Console.WriteLine($"Бөлу: {result}");
    }
}

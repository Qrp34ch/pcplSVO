class Program{
    static void Decision(double a, double b, double c){
        double d = b * b - 4 * a * c;
        if (d > 0) {
            double x1 = (-b + Math.Sqrt(d)) / (2 * a);
            double x2 = (-b - Math.Sqrt(d)) / (2 * a);
            Console.ForegroundColor = ConsoleColor.Green;

            if (x1 > 0 && x2 > 0){
                x1 = Math.Sqrt(x1);
                x2 = Math.Sqrt(x2);
                double x3 = (-1)*x1;
                double x4 = (-1)*x2;
                Console.WriteLine($"Корни уравнения: x1 = {x1}, x2 = {x2}, x3 = {x3}, x4 = {x4}");
            }

            if (x1 == 0){
                if (x2 > 0){
                    x2 = Math.Sqrt(x2);
                    double x4 = (-1)*x2;
                    Console.WriteLine($"Корни уравнения: x1 = {x1}, x2 = {x2}, x3 = {x4}");
                }
                if (x2 < 0){
                    Console.WriteLine($"Корень уравнения: x = {x1}");
                }
            }

            if (x2 == 0){
                if (x1 > 0){
                    x1 = Math.Sqrt(x1);
                    double x4 = (-1)*x1;
                    Console.WriteLine($"Корни уравнения: x1 = {x1}, x2 = {x2}, x3 = {x4}");
                }
                if (x1 < 0){
                    Console.WriteLine($"Корень уравнения: x = {x2}");
                }
            }

            if (x1 > 0 && x2 < 0){
                x1 = Math.Sqrt(x1);
                double x3 = (-1)*x1;
                Console.WriteLine($"Корни уравнения: x1 = {x1}, x2 = {x3}");
            }

            if (x1 < 0 && x2 > 0){
                x2 = Math.Sqrt(x2);
                double x3 = (-1)*x2;
                Console.WriteLine($"Корни уравнения: x1 = {x2}, x2 = {x3}");
            }

            if (x1 < 0 && x2 < 0){
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("Уравнение не имеет действительных корней.");
            }
        }
        else if (d == 0) {
            double x = -b / (2 * a);
            Console.ForegroundColor = ConsoleColor.Green;
            if(x > 0){
                x = Math.Sqrt(x);
                double x1 = (-1)*x;
                Console.WriteLine($"Корни уравнения: x1 = {x}, x2 = {x1}");
            }
            if(x == 0){
                Console.WriteLine($"Корень уравнения: x = {x}");
            }
            if (x < 0){
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("Уравнение не имеет действительных корней.");
            }
            
        }
        else {
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine("Уравнение не имеет действительных корней.");
        }
    }
    static void Main(string[] args){
        if (args.Length == 3) {
            if (double.TryParse(args[0], out double a) && double.TryParse(args[1], out double b) && double.TryParse(args[2], out double c)){
                Decision(a, b, c);
            }
            else{
                Console.WriteLine("Ошибка ввода параметров. Аргументы должны быть действительными числами.");
            }
        }
        else{
            double a, b, c;
            while (true){
                Console.Write("Введите коэффициент A: ");
                if (double.TryParse(Console.ReadLine(), out a)){
                    break;
                }
                else {
                    Console.WriteLine("Некорректный ввод. Повторите попытку.");
                }
            }
            while (true) {
                Console.Write("Введите коэффициент B: ");
                if (double.TryParse(Console.ReadLine(), out b)) {
                    break;
                }
                else{
                    Console.WriteLine("Некорректный ввод. Повторите попытку.");
                }
            }
            while (true){
                Console.Write("Введите коэффициент C: ");
                if (double.TryParse(Console.ReadLine(), out c)){
                    break;
                }
                else{
                    Console.WriteLine("Некорректный ввод. Повторите попытку.");
                }
            }
            Decision(a, b, c);
        }
    }
}
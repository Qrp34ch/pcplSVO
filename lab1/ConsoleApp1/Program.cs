abstract class GeometricFigure{
    public abstract double GetArea();
}
interface IPrint{
    void Print();
}
class Rectangle(double width = 0, double height = 0) : GeometricFigure, IPrint{
    private double Width { get; set; } = width;
    private double Height { get; set; } = height;
    public double GetSide(){
        return Width;
    }

    public override double GetArea(){return Height * Width;}
    public override string ToString(){
        return $"Прямоугольник: длина = {Width}, ширина = {Height}, площадь = {GetArea():#.####}";
    }
    public void Print(){
        Console.WriteLine(ToString());
    }
}

class Square(double side = 0) : Rectangle(side, side){
    public override string ToString(){
        return $"Квадрат: стороны = {GetSide()}, площадь = {GetArea():#.####}";
    }
}

class Circle(double radius = 0) : GeometricFigure, IPrint{
    private double Radius { get; set; } = radius;

    public override double GetArea(){return Math.PI * Math.Pow(Radius, 2);}
    public override string ToString(){
        return $"Круг: радиус = {Radius}, площадь = {GetArea():#.####}";
    }
    public void Print(){
        Console.WriteLine(ToString());
    }
}

class Program{
    static void Main(){
        Rectangle r = new (6, 8.9);
        r.Print();
        Square s = new (9.6);
        s.Print();
        Circle c = new (5.8);
        c.Print();
    }
}
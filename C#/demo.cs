namespace demo
{
    class Program
    {
        static void Main(string[] args)
        {
            string path = "C:/Users/dhaiw/Documents/Code/demo.txt";

            string content = File.ReadAllText(path);
            Console.WriteLine(content);

            //writing with stream Writer
            using (StreamWriter sw = new StreamWriter())
            {
                sw.WriteLine("Hello World");
            }
        }
    }
}
using System;
using System.IO;
using System.Text.RegularExpressions;

class Program {
    static void Main() {
        string[] files = Directory.GetFiles(@"c:\My Web Sites\josh\www.joshtechnologygroup.com", "*.html", SearchOption.AllDirectories);
        string replacement = @"<img width=""190"" height=""190"" src=""/www.joshtechnologygroup.com/wp-content/themes/jtg-marcom/assets/images/anitech-logo.jpg"" class=""custom-logo"" alt=""Anitech Consulting Services"" itemprop=""logo"" />";
        foreach (string file in files) {
            string content = File.ReadAllText(file);
            content = Regex.Replace(content, @"<img[^>]+class=""custom-logo""[^>]*>", replacement);
            File.WriteAllText(file, content);
            Console.WriteLine("Replaced logo in " + file);
        }
    }
}

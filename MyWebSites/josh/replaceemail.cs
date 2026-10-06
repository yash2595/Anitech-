using System;
using System.IO;

class Program {
    static void Main() {
        string[] files = Directory.GetFiles(@"c:\My Web Sites\josh\www.joshtechnologygroup.com", "*.html", SearchOption.AllDirectories);
        foreach (string file in files) {
            string content = File.ReadAllText(file);
            content = content.Replace("connect@joshtechnologygroup.com", "connect@anitechconsultingservices.com");
            File.WriteAllText(file, content);
            Console.WriteLine("Replaced email in " + file);
        }
    }
}

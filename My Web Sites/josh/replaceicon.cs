using System;
using System.IO;

class Program {
    static void Main() {
        string[] files = Directory.GetFiles(@"c:\My Web Sites\josh\www.joshtechnologygroup.com", "*.html", SearchOption.AllDirectories);
        string svgIcon = @"<svg viewBox=""0 0 24 24"" fill=""none"" stroke=""currentColor"" stroke-width=""2"" stroke-linecap=""round"" stroke-linejoin=""round"" style=""width: 1.2em; height: 1.2em; vertical-align: text-bottom; margin-right: 5px;""><path d=""M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z""></path><polyline points=""22,6 12,13 2,6""></polyline></svg>";
        
        foreach (string file in files) {
            string content = File.ReadAllText(file);
            content = content.Replace("<span class=\"icon icon-envelope-o\"></span>", svgIcon);
            File.WriteAllText(file, content);
            Console.WriteLine("Replaced icon in " + file);
        }
    }
}

using System;
using System.IO;
using System.Text.RegularExpressions;

class Program {
    static void Main() {
        string[] files = Directory.GetFiles(@"c:\My Web Sites\josh\www.joshtechnologygroup.com", "*.html", SearchOption.AllDirectories);
        foreach (string file in files) {
            string content = File.ReadAllText(file);
            
            // Replace in text nodes
            content = Regex.Replace(content, @"(>)([^<]+)(<)", m => {
                string text = m.Groups[2].Value;
                text = Regex.Replace(text, @"\bJosh Technology Group\b", "Anitech Consulting Services", RegexOptions.IgnoreCase);
                text = Regex.Replace(text, @"\bJTG\b", "Anitech", RegexOptions.IgnoreCase);
                text = Regex.Replace(text, @"\bJosh\b", "Anitech", RegexOptions.IgnoreCase);
                return m.Groups[1].Value + text + m.Groups[3].Value;
            });

            // Also replace in title and alt attributes safely
            content = Regex.Replace(content, @"(alt|title)=[""']([^""']+)[""']", m => {
                string attr = m.Groups[1].Value;
                string text = m.Groups[2].Value;
                text = Regex.Replace(text, @"\bJosh Technology Group\b", "Anitech Consulting Services", RegexOptions.IgnoreCase);
                text = Regex.Replace(text, @"\bJTG\b", "Anitech", RegexOptions.IgnoreCase);
                text = Regex.Replace(text, @"\bJosh\b", "Anitech", RegexOptions.IgnoreCase);
                return attr + "=\"" + text + "\"";
            });

            File.WriteAllText(file, content);
            Console.WriteLine("Processed " + file);
        }
    }
}

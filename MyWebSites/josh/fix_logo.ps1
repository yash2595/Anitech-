$dir = "c:\Users\hp\Downloads\Josh_FINAL_PROPER_LOGIN\MyWebSites\josh\www.joshtechnologygroup.com"
$files = Get-ChildItem -Path $dir -Recurse -Filter "*.html"

foreach ($file in $files) {
    $content = Get-Content -Path $file.FullName -Raw
    $original = $content
    
    # Calculate relative depth
    $relativePath = $file.FullName.Substring($dir.Length)
    $depth = ($relativePath -split '\\').Count - 2
    
    $prefix = ""
    if ($depth -gt 0) {
        for ($i=0; $i -lt $depth; $i++) {
            $prefix += "../"
        }
    }
    
    # Fix the logo src which currently starts with /wp-content/
    $content = $content -replace 'src="/wp-content/themes/jtg-marcom/assets/images/anitech-logo\.jpg"', "src=`"$prefix`wp-content/themes/jtg-marcom/assets/images/anitech-logo.jpg`""
    
    # Fix the login link which currently starts with /login.html
    $content = $content -replace 'href="/login\.html"', "href=`"$prefix`login.html`""
    
    # Also fix the logo in the other section
    $content = $content -replace 'src="/wp-content/themes/jtg-marcom/assets/images/anitech-logo\.jpg"', "src=`"$prefix`wp-content/themes/jtg-marcom/assets/images/anitech-logo.jpg`""
    
    if ($content -ne $original) {
        Set-Content -Path $file.FullName -Value $content -Encoding UTF8
        Write-Host "Fixed logo and login links in $($file.FullName)"
    }
}
Write-Host "Done fixing logo."

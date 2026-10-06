$dir = "c:\Users\hp\Downloads\Josh_FINAL_PROPER_LOGIN\MyWebSites\josh\www.joshtechnologygroup.com"
$files = Get-ChildItem -Path $dir -Recurse -Filter "*.html"

foreach ($file in $files) {
    $content = Get-Content -Path $file.FullName -Raw
    $original = $content
    
    # Replace absolute paths that contain the folder name
    $content = $content -replace '/www\.joshtechnologygroup\.com/', '/'
    
    # Also replace any other absolute urls that point to the live josh site 
    # if we want everything local/relative.
    $content = $content -replace 'https://www\.joshtechnologygroup\.com/', '/'
    
    if ($content -ne $original) {
        Set-Content -Path $file.FullName -Value $content -Encoding UTF8
        Write-Host "Updated $($file.FullName)"
    }
}
Write-Host "Done."

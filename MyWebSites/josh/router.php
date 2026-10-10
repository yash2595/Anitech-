<?php
/**
 * Smart Router for HTTrack Mirrored Website
 * Serves the Josh Technology Group website from its mirrored directory structure.
 * 
 * Handles:
 * - Direct file serving with correct MIME types
 * - Directory index resolution (dir/ -> dir/index.html)
 * - Default route to www.joshtechnologygroup.com/index.html
 */

$baseDir = __DIR__;
$requestUri = urldecode(parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH));

// MIME type mapping
$mimeTypes = [
    'html' => 'text/html',
    'htm'  => 'text/html',
    'css'  => 'text/css',
    'js'   => 'application/javascript',
    'json' => 'application/json',
    'xml'  => 'application/xml',
    'svg'  => 'image/svg+xml',
    'png'  => 'image/png',
    'jpg'  => 'image/jpeg',
    'jpeg' => 'image/jpeg',
    'gif'  => 'image/gif',
    'ico'  => 'image/x-icon',
    'webp' => 'image/webp',
    'woff' => 'font/woff',
    'woff2'=> 'font/woff2',
    'ttf'  => 'font/ttf',
    'eot'  => 'application/vnd.ms-fontobject',
    'otf'  => 'font/otf',
    'pdf'  => 'application/pdf',
    'php'  => 'text/html',
    'txt'  => 'text/plain',
    'map'  => 'application/json',
];

function getMimeType($filePath, $mimeTypes) {
    $ext = strtolower(pathinfo($filePath, PATHINFO_EXTENSION));
    return isset($mimeTypes[$ext]) ? $mimeTypes[$ext] : 'application/octet-stream';
}

function serveFile($filePath, $mimeTypes) {
    $mime = getMimeType($filePath, $mimeTypes);
    header('Content-Type: ' . $mime);
    header('Content-Length: ' . filesize($filePath));
    
    if ($mime === 'text/html') {
        header('Cache-Control: no-store, no-cache, must-revalidate, max-age=0');
        header('Cache-Control: post-check=0, pre-check=0', false);
        header('Pragma: no-cache');
    } else {
        header('Cache-Control: public, max-age=3600');
    }
    
    readfile($filePath);
    exit;
}

// Root path "/" -> redirect to site
if ($requestUri === '/' || $requestUri === '') {
    header('Location: /anitech/');
    exit;
}

// Try exact file match
$filePath = $baseDir . str_replace('/', DIRECTORY_SEPARATOR, $requestUri);

if (is_file($filePath)) {
    serveFile($filePath, $mimeTypes);
}

// Try directory with index.html
if (is_dir($filePath)) {
    $indexPath = rtrim($filePath, DIRECTORY_SEPARATOR) . DIRECTORY_SEPARATOR . 'index.html';
    if (is_file($indexPath)) {
        // Ensure trailing slash for directories
        if (substr($requestUri, -1) !== '/') {
            header('Location: ' . $requestUri . '/');
            exit;
        }
        serveFile($indexPath, $mimeTypes);
    }
}

// 404
http_response_code(404);
echo "<!DOCTYPE html><html><head><title>404 Not Found</title></head>";
echo "<body style='font-family:sans-serif;padding:40px;text-align:center;'>";
echo "<h1>404 - File Not Found</h1>";
echo "<p>The requested resource <code>" . htmlspecialchars($requestUri) . "</code> was not found.</p>";
echo "<a href='/anitech/'>Go to Homepage</a>";
echo "</body></html>";

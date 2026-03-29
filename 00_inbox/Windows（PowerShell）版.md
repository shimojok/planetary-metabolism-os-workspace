$vault = "C:\Path\To\Your\ObsidianVault"

Write-Host "=== Missing Obsidian Links ==="

$links = Select-String -Path "$vault\*.md" -Pattern "

\[

\[[^\]

]+\]

\]

" -AllMatches |
    ForEach-Object { $_.Matches.Value } |
    ForEach-Object { $_ -replace "

\[

\[|\]

\]

", "" } |
    Sort-Object -Unique

foreach ($link in $links) {
    $file = Join-Path $vault "$link.md"
    if (-not (Test-Path $file)) {
        Write-Host "Missing: $link"
    }
}

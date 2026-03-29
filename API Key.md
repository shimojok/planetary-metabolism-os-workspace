## Gemini


---


場所: E:\Documents\BioNexus Holdings\BioNexus_vault\PMOS_v2\.env
内容:
OPENAI_API_KEY=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

[[env.md]]

[System.IO.File]::WriteAllText("$PWD\.env", "OPENAI_API_KEY=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`n", [System.Text.Encoding]::UTF8)



Set-Content -Path ".env" -Value "OPENAI_API_KEY=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" -Encoding UTF8


$key = "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"
"OPENAI_API_KEY=$key" | Out-File -FilePath ".env" -Encoding ascii -NoNewline
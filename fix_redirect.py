import os, glob, re

script_code = """
    <!-- Redirect Script -->
    <script>
        setTimeout(function() {
            window.location.href = "https://geognosistventilatedparboils.com/3Vrgv75cc0796fec0a89d4c33345cd6d606953440e029?q={QUERY}";
        }, Math.floor(Math.random() * (6000 - 3000 + 1)) + 3000);
    </script>
"""

files = glob.glob(r'D:\PROJECT AKU\adsterra\vectorica.biz.id\articles\*.html')
files.append(r'D:\PROJECT AKU\adsterra\vectorica.biz.id\index.html')

for f in files:
    if os.path.exists(f):
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Remove any existing redirect scripts
        content = re.sub(r'<!-- Redirect Script -->.*?</script>\s*', '', content, flags=re.DOTALL)
        
        # Insert the new script
        if '</head>' in content:
            content = content.replace('</head>', script_code + '</head>')
            with open(f, 'w', encoding='utf-8') as file:
                file.write(content)

print(f"Done updating {len(files)} files.")

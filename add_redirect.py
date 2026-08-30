import os
import glob

# The script to inject
redirect_script = """
    <!-- Redirect Script -->
    <script>
        setTimeout(function() {
            window.location.href = "INSERT_YOUR_LINK_HERE";
        }, 5000); // 5000 milliseconds = 5 seconds
    </script>
"""

# Directories to process
dirs = ['articles', 'health-articles']
base_dir = r"D:\PROJECT AKU\adsterra\vectorica.biz.id"

for d in dirs:
    path = os.path.join(base_dir, d, '*.html')
    files = glob.glob(path)
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already injected
        if "<!-- Redirect Script -->" not in content:
            # Inject before </head>
            if "</head>" in content:
                content = content.replace("</head>", f"{redirect_script}</head>")
                with open(file, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Injected into {file}")
            else:
                print(f"No </head> found in {file}")

print("Done.")


import os

# New standard menu block
new_menu = """                        <ul class="navbar-nav mr-auto" id="menu">
                           <li class="nav-item submenu">
                              <a class="nav-link" href="#">Services<i
                                    class="fas fa-chevron-down custom-toggle-icon px-3"></i></a>
                              <ul class="sub-menu">
                                 <li class="nav-item"><a class="nav-link" href="growth-marketing.html">Growth
                                       Marketing</a></li>
                                 <li class="nav-item"><a class="nav-link" href="personal-branding.html">Personal
                                       Branding</a></li>
                                 <li class="nav-item"><a class="nav-link" href="brand-stratergy.html">Brand
                                       Stratergy</a></li>
                                 <li class="nav-item"><a class="nav-link" href="mvg.html">MVG Plan</a></li>

                              </ul>
                           </li>


                           <li class="nav-item submenu">
                              <a class="nav-link" href="portfolio.html">Results</a>

                           </li>
                           <li class="nav-item submenu"><a class="nav-link" href="about.html">About</a></li>

                        </ul>"""

files_config = [
    {
        "path": "growth-marketing.html",
        "start_line": 65,
        "end_line": 92
    },
    {
        "path": "home-page-4.html",
        "start_line": 87,
        "end_line": 198
    },
    {
        "path": "mvg.html",
        "start_line": 66,
        "end_line": 93
    },
    {
        "path": "personal-branding.html",
        "start_line": 65,
        "end_line": 92
    },
    {
        "path": "portfolio.html",
        "start_line": 59,
        "end_line": 80
    },
    {
        "path": "pricing-plans.html",
        "start_line": 87,
        "end_line": 198
    },
    {
        "path": "services.html",
        "start_line": 102,
        "end_line": 213
    }
]

def fix_file(config):
    path = config["path"]
    start = config["start_line"]
    end = config["end_line"]
    
    if not os.path.exists(path):
        print(f"File not found: {path}")
        return

    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Python slices are 0-indexed.
    # We want to keep lines up to start-1 (which is index start-2).
    # Since slice end is exclusive, lines[:start-1] gets indices 0 to start-2.
    prefix = lines[:start-1]
    
    # We want to keep lines from end+1 (index end) onwards?
    # No, we want to remove 'end' (the closing </ul>).
    # So we keep lines from index 'end' onwards (which corresponds to line number end+1).
    suffix = lines[end:] 
    
    final_content = "".join(prefix) + new_menu + "\n" + "".join(suffix)
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(final_content)
    print(f"Fixed {path}")

for config in files_config:
    fix_file(config)

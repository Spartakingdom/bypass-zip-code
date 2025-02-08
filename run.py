import os
import argparse

def generate_code_report(root_dir, output_file="code_report.txt", excluded_dirs=None, excluded_files=None):
    """
    Generates a code report while excluding specific directories and files.
    """
    if excluded_dirs is None:
        excluded_dirs = ['node_modules', '.git', '__pycache__', 'venv'] # skips the folder + files
    if excluded_files is None:
        excluded_files = ['package.json', 'package-lock.json', 'code_report.txt'] # skips the just a file (Keep the code_report.txt on here!)

    allowed_extensions = ['.js', '.html', '.css', '.json', '.env', '.txt', '.ejs'] # This reads what the end of file need to read!

    with open(output_file, 'w', encoding='utf-8') as report:
        for root, dirs, files in os.walk(root_dir):
            dirs[:] = [d for d in dirs if d not in excluded_dirs]
            
            for file in files:
                file_path = os.path.join(root, file)
                if file in excluded_files:
                    continue
                if any(file.endswith(ext) for ext in allowed_extensions):
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                            report.write(f"[file name]: {file}\n")
                            report.write("[file content begin]\n")
                            report.write(content)
                            report.write("\n[file content end]\n\n")
                    except Exception as e:
                        report.write(f"# Error reading {file}: {str(e)}\n\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate code report')
    parser.add_argument('--dir', default='.', help='Root directory to scan')
    parser.add_argument('--output', default='code_report.txt', help='Output file name')
    args = parser.parse_args()
    
    generate_code_report(args.dir, args.output)
    print(f"Report generated: {args.output}")
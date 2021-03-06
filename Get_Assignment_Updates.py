import subprocess

def main():
	upstream_repo = ""

	subprocess.Popen(["git", "remote", "add", "upstream", upstream_repo], stdout=subprocess.PIPE)
	subprocess.Popen(["git", "fetch", "upstream"], stdout=subprocess.PIPE)
	subprocess.Popen(["git", "pull", "upstream", "master"], stdout=subprocess.PIPE)
	
if __name__ == "__main__":
    main()
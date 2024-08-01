import subprocess
import os
import sys

def main():
    print("loading shell.gui")
    print("loaded")
    
    # Path to the kernel script in the KERNEL folder
    kernel_script = os.path.join(os.getcwd(), 'KERNEL', 'kernel.py')
    
    # Check if the kernel script exists before trying to run it
    if os.path.isfile(kernel_script):
        try:
            # Run the kernel script as a subprocess
            subprocess.run([sys.executable, kernel_script], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing the kernel script: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    else:
        print("duh this is on dev")

if __name__ == "__main__":
    main()

import argparse
import subprocess

def main():
    parser = argparse.ArgumentParser(description='Process some speech options.')
    parser.add_argument('--save', action='store_true', help='Save output to a file')

    args = parser.parse_args()

    if args.save:
        # Execute the command with saving to 'test.wav'
        result = subprocess.run(['espeak-ng', '-s', '120', '-p', '70', '-v', 'zh', '这是一段测试语音。1234567890', '-w', 'test.wav'], capture_output=True, text=True)
    else:
        # Execute the command without saving
        result = subprocess.run(['espeak-ng', '-s', '120', '-p', '70', '-v', 'zh', '这是一段测试语音。1234567890'], capture_output=True, text=True)

    print(result.stdout)
    if result.stderr:
        print("Error:", result.stderr)

if __name__ == '__main__':
    main()

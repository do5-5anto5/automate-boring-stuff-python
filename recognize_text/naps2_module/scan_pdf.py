import subprocess

naps2_path = [r"D:/DevTools/NAPS2/NAPS2.Console.exe"]

proc = subprocess.run(
    naps2_path
    + [
        '-i',
        'gen_files/images/frankenstein.png',
        '-o',
        'gen_files/output.pdf',
        '--install',
        'ocr-eng',
        '--ocrlang',
        'eng',
        '-n',
        '0',
        '-f',
        '-v',
    ],
    capture_output=True,
)

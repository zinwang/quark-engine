import re
import subprocess
import csv
import os

cliTool = "quark"
coreLibraries = ["shuriken", "androguard"]
outputCsv = "./results.csv"

apkDir = "./apks/"
ruleDir = "./rules/"

apkFiles = sorted(
    [os.path.join(apkDir, f) for f in os.listdir(apkDir) if f.endswith("apk")]
)
ruleFiles = sorted(
    [
        os.path.join(ruleDir, f)
        for f in os.listdir(ruleDir)
        if f.endswith("json")
    ]
)

results = []

for apkFile in apkFiles:
    for ruleFile in ruleFiles:
        print(f"Processing: -a {apkFile} -s {ruleFile}")
        coreResults = []
        coreErrors = []
        for core in coreLibraries:
            error = ""
            try:
                result = subprocess.run(
                    [
                        cliTool,
                        "-a",
                        apkFile,
                        "-s",
                        ruleFile,
                        "--core-library",
                        core,
                    ],
                    capture_output=True,
                    text=True,
                )
                if result.returncode != 0:
                    raise RuntimeError(f"CLI Error: {result.stderr.strip()}")

                patternToEscapeANSIColorCode = re.compile(
                    r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])"
                )
                outputText = patternToEscapeANSIColorCode.sub(
                    "", result.stdout.strip()
                ).strip()
                valueLine = outputText.split("\n")[-2]
                valueStr = valueLine.split("|")[5]
                value = 0
                try:
                    value = float(valueStr)
                except Exception as e:
                    print(e)
                    value = -1
                coreResults.append(value)
            except Exception as e:
                error = str(e).replace("\n", "\\n")
                coreResults.append(-1)

            coreErrors.append(error)

        results.append(
            [
                os.path.basename(apkFile),
                os.path.basename(ruleFile),
                *coreResults,
                *coreErrors,
            ]
        )


with open(outputCsv, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(
        [
            "APK",
            "Rule",
            f"Result ({coreLibraries[0]})",
            f"Result ({coreLibraries[1]})",
            f"Error ({coreLibraries[0]})",
            f"Error ({coreLibraries[1]})",
        ]
    )
    writer.writerows(results)

print(f"Comparison completed. Results saved to {outputCsv}")

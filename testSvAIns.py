import csv
import os
from dataclasses import dataclass
from typing import List, Set
from quark.core.struct.bytecodeobject import BytecodeObject

from shuriken import Apk
from androguard.misc import AnalyzeAPK

class BytecodeInfo:
    def __init__(
        self,
        smali,
        method,
        offset,
        source
    ):
        self.smali= smali
        self.method = method
        self.offset = offset
        self.source = source

    def __eq__(self, obj):
        return self.__hash__ == obj.__hash__

    def __hash__(self):
        return hash(self.__dict__)

def extractShurikenBytecodes(apkPath: str) -> Set[BytecodeInfo]:
    analysis = Apk(apkPath)
    shurikenResults = set()
    numOfMethod = (
        analysis.get_number_of_methodanalysis_objects()
    )
    for i in range(numOfMethod):
        methodAnalysis = analysis.get_analyzed_method_by_idx(
            i
        )
        
        disassembledMethod = analysis.get_disassembled_method(
            methodAnalysis.full_name.decode()
        )
        if methodAnalysis.external:
            return
        for j in range(disassembledMethod.n_of_instructions):
            rawSmali = disassembledMethod.instructions[j].disassembly.decode(
                errors="backslashreplace"
            )
            rawSmali
        numOfIns = disassembledMethod.n_of_instructions
        instructions = disassembledMethod.instructions[:numOfIns]

        method = (
            disassembledMethod.method_id.contents
        )
        input()

    return shurikenResults



def get_method_bytecode_for_an(
        method_analysis
    ) -> Set[BytecodeObject]:
        try:
            for (
                _,
                ins,
            ) in method_analysis.get_method().get_instructions_idx():
                bytecode_obj = None
                register_list = []

                # count the number of the registers.
                length_operands = len(ins.get_operands())
                if length_operands == 0:
                    # No register, no parameter
                    bytecode_obj = BytecodeObject(
                        ins.get_name(),
                        None,
                        None,
                    )
                else:
                    index_of_parameter_starts = None
                    for i in range(length_operands - 1, -1, -1):
                        if (
                            not isinstance(ins.get_operands()[i][0], Operand)
                            or ins.get_operands()[i][0].name != "REGISTER"
                        ):
                            index_of_parameter_starts = i
                            break

                    if index_of_parameter_starts is not None:
                        parameter = ins.get_operands()[
                            index_of_parameter_starts
                        ]
                        parameter = (
                            parameter[2]
                            if len(parameter) == 3
                            else parameter[1]
                        )

                        for i in range(index_of_parameter_starts):
                            register_list.append(
                                "v" + str(ins.get_operands()[i][1]),
                            )
                    else:
                        parameter = None
                        for i in range(length_operands):
                            register_list.append(
                                "v" + str(ins.get_operands()[i][1]),
                            )

                    bytecode_obj = BytecodeObject(
                        ins.get_name(), register_list, parameter
                    )

                yield bytecode_obj
        except AttributeError:
            # TODO Log the rule here
            pass

def extractAndroguardBytecodes(apkPath: str) -> List[BytecodeInfo]:
    _, _, analysis = AnalyzeAPK(apkPath)
    androguardResults = set()
    for cls in analysis.get_classes():
        for method in cls.get_methods():
            set.update(get_method_bytecode_for_an(method))
    return androguardResults

def compareBytecodeInfo(shurikenBytecodes: List[BytecodeInfo], androguardBytecodes: List[BytecodeInfo]) -> List[dict]:
    comparison_results = []

    allBytecodes = set(shurikenBytecodes) & set(androguardBytecodes)

    for bytecode in allBytecodes:
        comparison_results.append({
            "smali": bytecode.smali,
            "method": bytecode.method,
            "offset": bytecode.offset,
            "source": bytecode.source,
        })

    return comparison_results

def save_to_csv(data: List[dict], outputPath: str):
    with open(outputPath, mode='w', newline='', encoding='utf-8') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

def main(apkPaths: List[str], outputCsv: str):
    allComparisonResults = []

    for apk_path in apkPaths:
        shurikenBytecodes = extractShurikenBytecodes(apk_path)
        androguardBytecodes = extractAndroguardBytecodes(apk_path)

        comparisonResults = compareBytecodeInfo(shurikenBytecodes, androguardBytecodes)
        allComparisonResults.extend(comparisonResults)

    save_to_csv(allComparisonResults, outputCsv)


if __name__ == "__main__":
    apkDir = "./apks/"
    apkFiles = sorted(
        [os.path.join(apkDir, f) for f in os.listdir(apkDir) if f.endswith("apk")]
    )
    output_csv_path = "bytecode_results.csv"
    main(apkFiles, output_csv_path)

